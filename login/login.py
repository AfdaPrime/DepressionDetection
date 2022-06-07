# %%
import os
import sqlite3 as sql

# %%

# database connection
path = os.path.join('../db', 'diary.db')
conn = sql.connect(path)

c = conn.cursor()

# %% TO authentication FOR FIRST TIME AND LOGOUT


def authentication(username, password):

    c.execute('SELECT * FROM diary')

    result = c.fetchone()

# if database is empty(first time) go to signup else login
    if(result != []):
        signup(username, password)
    else:
        login(password)

# %% FIRST TIME SIGNUP


def signup(username, password):

    c.execute(
        "INSERT INTO user (name,password) VALUES (?,?)", (username, password))

# after signup tp login
    login(password)

# %% LOGIN


def login(password):

    c.execute("SELECT password FROM user ")

    result = c.fetchone()

    if(password == result):
        return True
    else:
        return False

# %% FUNCTION TO change password


def change_password(password):

    c.execute("UPDATE user SET password = ? WHERE id = 1", (password))
    return True
# %% DELETE AN ACC


def delete_account(password):

    # if the password is correct then clear the database(diary and user)
    if (login(password)):
        c.execute("DELETE FROM user WHERE id = 1")
        c.execute("DELETE FROM diary")
        return True
    else:
        print("you are not authencanted")
        return False
