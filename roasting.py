import json
import sqlite3

conn=sqlite3.connect('roasterdb.sqlite')#connect can create more than one curson like file handle
cur=conn.cursor()
#id #name unique logica key
#start frest every time in case mistake for drop 
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
Drop TABLE IF EXISTS Course;

CREATE TABLE USER(
id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE 
);

CREATE TABLE Course(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE
);
CREATE TABLE Member(
 user_id INTEGER,
 course_id INTEGER,
 role      INTEGER,
 PRIMARY KEY (user_id,course_id))
''')
#pk composite promary key one particular combination on course and user
fname=input('Enter a file name :- ')
if len(fname)<1:
    fname='rost.json'

    #just an array
str_data =open(fname).read()
json_data=json.loads(str_data)#load json

for entry in json_data:
    
    name=entry[0];
    title=entry[1];
    role=entry[2]
    
    print((name,title,role))# two tuple
    
    #if iser coz error dont blowup if we inser name twice dont blow up ignore
    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES(?)''',(name,))
    
    #pk from user wher name = fetch one record more than one in sun[0]
    cur.execute('''SELECT id FROM User WHERE name =?''',(name,))
    user_id=cur.fetchone()[0]
    #course 
    cur.execute('''INSERT OR IGNORE INTO Course(title) VALUES(?)''',(title,))
    
    cur.execute('SELECT id FROM Course WHERE title=?',(title,))
    course_id=cur.fetchone()[0]
    # couurse id or user id comb is unique so if its dublicate update
    cur.execute('''INSERT OR REPLACE INTO Member
    (user_id,course_id,role) VALUES(?,?,?)''',
                (user_id,course_id,role))
    
    conn.commit()
    #orgram doesnot contine
    
    

