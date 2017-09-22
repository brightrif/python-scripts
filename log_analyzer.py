#!/usr/bin/env python

import MySQLdb
import csv

#connect
db = MySQLdb.connect(host="localhost",user="admin",passwd="password",db="logs")

cursor = db.cursor()

with open ('test.log') as readlog:
        cr = csv.reader(readlog, delimiter='\t')


        for row in cr:


# Execute SQL select statement
                qry = 'insert into logs (ip,date,time,method,url,referance,status,bytes,timetaken) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                cursor.execute(qry,row)
                db.commit()


# Close the connection
        db.close()
