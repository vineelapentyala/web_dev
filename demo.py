import psycopg2

connection = psycopg2.connect("dbname=prof_dev")

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE test (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('''
    INSERT INTO test (id, completed) VALUES (1, true);
''')

connection.commit()

cursor.close()
connection.close()
