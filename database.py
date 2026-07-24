import psycopg2
from models import Product
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
        name VARCHAR(50),
        amount INTEGER,
        count INTEGER)''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS tracker(
        product_id INTEGER,
        type VARCHAR(50),
        count INTEGER)''')
    
def add_product_base(name, amount, count):
    cur.execute('''INSERT INTO product(name, amount, count) VALUES (%s,%s,%s)''', (name, amount, count) )
    cur.execute('''SELECT * FROM product''')
    for row in cur:
        products = Product(
            row[0],
            row[1],
            row[2],
            row[3]
        )
    return products

def find_by_id(product_id):
    cur.execute('''SELECT * FROM product WHERE product_id = %s''', (product_id,))
    for row in cur:
        products = Product(
            row[0],
            row[1],
            row[2],
            row[3]
        )
    return products            

def find_by_name(product_name):
    cur.execute('''SELECT * FROM product WHERE LOWER(name) = LOWER(%s)''', (product_name,))
    for row in cur:
        products = Product(
            row[0],
            row[1],
            row[2],
            row[3]
        )
    return products            
