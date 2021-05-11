import sqlite3
from sqlite3 import Error


def sql_connection():
    # create a database connection to a SQLite database in memory
    conn = None
    try:
        conn = sqlite3.connect(":memory:")
        query = conn.cursor()
        print("Enter the name of a game to add to the db. \n")
        game = input()
        print("Enter the date the game came out in 'YYYY-MM-DD' format. \n")
        date = input()
        query.execute('''CREATE TABLE Gamestore
                     (date TEXT, trans TEXT, name TEXT, retailprice REAL, actualprice REAL)''')
        query.execute("INSERT INTO Gamestore VALUES ('" + date + "','BUY','" + game + "',59.99,32.24)")
        query.execute("INSERT INTO Gamestore VALUES ('2019-05-21','SELL','Mortal Kombat Gold',29.99,12.19)")
        query.execute('''CREATE TABLE Games
                             (releasedate TEXT, developer TEXT, name TEXT, retailprice REAL, actualprice REAL)''')
        query.execute("INSERT INTO Games VALUES ('" + date + "','Nintendo','" + game + "',59.99,32.24)")
        query.execute("INSERT INTO Games VALUES ('1999-09-09','Eurocom','Mortal Kombat Gold',29.99,12.19)")
        conn.commit()
        query.execute("SELECT * FROM Gamestore")
        # fetches all rows from the SELECT query result and
        # does a for loop through all the rows
        tablerows = query.fetchall()
        print("Gamestore Table")
        for tablerows in tablerows:
            print(tablerows)

        query.execute("SELECT * FROM Games")
        tablerows = query.fetchall()
        print("Games Table")
        for tablerows in tablerows:
            print(tablerows)
    except Error as e:
        print("The program has crashed,", "sqlgamestore.db", " has encountered an error ", e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    # main function below
    # r means raw string when passing variable to functions (justpythonthings)
    sql_connection()

