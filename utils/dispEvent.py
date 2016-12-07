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
        return data['resource_uri']
    elif(data['ticket_classes'][0]['cost']['value']/100<budget):
        return data['resource_uri']
    else:
        return nextEvent(events,budget)
    
if __name__ == "__main__":
    events = searchEvents(11215, 20, 2016, 12, 15, 12, 30)
    print nextEvent(events, 100)
    print nextEvent(events, 100)
    print nextEvent(events, 100)
                          
