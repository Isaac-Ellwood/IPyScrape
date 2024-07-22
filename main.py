import tkinter as tk
import requests
from bs4 import BeautifulSoup

#globals
titleString = ""
authorString = ""
bodyString = ""


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

# When enter is clicked
def handle_click(event):
    # clear boxes
    title.delete("0",tk.END)
    author.delete("0",tk.END)
    body.delete("1.0",tk.END)

    # add loading
    title.insert(0, "loading")
    author.insert(0, "loading")
    body.insert(1.0,"loading")

    # scrape
    url = entry.get()
    requests_scrape(url)
    title.insert(0, titleString)
    author.insert(0, authorString)
    body.insert("1.0", bodyString)

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
# title
title = tk.Entry()
title.pack()
# author
author = tk.Entry()
author.pack()
# body
body = tk.Text()
body.pack()
window.mainloop()


