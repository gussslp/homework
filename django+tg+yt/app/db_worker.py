import sqlite3
from datetime import datetime


def add_video(song_title,author,link):
    connection = sqlite3.connect('..\db.sqlite3')    
    c = connection.cursor()
    c.execute("""INSERT INTO app_yt_video 
    (title,author,link,time)
    VALUES ('%s', '%s', '%s', '%s')
    """%(song_title,author,link,datetime.now()))
    connection.commit()
    c.close()
