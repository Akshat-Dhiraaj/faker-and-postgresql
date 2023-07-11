from faker import Faker
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(host="localhost", database="NewDB2", user="postgres", password="akshat", port = 5432)

# Creating cursor object for interacting with the database
cursor = conn.cursor()

# Creating the table
create_table_query = '''
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    gender VARCHAR(10),
    salary INTEGER
);
'''
cursor.execute(create_table_query)

# Generating 100 rows of data in the database
fake = Faker()
for _ in range(100):
    name = fake.name()
    age = fake.random_int(min=18, max=65)
    gender = fake.random_element(['Male', 'Female'])
    salary = fake.random_int(min=30000, max=100000)
    
    insert_query = f"INSERT INTO employees (name, age, gender, salary) VALUES ('{name}', {age}, '{gender}', {salary});"
    cursor.execute(insert_query)

# Commit
conn.commit()

# Close cursor and connection
cursor.close()
conn.close()
