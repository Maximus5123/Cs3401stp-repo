from bs4 import BeautifulSoup

import requests

html_text=requests.get('https://www.reddit.com/r/movies/comments/155ag1m/official_discussion_oppenheimer_spoilers/').text
#print(html_text)

with open ('output.txt', 'w')as file:
 file.write(html_text)