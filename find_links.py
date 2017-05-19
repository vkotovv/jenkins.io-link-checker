from BeautifulSoup import BeautifulSoup
import urllib2
import re
import urlparse

root_page = "https://jenkins.io"
    
def parse_blog():
    parse_blog_page_one()
    LAST_PAGE = 63
    for i in range(2, LAST_PAGE + 1):
        parse_blog_page(i)

def parse_solutions():
    print_links(root_page, "solutions/")

def parse_blog_page_one():
    page_url = root_page + "/node"
    print_links(page_url, "blog/")

def parse_blog_page(i):
    blog_page_url = root_page + "/node/page/" + str(i) + ".html"
    print_links(blog_page_url, "blog/")

def parse_docs():
    docs_root_page = root_page + "/doc/"
    url_template = "https://jenkins.io/doc/"
    links = get_links(docs_root_page, url_template)
    result = []
    for link in links:
        # get 2nd level links from the main /doc page
        result.extend(get_links(link, url_template))
    
    unique_links = list(set(result))
    for link in unique_links:
        print link

def get_links(url, search_term):
    ''' Find all links that contain specific search_term in URL '''
    links = []
    html_page = urllib2.urlopen(url)
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        result = ''
        parsed_url = link.get('href')
        if parsed_url is not None and parsed_url.startswith('http'):
            result = parsed_url
        else:
            result = urlparse.urljoin(root_page, parsed_url)
        if search_term in result and result not in links:
            # no duplicates
            links.append(result)
    return links

def print_links(url, search_term):
    links = get_links(url, search_term)
    for link in links:
        print link

if __name__ == "__main__":
    parse_solutions()
    parse_blog()
    parse_docs()
