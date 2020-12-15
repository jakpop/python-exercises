import random
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="", port=3306)
connect = mydb.cursor()


def createList(n):
    try:
        for i in range(n):
            database = randomDatabase()
            sql = randomSQL(database)
            connect.execute(sql)
        return True
    except:
        return False


def randomDatabase():
    return random.choice(['osoby', 'pracownicy', 'studenci', 'administracja'])


def randomSQL(database):
    return random.choice(['CREATE DATABASE ' + database, 'DROP DATABASE ' + database])


print(createList(4))
