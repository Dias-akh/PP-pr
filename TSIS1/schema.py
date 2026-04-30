import psycopg2
from config import load_config

def create_schema():
    commands = [
        """
        CREATE TABLE IF NOT EXISTS groups (
            id   SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        )
        """,
        """
        INSERT INTO groups(name) VALUES ('Family'),('Work'),('Friend'),('Other')
        ON CONFLICT DO NOTHING
        """,
        """
        ALTER TABLE contacts
            ADD COLUMN IF NOT EXISTS email    VARCHAR(100),
            ADD COLUMN IF NOT EXISTS birthday DATE,
            ADD COLUMN IF NOT EXISTS group_id INTEGER REFERENCES groups(id)
        """,
        """
        CREATE TABLE IF NOT EXISTS phones (
            id         SERIAL PRIMARY KEY,
            contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
            phone      VARCHAR(20)  NOT NULL,
            type       VARCHAR(10)  CHECK (type IN ('home', 'work', 'mobile'))
        )
        """
    ]
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
            conn.commit()
            print("Schema created successfully")
    except Exception as error:
        print(error)

if __name__ == "__main__":
    create_schema()