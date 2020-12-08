import requests
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="haslo", port=3306, database="bitcoins")
connect = mydb.cursor()

sql = "CREATE TABLE summaries(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), difference FLOAT, bid FLOAT, ask FLOAT, volume FLOAT, creation_date TIMESTAMP)"
connect.execute(sql)

sql = "CREATE TABLE active(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
connect.execute(sql)

response = requests.get("https://api.bittrex.com/api/v1.1/public/getmarketsummaries")

summaries = response.json()['result']
differences = {}

for summary in summaries:
    sql = "INSERT INTO active (name) VALUES('{}')"
    sql = sql.format(summary['MarketName'])
    connect.execute(sql)

    if summary['High'] is not None and summary['Low'] is not None:
        high = float(summary['High'])
        low = float(summary['Low'])
        differences[summary['MarketName']] = high - low

differences = dict(sorted(differences.items(), key=lambda x: x[1], reverse=True)[:10])
top_10_names = list(differences.keys())
top_10_values = list(differences.values())

for i in range(len(top_10_names)):
    response = requests.get("https://api.bittrex.com/api/v1.1/public/getmarketsummary", params={"market": top_10_names[i]})
    sql = "INSERT INTO summaries (name, difference, bid, ask, volume, creation_date) VALUES('{}', {}, {}, {}, {}, '{}')"
    sql = sql.format(top_10_names[i], top_10_values[i], response.json()['result'][0]['Bid'], response.json()['result'][0]['Ask'],
                     response.json()['result'][0]['Volume'], response.json()['result'][0]['TimeStamp'])
    connect.execute(sql)

mydb.commit()
