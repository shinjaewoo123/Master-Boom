# 8.1
test1 = 'this is a test of the emergency text system'

fout = open('test1', 'wt')
fout.write(test1)
fout.close()

# 8.2
fin = open('test1', 'rt')
test2 = fin.read()
fin.close()

print(test2)
print(test1 == test2)

# 8.3
books = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"'''

with open('test.csv', 'wt') as fout:
	fout.write(books)
	
# 8.4
import csv
with open('test.csv', 'rt') as fin:
	books = csv.DictReader(fin)
	for book in books:
		print(book)
		
# 8.5
books = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner 1960
Perdido Street Station,China Miville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''

with open('books.csv', 'wt') as fout:
	fout.write(books)
	
# 8.6
import sqlite3

db = sqlite3.connect('books.db')
curs = db.cursor()
curs.execute('''create table book (title text, aythor text, year int)''')
db.commit()

# 8.7
ins_str = 'insert into book values(?, ?, ?)'
with open('books.csv', 'rt') as fin:
	books = csv.DictReader(fin)
	for book in books:
		curs.execute(ins_str,(book['title'], book['author'], book['year']))
		
db.commit()

# 8.8
sql = 'select title from book order by title asc'
for row in db.execute(sql):
	print(row)

# 8.9
sql = 'select * from book order by year asc'
for row in db.execute(sql):
	print(row)
	

