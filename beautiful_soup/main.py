from bs4 import BeautifulSoup
import requests

# with open("website.html", "r", encoding="utf-8") as data:
#     data_html = data.read()
#
# soup = BeautifulSoup(data_html, "html.parser")
# print(soup.prettify())


def max_votes(upvotes):
    max_vote = 0
    max_index = None
    for index in range(len(upvotes)):
        if max_vote < upvotes[index]:
            max_vote = upvotes[index]
            max_index = index
    return max_index


response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
all_headline = soup.find_all(name="span", class_="titleline")
article_titles, article_upVotes, article_links = [], [], []
for headline in all_headline:
    article_titles.append(headline.find("a").getText())
    article_links.append(headline.find("a").get("href"))

article_upVotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
article_upVotes = [int(vote.split(" ")[0]) for vote in article_upVotes]

# print(article_titles)
# print(article_links)
# print(article_upVotes)
maxIndex = max_votes(article_upVotes)
print(article_titles[maxIndex])
print(article_links[maxIndex])
print(article_upVotes[maxIndex])
