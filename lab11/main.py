import time
import os

import keyboard

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

def _add_row(username, phone) -> str:
    with Database() as (conn, curr):
        curr.execute('''
            SELECT * FROM users WHERE username = %s
        ''', (username,))
        if curr.fetchone():
            curr.execute('''
                UPDATE users SET phone = %s WHERE username = %s
            ''', (phone, username))
            status = 'update'
        else:
            curr.execute('''
                INSERT INTO users (username, phone) VALUES (%s, %s)
            ''', (username, phone))
            status = 'insert'
        conn.commit()
        return status

def add_row():
    username = input('Enter username: ')
    phone = input('Enter phone: ')
    print('Row added succesfully!' if _add_row(username, phone) == 'insert' else 'Row updated succesfully!')
    
def add_rows():
    rows_raw = input('Enter rows username;phone, username2;phone2 ...: ')
    rows = [tuple(row.strip().split(';')) for row in rows_raw.split(',')]
    insert_count, update_count, incorrect_count = 0, 0, 0
    for row in rows:
        if row[1][:2] != '77':
            incorrect_count += 1
            continue
        status = _add_row(*row)
        if status == 'insert':
            insert_count += 1
        else:
            update_count += 1
    print(f'{insert_count} rows inserted, {update_count} rows updated, {incorrect_count} rows incorrect!')

def delete_row():
    username = input('Enter username: ')
    phone = input('Enter phone: ')
    with Database() as (conn, cur):
        cur.execute('''
            DELETE FROM users WHERE username = %s AND phone = %s
        ''', (username, phone))
    print('Row deleted successfully!')
    
def query_rows_pagination():
    with Database() as (conn, cur):
        cur.execute('SELECT COUNT(*) FROM users')
        count = cur.fetchone()[0]
        page = 0
        while True:
            os.system('cls')
            cur.execute('''
                SELECT * FROM users ORDER BY id LIMIT %s OFFSET %s
            ''', (10, page * 10))
            rows = cur.fetchall()
            print('ID\tUsername\tPhone')
            for row in rows:
                print(f'{row[0]}\t{row[1]}\t{row[2]}')
            print(f'Page {page + 1}/{count // 10 + 1}')
            print('Press q to quit, n for next page, p for previous page')
            key = keyboard.read_event(suppress=True).name
            if key == 'q':
                break
            elif key == 'n':
                page = (page + 1) % (count // 10 + 1)
            elif key == 'p':
                page = (page - 1) % (count // 10 + 1)
            time.sleep(0.1)    


if __name__ == '__main__':
    create_all()
    while True:
        operations = {
            '1': upload_data,
            '2': add_row,
            '3': add_rows,
            '4': delete_row,
            '5': query_rows_pagination
        }
        print('\n1. Upload data from CSV file\n' \
                '2. Add row\n' \
                '3. Add rows\n' \
                '4. Delete row\n' \
                '5. Query rows with pagination\n' \
                '6. Exit')
        choice = input('Enter choice: ')
        if choice == '6':
            break
        if choice in operations:
            operations[choice]()
        else:
            print('Invalid choice!')

    