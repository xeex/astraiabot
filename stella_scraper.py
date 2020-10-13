# TODO: For now, you have to manually navigate to the Stella/Satellite table, and save the page as an HTML file
#       in order to scrape it. Automate this in the future.

import requests
from bs4 import BeautifulSoup
import sqlite3

def update_stella():
    conn = sqlite3.connect('Stellaverse.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS "stella" (
        "st"	INTEGER,
        "name"	TEXT,
        "artist"	TEXT,
        "baseURL"	TEXT,
        "sabunURL"	TEXT,
        "LR2IR"	TEXT UNIQUE
        )''')
    
    with open("Stella.html") as f: soup = BeautifulSoup(f, 'html.parser')
    charts = soup.find_all("tr", "tr_normal") # Find all charts
    for line in charts:
        chart = line.find_all("td")
        level, name, artist, _, _, _, _ = list(map(lambda x: x.text, chart))
        # Strip the 'st' off of the level
        level = level[2:]
        _, LR2IR, baseURL, sabunURL, _, _, _ = list(map(lambda x: x.a['href'] if (x.a is not None) else None, chart))
        
        # Insert into table
        t = (level, name, artist, baseURL, sabunURL, LR2IR)
        c.execute('''INSERT INTO Stella VALUES (?, ?, ?, ?, ?, ?)''', t)
    
    conn.commit()
    conn.close()

def update_satellite():
    conn = sqlite3.connect('Stellaverse.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS "satellite" (
        "sl"	INTEGER,
        "name"	TEXT,
        "artist"	TEXT,
        "baseURL"	TEXT,
        "sabunURL"	TEXT,
        "LR2IR"	TEXT UNIQUE
        )''')
    
    with open("Satellite.html") as f: soup = BeautifulSoup(f, 'html.parser')
    charts = soup.find_all("tr", "tr_normal") # Find all charts
    for line in charts:
        chart = line.find_all("td")
        level, name, artist, _, _, _, _ = list(map(lambda x: x.text, chart))
        # Strip the 'sl' off of the level
        level = level[2:]
        _, LR2IR, baseURL, sabunURL, _, _, _ = list(map(lambda x: x.a['href'] if (x.a is not None) else None, chart))
        
        # Insert into table
        t = (level, name, artist, baseURL, sabunURL, LR2IR)
        c.execute('''INSERT INTO satellite VALUES (?, ?, ?, ?, ?, ?)''', t)
    
    conn.commit()
    conn.close()

if __name___ == "__main__":
    update_satellite()
    update_stella()