from config import load_config
import psycopg2

def create_tables():
    commands=(
        """ CREATE TABLE contacts(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL
        )
    """,
    )
    config=load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
        conn.commit()
    except(psycopg2.DatabaseError, Exception) as error:
        print(error)
if __name__=="__main__":
    create_tables()
