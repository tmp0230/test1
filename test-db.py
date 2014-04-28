

#from xpcom import components

import sys

#print "hello world"

#print sys.path

import MySQLdb

def test1():
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='db_wp',port=3306)
        cur=conn.cursor()
        print "b4 db exe"
        cur.execute('select * from tb2_users')
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
      
# =================================================
   
def test2():
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306)
        cur=conn.cursor()
         
        cur.execute('create database if not exists python')
        conn.select_db('python')
        cur.execute('create table test(id int,info varchar(20))')
         
        value=[1,'hi rollen']
        cur.execute('insert into test values(%s,%s)',value)
         
        values=[]
        for i in range(20):
            values.append((i,'hi rollen'+str(i)))
             
        cur.executemany('insert into test values(%s,%s)',values)
     
        cur.execute('update test set info="I am rollen" where id=3')
     
        conn.commit()
        cur.close()
        conn.close()
     
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        
 
def test3():
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306)
        cur=conn.cursor()
         
        conn.select_db('python')
     
        count=cur.execute('select * from test')
        print 'there has %s rows record' % count
     
        result=cur.fetchone()
        print result
        print 'ID: %s info %s' % result
     
        results=cur.fetchmany(5)
        for r in results:
            print r
     
        print '=='*10
        cur.scroll(0,mode='absolute')
     
        results=cur.fetchall()
        for r in results:
            print r[1]
         
     
        conn.commit()
        cur.close()
        conn.close()
     
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])      
         
# --------------------------------------

 
        
test1()
#test2()
test3()


# ======================  test sqlite

import sqlite3

def test4():
    con = sqlite3.connect('c:/mydatabase.db3')
    cur = con.cursor()
    cur.execute('CREATE TABLE foo (o_id INTEGER PRIMARY KEY, fruit VARCHAR(20), veges VARCHAR(30))')
    con.commit()
    cur.execute('INSERT INTO foo (o_id, fruit, veges) VALUES(NULL, "apple", "broccoli")')
    con.commit()
    print cur.lastrowid
    
    cur.execute('SELECT * FROM foo')
    print cur.fetchall()
    
test4()
