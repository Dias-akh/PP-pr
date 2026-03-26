import psycopg2
from Practice7.Practice7.config import load_config

def update(name,what,new_value):
    config=load_config()
    if what=='name':
        sql="""UPDATE contacts
                SET name=%s
                WHERE name = %s"""
    elif what=='phone':
        sql="""UPDATE contacts
               SET phone = %s 
               WHERE name = %s"""
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql,(new_value,name))
            conn.commit()
    except(psycopg2.DatabaseError,Exception) as error:
        print(error)

if __name__=='__main__':
    name=input("Whom values you want to change: ")
    what=input("What to change(name or phone): ")
    new_value=input("New value: ")
    update(name,what,new_value)
        