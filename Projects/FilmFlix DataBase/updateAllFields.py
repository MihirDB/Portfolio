from connect import *

def update_all_fields():
    try:
        fID = int(input("Enter the film ID to update a record: "))
        print("")
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {fID}")

        row = dbCursor.fetchone()
        if row == None:
            print(f"No record with the film ID {fID} exists!")
        else:
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {fID}")
            beforeUpdate = dbCursor.fetchone()
            print(f"Current Film details: \n{beforeUpdate}")
            print("")

            fTitle = input("Enter the new film title: ")
            fYearReleased = int(input("Enter the new year the film was released: "))
            fRating = input("Enter the new film rating: ")
            fDuration = int(input("Enter the new film duration: "))
            fGenre = input("Enter the new film genre: ")
            print("")

            dbCursor.execute("UPDATE tblFilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ? WHERE filmID = ?", (fTitle, fYearReleased, fRating, fDuration, fGenre, fID))
            dbConnect.commit()

            print(f"Record {fID} has been updated in the films table; please see the changes below: ")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {fID}")
            afterUpdate = dbCursor.fetchone()
            print(afterUpdate)
            print("")

    except sql.OperationalError as e:
        print(f"Failed because: {e}")

    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")

if __name__ == "__main__":
    update_all_fields()
