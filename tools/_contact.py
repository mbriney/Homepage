"""Single source of truth for the public contact address.

The address is never emitted into the served HTML. `mail_link()` writes
reversed, split data-* attributes; assets/js/nav.js reassembles the mailto
at runtime. To switch to an alias later, change MAIL_USER / MAIL_DOMAIN
here and rebuild — nothing else needs to change.
"""

MAIL_USER   = "mkbriney"
MAIL_DOMAIN = "gmail.com"


def mail_link(text=None, subject=None, cls=None, show=False):
    """Return an <a> that JS turns into a real mailto.

    text=None + show=True  -> JS fills in the address as the link text
    """
    attrs = [
        f'data-cu="{MAIL_USER[::-1]}"',
        f'data-cd="{MAIL_DOMAIN[::-1]}"',
    ]
    if subject:
        attrs.append(f'data-cs="{subject}"')
    if show:
        attrs.append('data-cshow="1"')
    if cls:
        attrs.append(f'class="{cls}"')
    label = text if text is not None else "email me"
    return f'<a href="#" {" ".join(attrs)}>{label}</a>'
