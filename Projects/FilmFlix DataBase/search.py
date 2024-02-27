from connect import *

def search_film():
    try:
        field = input("Please enter the field name you like to search by (filmID, title, yearReleased, rating, duration, genre): ")
        print("")

        if field in ["filmID", "yearReleased", "duration"]:
            idInput = int(input(f"Enter the value for the field {field}: "))
            print("")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} = {idInput}")

            row = dbCursor.fetchall()
            if row == None:
                print(f"No record with the filmID {idInput} exists!")
            else:
                for aFilm in row:
                    print(aFilm)
        
        elif field in ["title", "rating"]:
            strInput = input(f"Enter the value for the field {field}: ")
            print("")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} LIKE '%{strInput}%'")

            rows = dbCursor.fetchall()
            if not rows:
                print(f"No record with the field {field} matches {strInput}")
            else:
                for records in rows:
                    print(records)

        elif field == "genre":
            genreAmount = int(input("How many genre's would you like to search for?: "))
            print("")
            # this code was scrapped to limit the amount of genre's a user can search for
            # dbCursor.execute("SELECT COUNT(DISTINCT genre) FROM tblFilms")
            # tblGenreAmount = dbCursor.fetchone()[0]
            
            # if genreAmount > tblGenreAmount:
                # print("You have entered more genre amounts than what the table contains")
            
            if genreAmount > 5:
                print("You cannot search for more than 5 genres!")
            else:
                counter = 0
                genreInput = []
                while counter < genreAmount:
                    gInput = input("Enter the genre: ")
                    genreInput.append(gInput)
                    counter += 1
                print("")

                match genreAmount:
                    case 1:
                        dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genreInput[0]}'")
                        genreTypes = dbCursor.fetchall()
                        for gType in genreTypes:
                            print(gType)
                    case 2:
                        dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genreInput[0]}' OR genre = '{genreInput[1]}'")
                        genreTypes = dbCursor.fetchall()
                        for gType in genreTypes:
                            print(gType)
                    case 3:
                        dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genreInput[0]}' OR genre = '{genreInput[1]}' OR genre = '{genreInput[2]}'")
                        genreTypes = dbCursor.fetchall()
                        for gType in genreTypes:
                            print(gType)
                    case 4:
                        dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genreInput[0]}' OR genre = '{genreInput[1]}' OR genre = '{genreInput[2]}' OR genre = '{genreInput[3]}'")
                        genreTypes = dbCursor.fetchall()
                        for gType in genreTypes:
                            print(gType)
                    case 5:
                        dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genreInput[0]}' OR genre = '{genreInput[1]}' OR genre = '{genreInput[2]}' OR genre = '{genreInput[3]}' OR genre = '{genreInput[4]}'")
                        genreTypes = dbCursor.fetchall()
                        for gType in genreTypes:
                            print(gType)


    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
        print("DB operation performed")
        print("")

if __name__ == "__main__":
    search_film()
