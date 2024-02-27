from connect import *

def all_films():
    try:
        dbCursor.execute("SELECT * FROM tblFilms")
        allFilms = dbCursor.fetchall()

        if allFilms:
            print("filmID | title | yearReleased | rating | duration | genre")
            print("---------------------------------------------------------")
        
            for aFilm in allFilms:
                print(f"{aFilm[0]} | {aFilm[1]} | {aFilm[2]} | {aFilm[3]} | {aFilm[4]} | {aFilm[5]}")
        else:
            print("No films found in the table!")
    
    except sql.OperationalError as error:
        print(f"Failed because: {error}")
    
    except sql.ProgrammingError as programmingError:
        print(f"Not working becuse: {programmingError}")
    
    finally:
        print("DB operation performed")
        print("")

if __name__ == "__main__":
    all_films()