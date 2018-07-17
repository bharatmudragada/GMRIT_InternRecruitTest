#finding links in html file
from bs4 import BeautifulSoup
import re
import MySQLdb
import hashlib
import uuid
import random
out = open("new.txt",'w')
html_page = open("Buckton_Castle.html")
soup = BeautifulSoup(html_page, "lxml")
for link in soup.findAll('a'):
	l = link.get('href')
	if l != None:
		print(l,file=out)
#Creating DB
db = MySQLdb.connect("localhost","root","root")
cursor = db.cursor()
database = "mydata"
cursor.execute("DROP DATABASE IF EXISTS "+ database)
sql = "CREATE DATABASE " + database
cursor.execute(sql)
sql = "USE " + database
cursor.execute(sql)
sql = "CREATE TABLE user (interestid VARCHAR(1000), interestname VARCHAR(20), userid VARCHAR(1000))"
cursor.execute(sql)
name = ["Projects", "Startups", "Travel", "Food", "Music", "Pets", "Relationships"]
for i in range(10):
	intname = random.choice(name)
	usrid = str(uuid.uuid4())
	intid = hashlib.md5(usrid.encode())
	sql = "INSERT INTO user(interestid, interestname, userid) VALUES (?,?,?)"
	cursor.execute(sql, (str(intname), str(usrid), str(intid))) 
db.close()
