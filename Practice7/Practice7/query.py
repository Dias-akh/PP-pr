import psycopg2
from Practice7.Practice7.config import load_config

def get_all():
    config=load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM contacts;")
                rows=cur.fetchall()
                for row in rows:
                     print(row)
    except(psycopg2.DatabaseError,Exception) as error:
            print(error)

def by_name(name):
    config=load_config()
    sql="SELECT name,phone FROM contacts where name=%s;"
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql,(name,))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except(psycopg2.DatabaseError,Exception) as error:
            print(error)

def by_phone(phone):
    config=load_config()
    sql="SELECT name,phone FROM contacts where phone=%s;"
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql,(phone,))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except(psycopg2.DatabaseError,Exception) as error:
            print(error)

if __name__=="__main__":
    search=input("Search by(all, name, phone): ")
    if search=='all':
         get_all()
    elif search=='name':
         name=input("Input name: ")
         by_name(name)
    elif search=='phone':
         phone=input("Input phone: ")
         by_phone(phone)
    
    
   
