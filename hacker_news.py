from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup.prettify())

# print(soup.title)  # printing the title tag
# print(soup.title.text)  # printing the text inside the title tag

article_tag = soup.find(name="a", class_="titlelink")
print(article_tag)  # printing the first anchor tag
article_text = article_tag.get_text()
print(article_text)  # printing the text inside first anchor tag.
article_link = article_tag.get("href")
print(article_link)  # printing the link inside the first anchor_tag or getting the attribute value
article_upvote = soup.find(name="span", class_="score").get_text()
print(article_upvote)

articles_tag_list = soup.find_all(name="a", class_="titlelink")
print(articles_tag_list)  # printing all the anchor tag
articles_text_list = [article_tag.get_text() for article_tag in articles_tag_list]
print(articles_text_list)
articles_link_list = [article_tag.get("href") for article_tag in articles_tag_list]
print(articles_link_list)
articles_upvote_list = [int(item.get_text().split(" ")[0]) for item in soup.find_all(name="span", class_="score")]
print(articles_upvote_list)

highest_upvote = 0
for article_upvote in articles_upvote_list:
    if article_upvote > highest_upvote:
        highest_upvote = article_upvote
print(highest_upvote)

highest_upvote_index = articles_upvote_list.index(highest_upvote)
print(articles_text_list[highest_upvote_index])
print(articles_link_list[highest_upvote_index])

