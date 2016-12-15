import sqlite3

def addData(user, eN, eT, eC, eV, eA, fN, fA, fT, fP):
	db = sqlite3.connect('data/data.db')
	c = db.cursor()
	c.execute("INSERT INTO '%s' VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(user,eN,eT,eC,eV,eA,fN,fA,fT,fP))
	db.commit()
	db.close()

def getData(user):
	db = sqlite3.connect('data/data.db')
	c = db.cursor()
	retL = []
	s = c.execute("SELECT * FROM '%s'"%(user))
	for entry in s:
		retL.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7], entry[8]])
	return retL
