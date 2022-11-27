from configparser import ConfigParser

import psycopg2

hostname = ''
database = ''
username = ''
pwd = ''
port_id = 5432


def config(filename='./venv/database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db


def connect():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        # conn = psycopg2.connect(
        #     host=hostname,
        #     dbname=database,
        #     user=username,
        #     password=pwd,
        #     port=port_id)
        cur = conn.cursor()
        # print(conn)
    except Exception as error:
        print(error)
    return conn, cur


def close(conn, cur):
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.commit()
        conn.close()


def create_table():
    conn, cur = connect()
    query = ''' CREATE TABLE IIF NOT EXISTS employee(
                id int PRIMARY KEY,
                name varchar(40) NOT NULL,
                salary int,
                dept_id varchar(30)) '''
    cur.execute(query)
    close(conn, cur)


def insert_values():
    conn, cur = connect()
    query = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %S)'
    values = [(1, 'James', 12000, 'D1'), (2, 'James', 12000, 'D2'), (3, 'James', 12000, 'D3'),
              (4, 'James', 12000, 'D4')]
    for record in values:
        cur.execute(query, record)

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
        # print(record[1],record[2]
        # print(record['name'],record['salary']
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
    conn.commit()
    close(conn, cur)
