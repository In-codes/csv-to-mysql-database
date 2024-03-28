import csv

import mysql.connector

# Fetch the data from the csv file and put it to dict_list
csv_path = 'Your_csv_file_path'
final = []
with open(csv_path, 'r') as csv_reader:
    csv_reader = csv.reader(csv_reader)
    for num, value in enumerate(csv_reader):
        dict_list = dict()
        dict_list['id'] = int(num + 1)
        dict_list['name'] = value[0]
        dict_list['year'] = int(value[1])
        final.append(dict_list)

# The config file for connecting the python for database
mydatabase = mysql.connector.connect(
    username='your_username_in_database',
    password='database_username_password',
    host='localhost_or_your_host_address',
    database='database_name'
)

mycursor = mydatabase.cursor()

# To create your table in database
try:
    mycursor.execute('CREATE TABLE movie(id INT PRIMARY kEY, name VARCHAR(255), year INT)')
except mysql.connector.errors.ProgrammingError:
    ...

# Making queryset and push the csv file values to database
for item in final:
    sql = "INSERT INTO movie (id, name, year) VALUES (%s, %s, %s)"
    val = item['id'], item['name'], item['year']
    try:
        mycursor.execute(sql, val)
        print(f"Adding {item['name']} to database was successful!")
    except mysql.connector.errors.IntegrityError:
        pass
mydatabase.commit()

# The below code is for checking the table values

# mycursor.execute('SELECT * FROM your_table_name')
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

mydatabase.close()
