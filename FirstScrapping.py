from bs4 import BeautifulSoup
import requests

website = "https://subslikescript.com/movie/Titanic-120338"

result = requests.get(website)

content = result.text

soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify())

# Takes the contents of the whole article tag
box = soup.find('article', class_='main-article')

# print(box)

# Instead of soup i can use the box i defined previously to be more explicit
# soup.find('h1').get_text()
title = box.find('h1').get_text()

# The parameters exist to make our outcome more readable
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
print(transcript)

print(title)

# with this {title} i give my code a more dynamic character
with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)