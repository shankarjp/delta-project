#Python-MySQL Interface

def AddUser(user_name, user_password):
    import mysql.connector

    con = mysql.connector.connect(
        host = "mysql",
        user = "root",
        password = "password",
        database = "UserInfo",
        auth_plugin = "mysql_native_password"
    )

    cursor = con.cursor()

    tables = cursor.execute("SHOW TABLES LIKE 'Users'").fetchall()
    if(tables == []):
        cursor.execute("CREATE TABLE Users (user_name VARCHAR(100), user_password VARCHAR(100))")
    cursor.execute("INSERT INTO Users (user_name, user_password) VALUES (%s, %s)", (user_name, user_password))

    con.commit()
    cursor.close()
    con.close()

def CheckUser(user_name, user_password):
    import mysql.connector

    con = mysql.connector.connect(
        host = "mysql",
        user = "root",
        password = "password",
        database = "UserInfo",
        auth_plugin = "mysql_native_password"
    )

    cursor = con.cursor()

    tables = cursor.execute("SHOW TABLES LIKE 'Users'").fetchall()
    if(tables == []):
        cursor.execute("CREATE TABLE Users (user_name VARCHAR(100), user_password VARCHAR(100))")
        return(False)
    else:
        user = cursor.execute("SELECT user_name FROM Users WHERE user_name = %s AND user_password = %s", (user_name, user_password))
        if(user == []):
            return(False)
        else:
            return(True)
    con.commit()
    cursor.close()
    con.close()
