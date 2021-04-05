import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('drop table if exists counts')

cur.execute('''
            create table counts (email text, count integer)''')

fname = input('Enter file name:')
if(len(fname) < 1):
    fname = 'mbox-short.txt'

fhand = open(fname)

for line in fhand:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]

    cur.execute('select count from counts where email = ?', (email,))
    row = cur.fetchone()

    if row is None:
        cur.execute('insert into counts(email, count) values(?, 1)', (email,))
    else:
        cur.execute(
            'update counts set count = count + 1 where email = ?', (email,))

    conn.commit()

sqlstr = 'select email, count from counts order by count desc limit 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
