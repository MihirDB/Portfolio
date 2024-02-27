import sqlite3 as sql

try:
    with sql.connect("Week 11 - Python Project/FilmFlix DataBase/filmflix.db") as dbConnect:
        dbCursor = dbConnect.cursor()

except sql.OperationalError as error:
    print(f"Connection failed: {error}")