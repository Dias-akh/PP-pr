from config import load_config
import psycopg2
import json
import csv

# PRACTICE 8 — Base functions

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
def get_all():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM contacts")
            for row in cur.fetchall():
                print(row)

# 3.4 — New Stored Procedures

def add_phone(contact_name, phone, phone_type):
    #add a new phone number to an existing contact
    # The phone is inserted into the phones table linked by contact_id
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("CALL add_phone(%s,%s,%s)", (contact_name, phone, phone_type))
        conn.commit()

def move_to_group(contact_name, group_name):
    #assign a contact to a group
    # Updates group_id in the contacts table
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("CALL move_to_group(%s,%s)", (contact_name, group_name))
        conn.commit()

def search_contacts(query):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts(%s)", (query,))
            results = cur.fetchall()
            for row in results:
                print(row)

# 3.2 — Advanced Console Search & Filter

def filter_by_group(group_name):
    #Filter contacts by group name (Family, Work, Friend, Other)
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.name, c.email, c.birthday
                FROM contacts c
                JOIN groups g ON g.id = c.group_id
                WHERE g.name = %s
            """, (group_name,))
            for row in cur.fetchall():
                print(row)

def search_by_email(query):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT name, email FROM contacts
                WHERE email ILIKE %s
            """, (f'%{query}%',))
            for row in cur.fetchall():
                print(row)

def get_all_sorted(sort_by='name'):
     #Sort contacts by name or birthday
    allowed = ['name', 'birthday']
    if sort_by not in allowed:
        sort_by = 'name'
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT name, email, birthday FROM contacts ORDER BY {sort_by}")
            for row in cur.fetchall():
                print(row)

def paginated_navigation(page_size=3):
    page = 1
    while True:
        print(f"\n--- Page {page} ---")
        query_pagination(page, page_size)
        cmd = input("next / prev / quit: ").strip()
        if cmd == 'next':
            page += 1
        elif cmd == 'prev' and page > 1:
            page -= 1
        elif cmd == 'quit':
            break

# 3.3 — Import / Export

def export_to_json(filename='contacts.json'):
    #Export all contacts to a JSON file
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.name, c.email, c.birthday::text, g.name,
                       array_agg(p.phone) as phones
                FROM contacts c
                LEFT JOIN groups g ON g.id = c.group_id
                LEFT JOIN phones p ON p.contact_id = c.id
                GROUP BY c.name, c.email, c.birthday, g.name
            """)
            rows = cur.fetchall()
            data = [
                {"name": r[0], "email": r[1], "birthday": r[2],
                 "group": r[3], "phones": r[4]}
                for r in rows
            ]
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Exported to {filename}")

def import_from_json(filename='contacts.json'):
    #Import contacts from a JSON file
    config = load_config()
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            for contact in data:
                cur.execute("SELECT id FROM contacts WHERE name=%s", (contact['name'],))
                existing = cur.fetchone()
                if existing:
                    choice = input(f"{contact['name']} already exists. skip/overwrite: ")
                    if choice == 'skip':
                        continue
                    cur.execute("UPDATE contacts SET email=%s, birthday=%s WHERE name=%s",
                                (contact.get('email'), contact.get('birthday'), contact['name']))
                else:
                    cur.execute("INSERT INTO contacts(name, email, birthday) VALUES(%s,%s,%s)",
                                (contact['name'], contact.get('email'), contact.get('birthday')))
        conn.commit()
    print("Import ended")

def insert_csv(filename='phonebook.csv'):
    config = load_config()
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute("""
                    INSERT INTO contacts(name, phone, email, birthday)
                    VALUES(%s, %s, %s, %s)
                    ON CONFLICT DO NOTHING
                    RETURNING id
                    """, (row['name'], row['phone'], row.get('email'), row.get('birthday')))
                    
                    result = cur.fetchone()
                    if result:
                        contact_id = result[0]
                        cur.execute("""
                        INSERT INTO phones(contact_id, phone, type)
                        VALUES(%s, %s, %s)
                        """, (contact_id, row['phone'], row.get('type', 'mobile')))
                        
                        if row.get('group'):
                            cur.execute("""
                                INSERT INTO groups(name) VALUES(%s)
                                ON CONFLICT DO NOTHING
                                """, (row['group'],))
                            cur.execute("""
                                UPDATE contacts SET group_id = (
                                SELECT id FROM groups WHERE name = %s
                                ) WHERE id = %s
                                """, (row['group'], contact_id))
        conn.commit()
    print("CSV import ended")

# Console Interface 
if __name__ == "__main__":
    while True:
        print("\n=== PhoneBook ===")
        print("1. Search by pattern")
        print("2. Filter by group")
        print("3. Search by email")
        print("4. Sort")
        print("5. Pagination")
        print("6. Add contact")
        print("7. Add phone")
        print("8. Move to the group")
        print("9. Search (name + email + phone)")
        print("10. Export to JSON")
        print("11. Import from JSON")
        print("12. Show all contacts")
        print("13. Import from CSV")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == '1':
            pattern = input("Pattern: ")
            get_pattern(pattern)
        elif choice == '2':
            group = input("Group (Family/Work/Friend/Other): ")
            filter_by_group(group)
        elif choice == '3':
            email = input("Email: ")
            search_by_email(email)
        elif choice == '4':
            sort = input("Sort by (name/birthday): ")
            get_all_sorted(sort)
        elif choice == '5':
            paginated_navigation()
        elif choice == '6':
            name = input("Name: ")
            phone = input("Phone: ")
            insert_name_phone(name, phone)
        elif choice == '7':
            name = input("Contanct name: ")
            phone = input("Phone: ")
            ptype = input("Type (home/work/mobile): ")
            add_phone(name, phone, ptype)
        elif choice == '8':
            name = input("Contanct name: ")
            group = input("Group: ")
            move_to_group(name, group)
        elif choice == '9':
            query = input("Search: ")
            search_contacts(query)
        elif choice == '10':
            export_to_json()
        elif choice == '11':
            import_from_json()
        elif choice == '12':
            get_all()
        elif choice == '13':
            insert_csv()
        elif choice == '0':
            break