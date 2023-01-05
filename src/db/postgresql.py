import psycopg2

from src.db.config import config


def connect():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
    except Exception as error:
        print(error)
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.commit()
            conn.close()
    return conn, cur


def close(conn, cur):
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.commit()
        conn.close()


def create_table(name):
    conn, cur = connect()
    query = ''' CREATE TABLE IF NOT EXISTS '''+name+'''(
                site_captures_id int,
                scheduled_works_id int,
                brand varchar(40) NOT NULL,
                name varchar NOT NULL,
                url varchar NOT NULL,
                price varchar(40) NOT NULL,
                sale varchar(30),
                created_at timestamp NOT NULL,
                updated_at timestamp NOT NULL)'''
    cur.execute(query)
    close(conn, cur)


def insert_values(table_name, values):
    conn, cur = connect()
    query = 'INSERT INTO '+table_name+' (brand, name, url, price, sale, created_at, updated_at, sku) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    for record in values:
        # print(record)
        cur.execute(query, record)
        print("PRODUCTS PERSISTED IN ["+table_name+"]...")
    close(conn, cur)


def drop_table():
    conn, cur = connect()
    cur.execute('DROP TABLE IF EXISTS employee')
    close(conn, cur)


def show_table():
    conn, cur = connect()
    cur.execute('SELECT * FROM employee')
    for record in cur.fetchall():
        print(record)
    close(conn, cur)


def update():
    conn, cur = connect()
    update_query = 'UPDATE employee SET salary = salary + (sarary * 0.5)'
    cur.execute(update_query)
    close(conn, cur)


def delete_by_name(name):
    conn, cur = connect()
    delete = 'DELETE FROM employee WHERE name = %s'
    cur.execute(delete, name)
    close(conn, cur)
