from bs4 import BeautifulSoup
import requests

# The following variable set must be done because we want a better and more flexible output
# root variable now is re-usable
root = 'https://subslikescript.com'
website = f'{root}/movies'

result = requests.get(website)

content = result.text

soup = BeautifulSoup(content, 'lxml')

# Parameters contains the name of the tag plus the name of the class
# With this i take the whole <article> box
# Simple find() is used when i need to find one element
box = soup.find('article', class_="main-article")

# After i take on my hands the <article> box i must limit myself to the <a> tags
# Here we use find_all because we have multiple <a> tags (One <a> per transcript)
# For grabbing the <a> tags we have to set href to True
# With find_all i grab a list on my hands. So because it's a list i can use for loop to get access to individual elements

links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

print(links)

# The result after this print is not exactly what we want. We have to concatenate with "https://subslikescript.com"
# Let's say now that we want to grab more data from those individual links we grabbed into a grand list

for link in links:
    try:
        root = 'https://subslikescript.com'
        website = f'{root}/{link}'  # Now we want the ahref link not the movies url parameter
        result = requests.get(website)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')

        box = soup.find('article', class_="main-article")

        title = box.find('h1').get_text()
        transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

        with open(f'{title}.txt', 'w', encoding='utf-8') as file:
            file.write(transcript)

    except:
        print('------ Link is not working ------ ')
        print(link)
