from connect import *

def delete_film():
    try:
        fID = int(input("Enter the filmID to delete a record: "))
        print("")
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {fID}")

        row = dbCursor.fetchone()
        if row == None:
            print(f"FilmID {fID} does not exist!")
        else:
            dbCursor.execute("DELETE FROM tblFilms WHERE filmID = ?", (fID,))
            dbConnect.commit()
            print("The following record has been deleted: ")
            print(row)
            print("")

    except sql.OperationalError as e:
        print(f"Failed because: {e}")

    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")

if __name__ == "__main__":
    delete_film()
