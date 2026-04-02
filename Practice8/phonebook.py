from config import load_config
import psycopg2

def get_pattern(pattern):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_pattern(%s)", (pattern,))
            results = cur.fetchall()
            for row in results:
                print(row)

def query_pagination(page_number, page_size):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM query_pagination(%s,%s)", (page_number, page_size))
            results = cur.fetchall()
            for row in results:
                print(row)

def insert_name_phone(name, phone):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_name_phone(%s,%s)", (name, phone))
        conn.commit()

def insert_many(names, phones):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_many(%s,%s)", (names, phones))
        conn.commit()

def delete_by(name, phone):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_by(%s,%s)", (name, phone))
        conn.commit()

if __name__ == "__main__":
    print("get_pattern")
    get_pattern('Ai')

    print("query_pagination")
    query_pagination(1, 3)

    print("insert_name_phone")
    insert_name_phone('Temirlan', '77011112233')

    print("insert_many")
    insert_many(['Dias', 'Nurbol', 'Sanzhar'], ['77001111111', '77002222222', 'abc123'])

    print("delete_by")
    delete_by('Temirlan', None)