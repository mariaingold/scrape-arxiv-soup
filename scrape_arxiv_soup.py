# AROS v 0.1 (Academic Research Online System)
# Simple reflex agent web scraper
# Scrapes a specific arxiv page for basic citation data and stores in a CSV file
# Uses Python, requests, Beautiful Soup 4, Pandas 
#
# Author: Maria Ingold
# Built as part of UoEO MSc AI Intelligent Agents assignment

import requests
from bs4 import BeautifulSoup
import pandas as pd

# COLLECT 

# GET the url
page = requests.get("https://arxiv.org/abs/2109.00656")

content = page.content

# EXTRACT

# Parse the webpage content
soup = BeautifulSoup(content,"html.parser")
print (soup.prettify()) # Print the HTML contents of the page
#print(soup.get_text()) # Print the text of the page

# Extract the citation title
meta_tag = soup.find("meta", attrs={"name": "citation_title"})  
citation_title = meta_tag["content"] if meta_tag else "No meta title given"
print(citation_title)

# Extract the citation author
meta_tags = soup.find_all("meta", attrs={"name": "citation_author"})
citation_authors = [tag["content"] for tag in meta_tags if tag] if meta_tag else "No meta author given"
# print(citation_authors)
for author in citation_authors:
    print(author)

# Extract the citation date
meta_tag = soup.find("meta", attrs={"name": "citation_date"})
citation_date = meta_tag["content"] if meta_tag else "No meta date given"
print(citation_date)

# TRANSFORM

# Create a dictionary
data = {
    "Title": [citation_title],
    "Authors": [" and ".join(citation_authors)],
    "Date": [citation_date]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# STORE

# Export the DataFrame to a CSV file
df.to_csv("citation_data.csv", index=False)
