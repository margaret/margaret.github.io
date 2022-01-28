Personal Website
================

Visit it at :arrow_right: https://margaretsy.com

## Notes

### 404 pages

The `.htcaccess` file is configured to use the static `404.html` page as the 404 page. If you remove it, a generic 404 page is used. The `@app.errorhandler(404)` in `site.py` will serve the 404 page when the site is running live from the command `python site.py`.

## How's the DNS stuff work?

Custom domain is hosted on Namecheap, so follow https://www.namecheap.com/support/knowledgebase/article.aspx/9645/2208/how-do-i-link-my-domain-to-github-pages

There's a confusing bit at the end where they give you conflicting info about deleting duplicate entries, but you should set both `192.30.252.153` and `192.30.252.154` as `A Record`s.
