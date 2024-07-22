from urllib.request import urlopen
from bs4 import BeautifulSoup

def urllib_scrape(url):
    #scrapes
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    #get globals
    global titleString
    global authorString
    global bodyString
    
    if(titleString == ""):
        titleString = (soup.title.string)
    # Author
    if(authorString == ""):
        try:
            authorString = (soup.find(attrs={"rel": "author"}).get_text())
        except:
            authorString = ""
    if(bodyString == ""):
        bodyString = (soup.text)

