from connect import *

def insert_film():
    try:
        dbCursor.execute("SELECT filmID FROM tblFilms")
        ids = [row[0] for row in dbCursor.fetchall()]
        
        fID = int(input("Enter the filmID: "))
        print("")
        while fID in ids:
            fID = input(f"Film ID {fID} already exists, please enter another filmID: ")

        fTitle = input("Enter the film title: ")
        fYearReleased = int(input("Enter the year the film was released: "))
        fRating = input("Enter the film rating: ")
        fDuration = int(input("Enter the film duration: "))
        fGenre = input("Enter the film genre: ")
        print("")

        dbCursor.execute("INSERT INTO tblFilms VALUES(?, ?, ?, ?, ?, ?)", (fID, fTitle, fYearReleased, fRating, fDuration, fGenre))
        dbConnect.commit()

        dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {fID}")
        newFilm = dbCursor.fetchone()
        print(f"You have added {fTitle} to the table: ")
        print(newFilm)
        print("")

    except sql.OperationalError as e:
            print(f"Failed because: {e}")

    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")

    except sql.Error as er:
        print(f"This error occurs: {er}")

if __name__ == "__main__":
    insert_film()
    