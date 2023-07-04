import sqlite3
conn=sqlite3.connect('emaildb.sqlite')#create data base
#make Connection
cur= conn.cursor()
#handle open ir and send sql command to sql

#drop the table if exist
cur.execute('DROP TABLE IF EXISTS Counts')
# longer trible quite
cur.execute('''CREATE TABLE  Counts(org TEXT , count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh=open(fname)

for line in fh:
    if not line.startswith('From: '):continue
    pieces=line.split()
    email=pieces[1]
    email=email.split('@')
    org=email[1]
    cur.execute('SELECT count FROM Counts WHERE org= ?',(org,))#openening recor set
    row=cur.fetchone()#grab that first one row is information on database
    if row is None:
        cur.execute('''INSERT INTO Counts (org,count) VALUES (?,1)''',(org,))
    else:
        cur.execute('Update  Counts SET count=count +1 where org= ?',(org,))
conn.commit()
    #coomit 
sqlstr='SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
cur.close()

