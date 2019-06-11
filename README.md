Scripts to find and check the links on /solutions, /doc and /blog parts of https://jenkins.io.

You will need Python 2 + BeautifulSoup, https://github.com/stevenvachon/broken-link-checker installed.

Usage example:
```
python find_links.py --blog_pages=5 > links.txt
./check_links.sh
```

