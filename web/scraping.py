# Beautiful Soup is a Python library designed for quick turnaround projects like screen-scraping. Three features make it powerful:
#
# Beautiful Soup provides a few simple methods and Pythonic idioms for navigating, searching, and modifying a parse tree: a toolkit for dissecting a document and extracting what you need. It doesn't take much code to write an application
# Beautiful Soup automatically converts incoming documents to Unicode and outgoing documents to UTF-8. You don't have to think about encodings, unless the document doesn't specify an encoding and Beautiful Soup can't detect one. Then you just have to specify the original encoding.
# Beautiful Soup sits on top of popular Python parsers like lxml and html5lib, allowing you to try out different parsing strategies or trade speed for flexibility.

import requests
from bs4 import BeautifulSoup

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')

# To get HTML format
print(soup.prettify())

# To get text only
print(soup.get_text())

# To print particular tags in HTML
res = soup.a
# res = soup.a.img
print(res.prettify())
print(res.get_text())

# Filtering methods # find_all()

print(soup.findAll('li'))


# Downloading And Scraping The Contents Of A Web Page

url = "http://www.ibm.com"
data  = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")  # create a soup object using the variable 'data'
for link in soup.find_all('a', href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))

for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))