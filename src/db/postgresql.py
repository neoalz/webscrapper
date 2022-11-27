import psycopg2

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = 'admin'
port_id= 5432
conn = None
cur = None


try:
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)
    cur = conn.cursor()



except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

def create_table():
    create_table = ''' CREATE TABLE IIF NOT EXISTS employee(
                id int PRIMARY KEY,
                name varchar(40) NOT NULL,
                salary int,
                dept_id varchar(30)) '''
    cur.execute(create_table)
    conn.commit()

def insert_values():
    insert = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %S)'
    values = [(1, 'James', 12000, 'D1'), (2, 'James', 12000, 'D2'), (3, 'James', 12000, 'D3'), (4, 'James', 12000, 'D4')]
    for record in values:
        cur.execute(insert,record)

    conn.commit()

def drop_table():
    cur.execute('DROP TABLE IF EXISTS employee')
    conn.commit()
def show_table():
    cur.execute('SELECT * FROM employee')
    for record in cur.fetchall():
        print(record)
        #print(record[1],record[2]
        #print(record['name'],record['salary']

def update():
    update_query = 'UPDATE employee SET salary = salary + (sarary * 0.5)'
    cur.execute(update_query)

def delete_by_name(name):
    delete = 'DELETE FROM employee WHERE name = %s'
    cur.execute(delete, name)
    conn.commit()





