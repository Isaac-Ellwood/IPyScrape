import tkinter as tk
import requests
from bs4 import BeautifulSoup



# When enter is clicked
def handle_click(event):
    # clear boxes
    title.delete("0",tk.END)
    author.delete("0",tk.END)
    output.delete("1.0",tk.END)
    # add loading
    title.insert(0, "loading")
    author.insert(0, "loading")
    output.insert(1.0,"loading")

    # scrape
    url = entry.get()
    r = requests.get(url)
    if r.status_code == 200:
        soup=BeautifulSoup(r.text,'html.parser')

        # clear boxes
        title.delete("0",tk.END)
        author.delete("0",tk.END)
        output.delete("1.0",tk.END)

        # Get title
        try:
            title.insert(0, soup.title.string)
        except:
            title.insert(0, "No title found")
        # Get author
        try:
            author.insert(soup.find(rel="author").get_text())
        except:
            author.insert(0, "No author found")
        # Get body text
        try:
            output.insert("1.0", soup.get_text())
        except:
            output.insert("No content found")
    else:
        # clear boxes
        title.delete("0",tk.END)
        author.delete("0",tk.END)
        output.delete("1.0",tk.END)
        # error
        output.insert('Error ', r.status_code)

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
# output
output = tk.Text()
output.pack()
window.mainloop()


