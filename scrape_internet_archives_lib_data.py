from bs4 import BeautifulSoup as bs
from urllib import request as req
import pandas as pd

# Change the number of pages to the page until you want the data 
number_of_pages = 1 

l_books = {
    "name": [],
    "author": []
}

for i in range(1, number_of_pages+1):
    url = req.urlopen('https://archive.org/details/internetarchivebooks?&sort=-downloads&page=%d' % i)
    soup = bs(url, 'html5lib')

    titles = []
    titles = [title for title in soup.find_all("div", {"class" : "ttl"})]

    for t in titles:
        try:
            fill_text = ""
            # print(t.parent.parent.find_next_siblings("div")[1].contents[3].text)
            fill_text = t.parent.parent.find_next_siblings("div")[1].contents[3].text
        except Exception:
            fill_text = " "
        finally:
            l_books["name"].append(' '.join(t.text.split()))
            l_books["author"].append(' '.join(fill_text.split()))
            # l_books.append({str(' '.join(t.text.split())) : str(' '.join(fill_text.split()))})
            # books[' '.join(t.text.split())] = ' '.join(fill_text.split())


# print(type(l_books))

columns = ["name", "author"]
books_df = pd.DataFrame(l_books, columns=["name", "author"])

print(books_df)

# I am having some problems saving the scraped data as csv. As I'm unable to find a good seperator
books_df.to_csv('internet_archive_lib_book_data.csv', encoding='utf-8')


