import os
import mysql.connector as mysql
from reportlab.pdfgen import canvas

conn = mysql.connect(
    host='localhost',
    user='root',
    password='Young1995@',
    database='practice'
)
cursor = conn.cursor()

def dictfetchall(cursor):
    cols = [row[0] for row in cursor.description]
    return [
        dict(zip(cols, row)) for row in cursor.fetchall() 
    ]

# query = '''
# CREATE TABLE customers (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(150) NOT NULL,
#     email VARCHAR(100) NOT NULL,
#     phone VARCHAR(9) NOT NULL
# )
# '''
# cursor.execute(query)
# conn.commit()

# customers = [
#     ('Januario Cipriano', 'januario.cipriano@admin.com', '86954128'),
#     ('Reinata Cipriano', 'reinata.cipriano@admin.com', '87453214'),
#     ('Cipriano Cipriano', 'cipriano.cipriano@admin.com', '844532134'),
#     ('Angelina Cipriano', 'angelina.cipriano@admin.com', '864326540'),
#     ('Maico Cipriano', 'maico.cipriano@admin.com', '853412523')
# ]
# query = '''
# INSERT INTO customers (
#     name, email, phone
# ) VALUES (%s, %s, %s);
# '''
# cursor.executemany(query, customers)
# conn.commit()

query = 'SELECT * FROM customers';
cursor.execute(query)
results = dictfetchall(cursor) # .fetchall()
# print(results)

pdf = canvas.Canvas('mysql_python.pdf')
pdf.setFont('Helvetica-Bold', 16)
pdf.drawString(50, 750, 'Customer Report')

def set_spacing(text, spacing=40):
    return text + ' ' * spacing

pdf.setFont('Helvetica', 12)
y = 700
pdf.drawString(50, y, set_spacing('Name') + set_spacing('Email') + set_spacing('Phone'))
y -= 15
for row in results:
    pdf.drawString(50, y, set_spacing(row['name'], spacing=20) + set_spacing(row['email'], spacing=20) + set_spacing(row['phone'], spacing=20))
    pdf.drawString(50, y, '_' * 70)

    # pdf.drawString(50, y, 'Name: ' + row['name'])
    # pdf.drawString(50, y - 20, 'Email: ' + row['email'])
    # pdf.drawString(50, y - 40, 'Phone: ' + row['phone'])
    y -= 15

pdf.save()
os.system('start mysql_python.pdf')