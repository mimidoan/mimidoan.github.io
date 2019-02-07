from bs4 import BeautifulSoup, SoupStrainer
import requests
import re

def main():
    file = open('longings.txt', 'w')
    get_titles(file)

def get_titles(file):
    pages = []
    url = 'https://www.goodreads.com/quotes/tag/longing'
    pattern = r'"([A-Za-z0-9_\./\\-]*)"'
    
    for link in range(1,26):
	    pages.append(url + "?page=" + str(link))
    
    for item in pages:
        page = requests.get(item)
        if page:
            soup = BeautifulSoup(page.text, 'html.parser')
            quoteText = soup.findAll('div', {'class': 'quoteText'})
            # print(quoteText)

            for each in quoteText:
                a = each.contents[0].replace('”', '').replace('“', '').replace('"', '')
                # print(a)
                file.write(a + "\n")

if __name__ == "__main__":
    main()
