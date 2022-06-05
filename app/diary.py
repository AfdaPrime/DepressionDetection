# %%
import os
import sqlite3 as sql
from datetime import datetime
from tkinter import NONE
import text_cleaning as tc
import model
import numpy as np

# %%

# database connection
path = os.path.join('../db', 'diary.db')
conn = sql.connect(path)

c = conn.cursor()

# %%    INSERT DATA INTO DATABASE


# insert the data into the database


def insert(text):
    # current time the diary insert
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # predict the depression level of the text
    x = tc.text_cleaning(text)

    level = model.predict_sentiment([x])

    c.execute(
        "INSERT INTO diary (content,time,depression_level) VALUES (?,?,?)", (text, current_time, np.float32(level[0][0]).item()))

    conn.commit()
# %%    VEIW DATA


x = 0


def view():

    global x

    # select content from x to x+10
    c.execute("SELECT id FROM diary WHERE id BETWEEN ? AND ?", (x, x+10))

    result = c.fetchall()

    if(result != []):
        print(result)
    else:
        print("at the end")
        prev()
    conn.commit()


def next():
    global x
    x += 11
    view()


def prev():
    global x

    if(x != 0):
        x -= 11
        view()
    else:
        print("at the begining")
        view()

# %%
