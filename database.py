import psycopg2
con = psycopg2.connect(
    host = 'localhost',
    database = 'sales-tracker',
    user = 'postgres',
    password = '1234',
    port = '5432'
)
con.autocommit = True
cur = con.cursor()
cur.execute('''CREATE EXTENSION IF NOT EXISTS pgcrypto''')

def create_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS product(
        product_id BIGSERIAL PRIMARY KEY,
        name VATCHAT(50),
        amount INTEGER,
        count INTEGER)''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS tracker(
        product_id INTEGER,
        type VARCHAR(50),
        count INTEGER)''')
    
def add_product_base(name, amount, count):
    cur.execute('''INSERT INTO product(name, amount, count) VALUES (%s,%s,%s)''', (name, amount, count))