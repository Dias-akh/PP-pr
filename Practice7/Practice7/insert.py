import psycopg2
from Practice7.Practice7.config import load_config
import csv

def insert(name,phone):
    config=load_config()
    sql="""INSERT INTO contacts(name,phone) VALUES(%s,%s) RETURNING id;"""
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql,(name,phone))
        conn.commit()
    except(psycopg2.DatabaseError,Exception) as error:
        print(error)


def insert_csv(filename='phonebook.csv'):
    config=load_config()
    sql="""INSERT INTO contacts(name,phone) VALUES(%s,%s) RETURNING id; """

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                 with open(filename, 'r', encoding='utf-8') as f:
                     reader=csv.DictReader(f)
                     for row in reader:
                         cur.execute(sql, (row['name'], row['phone']))
        conn.commit()
    except(psycopg2.DatabaseError,Exception) as error:

        print(error)

if __name__=='__main__':
    what=input("How do you want to insert Keyboard or from CSV file)? ")
    if what=='Keyboard':
        name=input("Input name: ")
        phone=input("Input phone: ")
        insert(name,phone)
        print("Done")
    elif what=='CSV':
        insert_csv()
        print("Done")




