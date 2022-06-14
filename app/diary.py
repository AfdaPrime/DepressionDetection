# %%
import os
import sqlite3 as sql
from datetime import datetime
import model
import numpy as np
import text_cleaning as tc

# %%



# database connection
path = os.path.join('./db', 'diary.db')
conn = sql.connect(path)

c = conn.cursor()



# %%    INSERT DATA INTO DATABASE
# insert the data into the database

def insert(text,user_id):
    
    # current time the diary insert
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d")

    # predict the depression level of the text
    x = tc.text_cleaning(text)


    level = model.predict_sentiment([x])
    emoji = model.predict_image()


    c.execute(
        "INSERT INTO diary (content,time,depression_level,emoji,userId) VALUES (?,?,?,?,?)", (text, current_time, np.float32(level[0][0]).item(),emoji,user_id))

    conn.commit()
# %%    VEIW DATA

def view(user_id):

    c.execute("SELECT * FROM diary WHERE userId = ? ORDER BY id DESC ", [user_id])

    result = c.fetchall()

    return result

