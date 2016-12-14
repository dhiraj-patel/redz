import sqlite3

def addEvent(u, eN, eT, eC, eV, eA, eL, fN, fA, fT, fP, fL):
	db = sqlite3.connect('data/data.db')
	c = db.cursor()
	c.execute("INSERT INTO '%s' VALUES ('%s','%s','%s', '%s','%s','%s','%s','%s','%s','%s','%s')"%(u, eN, eT, eC, eV, eA, eL, fN, fA, fT, fP, fL))
	db.commit()
	db.close()



