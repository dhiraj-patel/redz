import urllib2, json

#seachEvents(zip, range, year, month, day, hour, minute)
#Params:
# zip - zip code
# range - distance
# year, month, day, hour, minute - date
#Returns: list of api urls to events sorted by date
#What it does: Searches events based on zip code, distance from house, and date
def searchEvents(zip, range, year, month, day, hour, minute):
    q = "https://www.eventbriteapi.com/v3/events/search/?token=COVN2QEFIDLBA54TVAVS"
    q+="&sort_by=date"
    q+="&location.address="+str(zip)
    q+="&location.within="+str(range)+"mi"
    q+="&start_date.range_start=%d-%d-%dT%d:%d:00"%(year, month, day, hour, minute)
    u = urllib2.urlopen(q)
    response = u.read()
    data = json.loads( response )
    events = data["events"]
    ret = []
    i = 0
    while i < len(events):
        ret.append(events[i]['resource_uri'])
        i+=1
    return ret

#seachEvents(zip, range, year, month, day, hour, minute)
#Params:
# events - list of events
# budget - int budget in dollars
#Returns: api url to next event
#What it does: removes the first event from the list and checks the price, if
#it is below the cost it returns the event, if not it recursively calls itself
def nextEvent(events,budget):
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
        return nextEvent(events,budget)

#dispEvent(event)
#Params:
# event - event url
#Returns: dictionary with all of the data for the event
#What it does: grabs data from api
def dispEventResults(event):
    u = urllib2.urlopen(event+"&expand=venue,logo_id")
    response = u.read()
    data = json.loads( response )
    d = {}
    d['name']=data['name']['text']
    d['description']=data['description']['text']
    d['time']=data['start']['local']
    d['place']=data['venue']['name']
    d['address']=data['venue']['address']['localized_address_display']
    d['logo']=data['logo']['url']
    d['url']=data['url']
    return d


if __name__ == "__main__":
    events = searchEvents(11215, 20, 2016, 12, 15, 12, 30)
    print dispEventResults(nextEvent(events, 100))
                          
