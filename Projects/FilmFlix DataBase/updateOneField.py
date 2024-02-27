from connect import *

def update_one_field():
    try:
        fID = int(input("Enter the film ID to update a record: "))
        print("")
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {fID}")

        row = dbCursor.fetchone()
        if row == None:
            print(F"No record with the film ID {fID} exists!")
        else:
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {fID}")
            beforeUpdate = dbCursor.fetchone()
            print(f"Current Film details: \n{beforeUpdate}")
            print("")

            fieldName = input("Enter the field (title, yearReleased, rating, duration, genre) you would like to update: ")
            print("")

            if fieldName in ["title", "rating", "genre"]:
                fieldValue = input(f"Enter the updated value for {fieldName}: ")
            elif fieldName in ["yearReleased", "duration"]:
                fieldValue = int(input(f"Enter the updated value for {fieldName}: "))
                print("")

            dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = ? WHERE filmID = ?", (fieldValue, fID))
            dbConnect.commit()
            
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {fID}")
            afterUpdate = dbCursor.fetchone()
            print(f"Record {fID} has been updated in the films table; please see the changes below: ")
            print(afterUpdate)
            print("")

    except sql.OperationalError as e:
        print(f"Failed because: {e}")

    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")

if __name__ == "__main__":
    update_one_field()
