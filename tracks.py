import xml.etree.ElementTree as ET
import sqlite3

conn=sqlite3.connect('trackdb.sqlite')# create database
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')
fname =input('Eneter  file Name: ')
if (len(fname)<1):fname='Library.xml'
    #ook up in libaray key
def lookup(d,key):
    found=False
    for child in d:
        if found: return child.text
        if child.tag=='key' and child.text==key:
            found=True
    return None

stuff=ET.parse(fname)#parse al string
all=stuff.findall('dict/dict/dict')#all the dict to get the key 
print('dict count: ',len(all))
for entry in all: # iterate though each key 
    if(lookup(entry,'Track ID')is None):continue
    
    
    
    track = lookup(entry, 'TRACK ID')
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')

    
    
    
    if name is None or artist is None or album is None:
        continue
    
    
    print (track, name, artist, genre, album)
    # or ignore artist name is unique if it already there dont insert
    cur.execute('''INSERT  OR IGNORE INTO ARTIST (name) VALUES (?)''',(artist,))
    
    cur.execute('SELECT ID IGNORE FROM ARTIST WHERE name=? ',(artist,))
    
    artist_id=cur.fetchone()[0]#fk for album
    
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]
 #update if doesnot have it
    cur.execute('''INSERT OR REPLACE INTO Track 
        (id, title, album_id, genre_id) 
        VALUES ( ?, ?, ?, ? )''', 
        (track, name, album_id, genre_id) )

    conn.commit()
    
    





