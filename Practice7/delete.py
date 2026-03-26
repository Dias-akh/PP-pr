import psycopg2
from config import load_config

def delete_name(name):
    config=load_config()
    sql="DELETE FROM contacts WHERE name=%s"
    deleted=0
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql,(name,))
                deleted=cur.rowcount
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return deleted

def delete_phone(phone):
    config=load_config()
    sql="DELETE FROM contacts WHERE phone=%s"
    deleted=0
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql,(phone,))
                deleted=cur.rowcount
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return deleted

if __name__ == '__main__':
    query=input("By what value you want to delete: ")
    if query=='name':
        name=input("Input name: ")
        deleted=delete_name(name)
        print(deleted)
    elif query=='phone':
        phone=input("Input phone: ")
        deleted=delete_phone(phone)
        print(deleted)

            
 
