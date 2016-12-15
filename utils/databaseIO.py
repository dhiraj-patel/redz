import sqlite3

def addData(u, eN, eT, eC, eV, eA, fN, fA, fT, fP):
	db = sqlite3.connect('data/data.db')
	c = db.cursor()
	c.execute("INSERT INTO '%s' VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(u,eN,eT,eC,eV,eA,fN,fA,fT,fP))
	db.commit()
	db.close()

