from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")
yc_response = response.text

soup = BeautifulSoup(yc_response, "html.parser")
article= soup.find_all(name = "span",class_= "titleline",)

articles = []
article_links = []
article_upvotes = []

for art in article:
    li=art.getText()
    articles.append(li)
    link = art.find(name= "a").get("href")
    article_links.append(link)

# print(n)
# article_link= n.get("href")
article_upvote = soup.find_all(name="span", class_= "score")
for b in article_upvote:
    vote = int(b.getText().split()[0])
    article_upvotes.append(vote)

# print(articles)
# print(article_links)
# print(article_upvotes)


largest_number = max(article_upvotes)
index = article_upvotes.index(largest_number)
print(largest_number)
print(articles[index])
print(article_links[index])


# print(article_upvote)
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# anchor_tags = soup.find_all(name="a")
# for tag in anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id= "name")
# print(heading)
# section = soup.find(name="h3", class_ = "heading")
# print(section)
# print(soup.find_all(name="a"))

# company_url = soup.select_one(selector= "p a")
#
# name =soup.select(".heading")
#
# print(company_url)
# print(name)