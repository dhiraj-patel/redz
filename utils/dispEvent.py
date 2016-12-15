import urllib2, json

#seachEvents(zip, range, year, month, day, hour, minute)
#Params:
# zip - zip code
# range - distance
# year, month, day, hour, minute - date
#Returns: list of api urls to events sorted by date
#What it does: Searches events based on zip code, distance from house, and date
def searchEvents(zip, range, year, month, day, hour, minute):
    instream = open('keys.csv', 'r') 
    content = instream.readlines() 
    instream.close()
    q = "https://www.eventbriteapi.com/v3/events/search/?token="
    q+=content[0][:-1]
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

#nextEvent(events,budget)
#Params:
# events - list of events
# budget - int budget in dollars
#Returns: api url to next event
#What it does: removes the first event from the list and checks the price, if
#it is below the cost it returns the event, if not it recursively calls itself
def nextEvent(events,budget):
    instream = open('keys.csv', 'r') 
    content = instream.readlines() 
    instream.close()
    q = events[0]
    events.remove(q)
    q+="?token="+content[0][:-1]
    q+="&expand=ticket_classes"
    u = urllib2.urlopen(q)
    response = u.read()
    data = json.loads( response )
    isfree = data['ticket_classes'][0]['free']
    if(isfree):#free event
        return data['resource_uri']+"?token=COVN2QEFIDLBA54TVAVS&expand=ticket_classes"
    elif 'cost' in data['ticket_classes'][0].keys():#paid event
        if data['ticket_classes'][0]['cost']['value']/100 < budget:
            return data['resource_uri']+"?token=COVN2QEFIDLBA54TVAVS&expand=ticket_classes"
        else:
            return nextEvent(events,budget)
    else:#must be pay what you wish
        return data['resource_uri']+"?token=COVN2QEFIDLBA54TVAVS&expand=ticket_classes"

#dispEvent(event)
#Params:
# event - event url
#Returns: dictionary with all of the data for the event
#What it does: grabs data from api
def dispEventResults(event):
    u = urllib2.urlopen(event+"&expand=venue,logo_id,ticket_classes")
    response = u.read()
    data = json.loads( response )
    d = {}
    d['name']=data['name']['text']
    d['description']=data['description']['text']
    d['time']=data['start']['local']
    d['place']=data['venue']['name']
    d['address']=data['venue']['address']['localized_address_display']
    d['lat']=data['venue']['latitude']
    d['long']=data['venue']['longitude']
    isfree = data['ticket_classes'][0]['free']
    if(isfree):#free event
        d['cost']=0
    elif 'cost' in data['ticket_classes'][0].keys():#paid event
        d['cost']=data['ticket_classes'][0]['cost']['value']/100
    else:#must be pay what you wish
        d['cost']=0
    if data['logo'] != None:
        d['logo']=data['logo']['url']
    else:
        d['logo']='http://bdamar.com/adminbdamar.com/edu/coaching/upload/3011758078676434.png'
    d['url']=data['url']
    return d


if __name__ == "__main__":
    events = searchEvents(11215, 20, 2016, 12, 15, 12, 30)
    print dispEventResults(nextEvent(events, 100))
                          
