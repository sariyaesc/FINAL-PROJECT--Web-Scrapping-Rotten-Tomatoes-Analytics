import sqlite3
import pandas as pd

df=pd.read_csv("Web_Scrap/dataset/On-Theaters-Rotten-Tomatoes-12-08-2023.csv")
conn=sqlite3.connect('pruebatomato.db')
cursor= conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
               Id INTEGER PRIMARY KEY AUTOINCREMENT,
               Title TEXT NOT NULL,
               Critics TEXT NOT NULL,
               Audience TEXT NOT NULL,
               Premiere TEXT NOT NULL
               )''')

for index, row in df.iterrows():
    cursor.execute("INSERT INTO usuarios (Title, Critics, Audience, Premiere) VALUES (?,?,?,?)",
                   (row['Titles'], row['Critics Score'], row['Audience Score'], row['Premiere']))
conn.commit()
conn.close()

