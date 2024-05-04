from database import Database


def create_all():
    with Database() as (conn, cur):
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (  
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                phone VARCHAR(50) NOT NULL
            )
        ''')
        
def upload_data():
    file_path = input('Enter path to CSV file: ')
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n')
    data = [tuple(line.split(';')) for line in data]
    with Database() as (conn, cur):
        cur.executemany('''
            INSERT INTO users (username, phone) VALUES (%s, %s)
        ''', data)
    print('Data uploaded successfully!')
    
def add_row():
    username = input('Enter username: ')
    phone = input('Enter phone: ')
    with Database() as (conn, cur):
        cur.execute('''
            INSERT INTO users (username, phone) VALUES (%s, %s)
        ''', (username, phone))
    print('Row added successfully!')
    
def edit_row():
    username = input('Enter username: ')
    with Database() as (conn, cur):
        cur.execute('''
            SELECT * FROM users WHERE username = %s
        ''', (username,))
        row = cur.fetchone()
        if row is None:
            print('Row not found!')
            return
        which = input('Enter which field to edit (username/phone): ')
        if which == 'username':
            username = input('Enter new username: ')
            cur.execute('''
                UPDATE users SET username = %s WHERE username = %s
            ''', (username, row[1]))
            print('Row updated successfully!')
        elif which == 'phone':
            phone = input('Enter new phone: ')
            cur.execute('''
                UPDATE users SET phone = %s WHERE username = %s
            ''', (phone, row[1]))
            print('Row updated successfully!')
        else:
            print('Invalid field!')
            
def delete_row():
    username = input('Enter username: ')
    phone = input('Enter phone: ')
    with Database() as (conn, cur):
        cur.execute('''
            DELETE FROM users WHERE username = %s AND phone = %s
        ''', (username, phone))
    print('Row deleted successfully!')
    
def query_rows():
    query = dict(
        username = input('Enter username: '),
        phone = input('Enter phone: ')
    )
    if not query['username'] and not query['phone']:
        print('Empty query!')
        return
    
    sql_keys = [f'{key} ILIKE %s' for key, value in query.items() if value != '']
    values = [f'%{value}%' for key, value in query.items() if value != '']
    
    with Database() as (conn, cur):
        cur.execute(f'''
            SELECT * FROM users WHERE {' AND '.join(sql_keys)}
        ''', values)
        rows = cur.fetchall()
        
    if len(rows) == 0:
        print('No rows found!')
    else:
        print(f'{len(rows)} rows found:')  
        for row in rows:
            print('>', ' - '.join(row[1:]))

if __name__ == '__main__':
    create_all()
    while True:
        operations = {
            '1': upload_data,
            '2': add_row,
            '3': edit_row,
            '4': delete_row,
            '5': query_rows
        }
        print('\n1. Upload data from CSV file\n' \
                '2. Add row\n' \
                '3. Edit row\n' \
                '4. Delete row\n' \
                '5. Query rows\n' \
                '6. Exit')
        choice = input('Enter choice: ')
        if choice == '6':
            break
        if choice in operations:
            operations[choice]()
        else:
            print('Invalid choice!')

    