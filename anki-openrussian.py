import re
import requests_cache
from bs4 import BeautifulSoup as bs
from word import Word

#this is the ez mode way of doing this
#import pandas as pd
#df_pandas = pd.read_html(url, attrs = {'class': 'wordlist'}, flavor='bs4', thousands='.')

#open a requests cache
cached_session = requests_cache.CachedSession('openrussian_cache')
#make a list of words
saved_words = []

#openrussian database urls
url = 'https://en.openrussian.org'
list_ext = '/list/all'
paging_ext = '?start='

#get initial response from url or cache
response = cached_session.get(url + list_ext)

#parse response content with beautifulsoup
soup = bs(response.content, 'html.parser')

#find the paging span tag, which contains the range of words available
paging = soup.find(class_='paging')
paging_span = paging.span.string.split()
#get the current range
current_range = paging_span[0]
#get the max range
max_range = paging_span[2]

print(current_range, max_range)


#find the table with class="wordlist"
wordlist = soup.find(name='table', class_='wordlist')
#get the body of the table (we don't want the header)
wordlist_body = wordlist.tbody
#get all the data from each table row
for row in wordlist_body.find_all(name='tr'):
    #get the tag containing the word ranking
    rank_tag = row.find(class_='rank')
    word_rank = rank_tag.string
    #get the tag containing the word and its url
    name_url_tag = row.find(href=True)
    word_name = name_url_tag.string
    word_url = url + name_url_tag['href']
    #get all the english translations for the word
    translation_tags = row.find_all(class_='tl')
    word_translations = [tag.get_text().strip() for tag in translation_tags]
    #save this word as a word object
    saved_words.append(Word(rank=word_rank, word=word_name, url=word_url, translations=word_translations))

from wordwriter import WordWriter
writer = WordWriter('outputs/words.txt', saved_words)
writer.write()
