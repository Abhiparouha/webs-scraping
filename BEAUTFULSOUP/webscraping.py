import requests
from bs4 import BeautifulSoup
url =""
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
    linkText ="https://" +link.get('href')
    all_links.add(link)
    print(linkText)