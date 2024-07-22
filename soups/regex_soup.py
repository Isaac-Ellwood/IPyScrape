import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
url = "https://www.newshub.co.nz/home/politics/2023/10/nz-election-2023-live-updates-results-analysis-reaction.html"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)  # Remove HTML tags

authorPattern = "<author.*?>.*?</author.*?>"
match_results = re.search(authorPattern, html, re.IGNORECASE)
try:
    author = match_results()
    author = re.sub("<.*?>", "", author)  # Remove HTML tags
    print(author)
except:
    print("FUCKKKKK")
print(title)