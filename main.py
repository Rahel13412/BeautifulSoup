from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)
print(soup.prettify())
print(soup.a)  # print first anchor tag
all_anchor_tag = soup.find_all(name="a")  # finding by tag name
print(all_anchor_tag)  # print list of all anchor tag

for tag in all_anchor_tag:
    print(tag.get_text())  # print all the text inside anchor tag
    print(tag.get("href"))  # print all the link

h1_heading = soup.find(name="h1", id="name")  # finding by tag and attribute name
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.name)  # printing the htlm element name.
print(section_heading.get("class"))  # printing the valve of class attribute.

company_url = soup.select_one(selector="p a")  # css selector
name = soup.select_one(selector="#name")  # id selector
soup.select(selector=".heading")  # class selector
