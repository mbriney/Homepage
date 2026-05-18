/* Site-wide GA4 instrumentation: outbound clicks, PDF downloads,
   Vimeo + YouTube video engagement.
   Lightbox open events are fired separately from nav.js. */
(function () {
  if (typeof gtag !== 'function') return;
  var SOURCE_PAGE = location.pathname;

  /* ---------- 1. Outbound clicks + PDF downloads ---------- */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a');
    if (!a) return;
    var href = a.getAttribute('href');
    if (!href || href.charAt(0) === '#') return;

    var url;
    try { url = new URL(href, location.href); } catch (_) { return; }

    // PDF / download files first — these always count even on same domain.
    var ext = (url.pathname.match(/\.([a-z0-9]+)$/i) || [])[1];
    var DL_EXT = ['pdf','docx','doc','xlsx','xls','pptx','ppt','zip'];
    if (ext && DL_EXT.indexOf(ext.toLowerCase()) !== -1) {
      gtag('event', 'file_download', {
        file_name: url.pathname.split('/').pop(),
        file_extension: ext.toLowerCase(),
        link_text: (a.textContent || '').trim().slice(0, 80),
        link_url: url.href,
        source_page: SOURCE_PAGE
      });
      // For the CV resume specifically, also fire a friendly named event
      // so it's easy to mark as a key event / conversion in GA4 admin.
      if (/resume|cv/i.test(url.pathname)) {
        gtag('event', 'resume_download', {
          file_name: url.pathname.split('/').pop(),
          source_page: SOURCE_PAGE
        });
      }
      return;
    }

    // Outbound link (external host)
    if (url.host && url.host !== location.host) {
      gtag('event', 'outbound_click', {
        link_url: url.href,
        link_domain: url.host,
        link_text: (a.textContent || '').trim().slice(0, 80),
        source_page: SOURCE_PAGE
      });
    }
  }, true);

  /* ---------- 2. Vimeo video tracking ---------- */
  var vimeoIframes = Array.prototype.slice.call(
    document.querySelectorAll('iframe[src*="player.vimeo.com"]')
  );
  if (vimeoIframes.length) {
    var vs = document.createElement('script');
    vs.src = 'https://player.vimeo.com/api/player.js';
    vs.async = true;
    vs.onload = function () {
      vimeoIframes.forEach(function (iframe) {
        if (!window.Vimeo || !window.Vimeo.Player) return;
        var player = new window.Vimeo.Player(iframe);
        var id = (iframe.src.match(/video\/(\d+)/) || [])[1] || 'unknown';
        var title = iframe.getAttribute('title') || '';
        var fired = { start:false, p25:false, p50:false, p75:false, end:false };
        var duration = 0;

        player.getDuration().then(function (d) { duration = d; });

        player.on('play', function () {
          if (fired.start) return;
          fired.start = true;
          gtag('event', 'video_start', meta());
        });

        player.on('timeupdate', function (d) {
          if (!duration) return;
          var pct = d.seconds / duration;
          if (pct >= 0.25 && !fired.p25) { fired.p25 = true; progress(25); }
          if (pct >= 0.50 && !fired.p50) { fired.p50 = true; progress(50); }
          if (pct >= 0.75 && !fired.p75) { fired.p75 = true; progress(75); }
        });

        player.on('ended', function () {
          if (fired.end) return;
          fired.end = true;
          gtag('event', 'video_complete', meta());
        });

        function meta(extra) {
          return Object.assign({
            video_provider: 'vimeo',
            video_id: id,
            video_title: title,
            source_page: SOURCE_PAGE
          }, extra || {});
        }
        function progress(pct) {
          gtag('event', 'video_progress', meta({ video_percent: pct }));
        }
      });
    };
    document.head.appendChild(vs);
  }

  /* ---------- 3. YouTube video tracking via IFrame API ---------- */
  var ytIframes = Array.prototype.slice.call(
    document.querySelectorAll(
      'iframe[src*="youtube-nocookie.com/embed"], iframe[src*="youtube.com/embed"]'
    )
  );
  if (ytIframes.length) {
    // Enable JS API on each iframe (modifies src before YT API instantiates them)
    ytIframes.forEach(function (iframe) {
      if (!/[?&]enablejsapi=/.test(iframe.src)) {
        iframe.src = iframe.src + (iframe.src.indexOf('?') === -1 ? '?' : '&') + 'enablejsapi=1';
      }
    });

    // Load the YT IFrame API
    var ys = document.createElement('script');
    ys.src = 'https://www.youtube.com/iframe_api';
    ys.async = true;
    document.head.appendChild(ys);

    window.onYouTubeIframeAPIReady = function () {
      ytIframes.forEach(function (iframe) {
        var id = (iframe.src.match(/embed\/([A-Za-z0-9_-]+)/) || [])[1] || 'unknown';
        var title = iframe.getAttribute('title') || '';
        var fired = { start:false, p25:false, p50:false, p75:false, end:false };
        var duration = 0;
        var pollTimer = null;

        new window.YT.Player(iframe, {
          events: {
            'onReady': function (e) {
              try { duration = e.target.getDuration() || 0; } catch (_) {}
            },
            'onStateChange': function (e) {
              var YT = window.YT;
              if (e.data === YT.PlayerState.PLAYING) {
                if (!fired.start) {
                  fired.start = true;
                  gtag('event', 'video_start', meta());
                }
                if (pollTimer) clearInterval(pollTimer);
                pollTimer = setInterval(function () {
                  try {
                    if (!duration) duration = e.target.getDuration() || 0;
                    var t = e.target.getCurrentTime();
                    if (!duration || !t) return;
                    var pct = t / duration;
                    if (pct >= 0.25 && !fired.p25) { fired.p25 = true; progress(25); }
                    if (pct >= 0.50 && !fired.p50) { fired.p50 = true; progress(50); }
                    if (pct >= 0.75 && !fired.p75) { fired.p75 = true; progress(75); }
                  } catch (_) {}
                }, 1000);
              } else if (e.data === YT.PlayerState.PAUSED) {
                if (pollTimer) { clearInterval(pollTimer); pollTimer = null; }
              } else if (e.data === YT.PlayerState.ENDED) {
                if (pollTimer) { clearInterval(pollTimer); pollTimer = null; }
                if (!fired.end) {
                  fired.end = true;
                  gtag('event', 'video_complete', meta());
                }
              }
            }
          }
        });

        function meta(extra) {
          return Object.assign({
            video_provider: 'youtube',
            video_id: id,
            video_title: title,
            source_page: SOURCE_PAGE
          }, extra || {});
        }
        function progress(pct) {
          gtag('event', 'video_progress', meta({ video_percent: pct }));
        }
      });
    };
  }
})();
