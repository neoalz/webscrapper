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

    create_table = ''' CREATE TABLE IIF NOT EXISTS employee(
            id int PRIMARY KEY,
            name varchar(40) NOT NULL,
            salary int,
            dept_id varchar(30)) '''

    insert = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %S)'
    values = [(1, 'James', 12000, 'D1'),(2, 'James', 12000, 'D2'),(3, 'James', 12000, 'D3'),(4, 'James', 12000, 'D4')]
    query = create_table
    cur.execute(query)

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
