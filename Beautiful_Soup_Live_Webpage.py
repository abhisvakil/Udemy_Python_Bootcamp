from bs4 import BeautifulSoup
import requests
#Beautiful soup code to extract live website and perform various operations such as fetching particular anchor tags

response = requests.get("https://news.ycombinator.com/news")
#print(response.text)
yc_web_page = response.text

#Creating beatiful soup object and passing the data with which we are working
soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)
print(soup.find(name="span", class_="titleline").getText())

articles = soup.find_all(name='a', class_="title")
article_texts=[]
article_links=[]
for article_tag in articles:
    text=article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes=[score.getText() for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
largest_number=max(article_upvotes)
largest_index=article_upvotes.index(largest_number)

#printing value with the largest index from article text
print(article_texts[largest_index])
print(article_texts[largest_index])
article_with_highest_score=[text.getText for text in soup.find(name='span', class_="score") if max(article_upvotes)]
print(article_with_highest_score)


