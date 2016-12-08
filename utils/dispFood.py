import urllib2, json

#seachFood(lat, long, rad, maxprice, )
#Params:
# lat - lattitude
# long - longitude
# rad - radius
# maxprice - price (0-4) 0 is most affordable
#Returns: list of places
#What it does: Searches events based on zip code, distance from house, and date
def searchFood(lat, long, rad, maxprice):
    q = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    q+="key=AIzaSyADc7Kdirb61v6g5LBZdisoLLeG3q_j03g"
    q+="&location="+str(lat)+","+str(long)
    q+="&radius="+str(rad)
    q+="&maxprice="+str(maxprice)
    q+="&type=restruant"
    u = urllib2.urlopen(q)
    response = u.read()
    data = json.loads( response )
    print data["results"][0]
    return data

#nextEvent(events,budget)
#Params:
# events - list of events
# budget - int budget in dollars
#Returns: api url to next event
#What it does: removes the first event from the list and checks the price, if
#it is below the cost it returns the event, if not it recursively calls itself
'''def nextEvent(events,budget):
    q = events[0]
    events.remove(q)
    q+="?token=COVN2QEFIDLBA54TVAVS"
    q+="&expand=ticket_classes"
    u = urllib2.urlopen(q)
    response = u.read()
    data = json.loads( response )
    isfree = data['ticket_classes'][0]['free']
    if(isfree):
        return data['resource_uri']+"?token=COVN2QEFIDLBA54TVAVS&expand=ticket_classes"
    elif(data['ticket_classes'][0]['cost']['value']/100<budget):
        return data['resource_uri']+"?token=COVN2QEFIDLBA54TVAVS&expand=ticket_classes"
    else:
        return nextEvent(events,budget)'''


searchFood(40.6653873,-73.9861546,1000,4)
