from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
movies_names = [tag.get_text() for tag in soup.select(selector="h3 a")]
release_years = [tag.get_text() for tag in soup.find_all(name="span", class_="lister-item-year text-muted unbold")]
movies_ratings = [tag.get_text() for tag in soup.find_all(name="span", class_="certificate")]
movies_durations = [tag.get_text() for tag in soup.find_all(name="span", class_="runtime")]
movies_genres = [tag.get_text().strip() for tag in soup.find_all(name="span", class_="genre")]
movies_directors = [tag.get_text().strip() for tag in soup.find_all(name="span", class_="genre")]
movies_votes = [item.get_text().split("\n")[2] for item in soup.find_all(name="p", class_="sort-num_votes-visible")]
gross_revenues = [item.get_text().split("\n")[4] for item in soup.find_all(name="p", class_="sort-num_votes-visible")]
imdb_ratings = [tag.get("data-value") for tag in soup.find_all(name="div", class_="inline-block ratings-imdb-rating")]

with open("movies.txt", mode="w") as file:
    file.write("movies_name,release_year,movie_directors,rating,duration,genres,imdb_rating,votes,revenue\n")
    for i in range(49):
        file.write(
            f"{i},{movies_names[i]},{release_years[i]},{movies_directors[i]},{movies_ratings[i]},{movies_durations[i]},"
            f"{movies_genres[i]},{imdb_ratings[i]},{movies_votes[i]},{gross_revenues[i]}\n")
