from Practice7.Practice7.config import load_config
import psycopg2

def insert(name,phone):
    sql="""INSERT INTO contacts(name,phone) VALUES(%s,%s);"""
    config=load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql,(name,phone))
    conn.commit()
if __name__=='__main__':
    name=input()
    phone=input()
    insert(name,phone)