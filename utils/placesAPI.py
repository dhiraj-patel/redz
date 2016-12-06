import urllib2, json

def getInfo():
    u = urllib2.urlopen(https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyADc7Kdirb61v6g5LBZdisoLLeG3q_j03g)
    r = u.read()
    data = r.loads()
    print data

