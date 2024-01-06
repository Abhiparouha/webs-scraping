import requests
from bs4 import BeautifulSoup
url ="https://www.amazon.in/b/?_encoding=UTF8&node=15325111031&pd_rd_w=z7mBk&content-id=amzn1.sym.b25e0925-6d5c-48be-9247-464080b72908&pf_rd_p=b25e0925-6d5c-48be-9247-464080b72908&pf_rd_r=FGW555MN43TBBMTJDW51&pd_rd_wg=9KGPE&pd_rd_r=06b79353-01f7-416c-8cd7-4037a4611a7b"
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)
title=soup.title
# print(type(title))
# print(type(soup))
# print(type(title.string))
# get the title of the paragraphs from the page
paras = soup.find_all('p')
# print(paras)
# get the title of the anchor tags from the page
anchors= soup.find_all('a')
# print(anchors)

# get first element in the html pages
print(soup.find('p'))

# get classes of any elements in the html Pages

print(soup.find('p')['class'])

#find all the elements with class lead
print(soup.find_all("p", class_="lead"))

#get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())
# get the title of the anchor tags from the page
anchors= soup.find_all('a')
all_links = set()
#get all the links on the page:
for link in anchors:
    if(link.get('href') !='#');
    linkText ="https://www.amazon.in/b/?_encoding=UTF8&node=15325111031&pd_rd_w=z7mBk&content-id=amzn1.sym.b25e0925-6d5c-48be-9247-464080b72908&pf_rd_p=b25e0925-6d5c-48be-9247-464080b72908&pf_rd_r=FGW555MN43TBBMTJDW51&pd_rd_wg=9KGPE&pd_rd_r=06b79353-01f7-416c-8cd7-4037a4611a7b" +link.get('href')
    all_links.add(link)
    print(linkText)