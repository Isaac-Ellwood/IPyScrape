import sys
import tkinter as tk
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import http.client
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import ssl
import tkinter.ttk as ttk
import pickle

#sets recursion limit so save works
sys.setrecursionlimit(100000)

#globals
titleString = ""
authorString = ""
bodyString = ""

try:
    # Deserialize the object from the binary file
    with open('data.pkl', 'rb') as file:
        loaded_data = pickle.load(file)
        data = loaded_data
except:
    # Initialise empty list
    data = []

def save_data():
    # Append list
    data.append([titleString, authorString, bodyString])
    # Serialize the object to a binary format
    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)

def requests_scrape(url):
    r = requests.get(url)
    if r.status_code == 200:
        soup=BeautifulSoup(r.text,'html.parser')

        #get globals
        global titleString
        global authorString
        global bodyString

        # clear boxes
        title.delete("0",tk.END)
        author.delete("0",tk.END)
        body.delete("1.0",tk.END)

        # Get title
        try:
            titleString = soup.title.string
        except:
            titleString = ""
        # Get author
        try:
            authorString = soup.find(rel="author").get_text()
        except:
            authorString = ""
        # Get body text
        try:
            bodyString = soup.get_text()
        except:
            bodyString = ""
    else:
        # clear boxes
        title.delete("0",tk.END)
        author.delete("0",tk.END)
        body.delete("1.0",tk.END)
        # error
        body.insert('Error ', r.status_code)

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
    if(authorString == ""):
        try:
            authorString = (soup.find(attrs={"rel": "author"}).get_text())
        except:
            authorString = ""
    if(bodyString == ""):
        bodyString = (soup.text)

def sus_scrape(url):

    #get globals
    global titleString
    global authorString
    global bodyString

    # Parse the URL
    parsed_url = urlparse(url)
    context = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection(parsed_url.netloc, context=context)

    # Send the request
    conn.request("GET", parsed_url.path)
    response = conn.getresponse()

    # Check the status code
    if response.status == 200:
        data = response.read()
        soup = BeautifulSoup(data, 'html.parser')
        if(titleString == ""):
            titleString = (soup.title.string)
        if(authorString == ""):
            try:
                authorString = (soup.find(attrs={"rel": "author"}).get_text())
            except:
                authorString = ""
        if(bodyString == ""):
            bodyString = (soup.get_text())
    else:
        print('Error ', response.status)

    conn.close()

# When enter is clicked
def handle_click(event):
    # clear boxes
    loading.step(5)
    title.delete("0",tk.END)
    author.delete("0",tk.END)
    body.delete("1.0",tk.END)

    # add loading
    loading.step(5)
    title.insert(0, "loading")
    author.insert(0, "loading")
    body.insert(1.0,"loading")

    # scrape
    url = entry.get()
    requests_scrape(url)
    loading.step(50)
    #check
    if (titleString == "" or authorString == "" or bodyString == ""):
        urllib_scrape(url)
        loading.step(20)
        if (titleString == "" or authorString == "" or bodyString == ""):
            sus_scrape(url)
            loading.step(20)

    # format
    remove_whitespace()

    # insert
    title.insert(0, titleString)
    author.insert(0, authorString)
    body.insert("1.0", bodyString)

    # save data
    save_data()


# delete whitespace
def remove_whitespace():
    global bodyString
    bodyString.split('\n')
    bodyString = '\n'.join([line for line in bodyString.split('\n') if line.strip()])

# make window
window = tk.Tk()
# title
label = tk.Label(
    text="Hello, pljnniiiinklkkl",
    fg="white",
    bg="black",
    width=100,
    height=10
)
label.pack()
# url input
label = tk.Label(text="Paste or type URL")
entry = tk.Entry()
label.pack()
entry.pack()
# enter button
enter = tk.Button(
    text="Enter",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",)
enter.bind("<Button-1>", handle_click)
enter.pack()

# loading bar
loading = ttk.Progressbar()
loading.pack()

# title
title = tk.Entry()
title.pack()
# author
author = tk.Entry()
author.pack()
# body
body = tk.Text()
body.pack()

# SET DEFAULT URL
entry.insert(0, "https://www.newshub.co.nz/home/politics/2023/10/nz-election-2023-live-updates-results-analysis-reaction.html")

# main
window.mainloop()


