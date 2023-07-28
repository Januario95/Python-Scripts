import os
import random
import itertools
from statistics import mean
from reportlab.pdfgen import canvas
from reportlab.lib.units import (
    cm, inch, mm, pica, toLength
)
from reportlab.rl_config import defaultPageSize
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.utils import ImageReader

filename = 'hello_world.pdf'

open_file = lambda: os.system('start hello_world.pdf')

# can = canvas.Canvas(filename)
# can.drawString(20, 400, 'Hello World!')
# can.showPage()
# can.save()
# os.system('start hello_world.pdf')

# print(cm)
# print(inch)
# print(mm)
# print(pica)

# can = canvas.Canvas(filename)
# can.drawString(2*cm, 20*cm, 'Hello World!')
# can.showPage()
# can.save()
# os.system('start hello_world.pdf')

# can = canvas.Canvas(filename)
# fonts = can.getAvailableFonts()

# # can.setFont(random.choice(fonts), 24)
# can.setFont(random.choice(fonts), 24)
# x = 30
# y = 750
# can.drawString(x, y, 'Hello')
# can.drawString(x, y - 30, 'World')

# can.setFont(random.choice(fonts), 16)
# can.drawString(x, y - 50, 'How are you?')
# can.showPage()
# can.save()
# os.system('start hello_world.pdf')

# WIDTH, HEIGHT = defaultPageSize

# can = canvas.Canvas(filename)
# can.drawString(WIDTH/4, HEIGHT-20, 
#                f'WIDTH:{WIDTH}     HEIGHT:{HEIGHT}')
# can.showPage()
# can.save()
# os.system('start hello_world.pdf')

# print(letter)
# print(A4)

# c = canvas.Canvas(filename, pagesize=letter)

width, height = A4
# c = canvas.Canvas(filename, pagesize=A4)
# c.drawString(50, height-50, 'Hello World!')

# x = 50
# y = height - 50
# c.line(x, y, x + 200, y)
# c.rect(50, height - 300, 200, 100)
# c.roundRect(50, height - 180, 300, 100, 10)
# c.circle(100, height - 130, 50)

# c.showPage()
# c.save()
# open_file()

# c = canvas.Canvas('shapes.pdf', pagesize=A4)
# c.drawString(30, height - 50, 'Line')

# x = 120
# y = height - 45
# c.line(x, y, x + 100, y)
# c.drawString(30, height - 100, 'Rectangle')
# c.rect(x, height - 120, 100, 50)
# c.drawString(30, height - 170, 'Circle')
# c.circle(170, height - 165, 20)
# c.drawString(30, height - 240, 'Ellipse')
# c.ellipse(x, y - 170, x + 100, y - 220)
# c.showPage()
# c.save()
# os.system('start shapes.pdf')

# c = canvas.Canvas('styles.pdf')
# c.setFillColorRGB(0, 0, 1)
# c.setStrokeColorRGB(0.7, 0, 0.7)
# c.setFont('Helvetica', 10)
# c.drawString(50, height - 50, 'Hello World!')
# c.setFont('Times-Roman', 20)
# c.drawString(130, height - 50, 'Hello World!')
# c.rect(50, height - 150, 50, 50, fill=True)

# text = c.beginText(50, height - 50)
# text.setFont('Times-Roman', 12)
# text.textLine('Hello World!')
# text.textLine('From ReportLab and Python!')
# text.textLines('Hello World!\nFrom ReportLab and Python!')

# c.drawText(text)

# c.showPage()
# c.save()
# os.system('start styles.pdf')

image = 'Creatsy_Bag.png'
# c = canvas.Canvas('images.pdf')
# # c.drawImage(image, 5, height - 500)

# c.drawImage(image, 5, height - 100, width=100, height=100)

# c.showPage()
# c.save()
# os.system('start images.pdf')

# c = canvas.Canvas('images.pdf', pagesize=A4)
# img = ImageReader(image)
# img_width, img_height = img.getSize()

# c.drawImage(img, 0, height - img_height)
# c.showPage()
# c.save()
# os.system('start images.pdf')

# c = canvas.Canvas('grids.pdf')
# xlist = [10, 60, 110, 160]
# ylist = [height - 10, height - 60,
#          height - 110, height - 160]
# c.grid(xlist, ylist)
# c.showPage()
# c.save()
# os.system('start grids.pdf')


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)


def export_to_pdf(data):
    c = canvas.Canvas("grid-students.pdf", pagesize=A4)
    w, h = A4
    max_rows_per_page = 45
    # Margin.
    x_offset = 50
    y_offset = 50
    # Space between rows.
    padding = 15

    xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]

    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))
        c.showPage()

    c.save()
    os.system('start grid-students.pdf')


data = [("NAME", "GR. 1", "GR. 2", "GR. 3", "AVG", "STATUS")]

for i in range(1, 101):
    exams = [random.randint(0, 10) for _ in range(3)]
    avg = round(mean(exams), 2)
    state = "Approved" if avg >= 4 else "Disapproved"
    data.append((f"Student {i}", *exams, avg, state))

export_to_pdf(data)
