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
    instream = open('keys.csv', 'r') 
    content = instream.readlines() 
    instream.close()
    q = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    q+="key="+content[1]
    q+="&location="+str(lat)+","+str(long)
    q+="&radius=2000"
    q+="&maxprice="+str(maxprice)
    #q+="&rankby=distance"
    q+="&type=restruant,food"
    u = urllib2.urlopen(q)
    response = u.read()
    data = json.loads( response )
    return data

#nextFood(events)
#Params:
# events - list of events
#Returns: api url to next event
#What it does: removes the first event from the list and checks the price, if
#it is below the cost it returns the event, if not it recursively calls itself
def nextFood(foods, i):
    instream = open('keys.csv', 'r') 
    content = instream.readlines() 
    instream.close()
    food = foods["results"][i];
    q = "https://maps.googleapis.com/maps/api/place/details/json?"
    q+="key="+content[1]
    q+= "&placeid="+str(food["place_id"])
    return q

#getPhoto(photo_reference)
#Params:
# photo_reference - photo_refenence to use in api request
#Returns: image
#What it does: Uses photo_reference to get image off of google places
def getPhoto(photo_reference):
    instream = open('keys.csv', 'r') 
    content = instream.readlines() 
    instream.close()
    q = "https://maps.googleapis.com/maps/api/place/photo?"
    q+="key="+content[1]
    q+="&photoreference="+photo_reference
    q+="&maxwidth=400"
    u = urllib2.urlopen(q)
    response = u.read()
    outstream = open('static/image.jpg', 'w') 
    outstream.write(response)
    outstream.close()
    return '../static/image.jpg'

#formatTime(time)
#Params:
# time - array returned by json from places apu
#Returns: nice string
#What it does: makes the string nicer
def formatTime(time):
    retstr = ''
    i = 0
    while i < len(time):
        retstr+=time[i]
        retstr+=", "
        i+=1
    return retstr

#dispFoodResults(event)
#Params:
# event - event url
#Returns: dictionary with all of the data for the food
#What it does: grabs data from api
def dispFoodResults(food):
    u = urllib2.urlopen(food)
    response = u.read()
    data = json.loads( response )
    d = {}
    d['name']=data['result']['name']
    d['address']=data['result']['formatted_address']
    if 'photos' in data['result'].keys():
        photo_reference =  data['result']['photos'][0]['photo_reference']
        d['logo']=getPhoto(photo_reference)
    else:
        d['logo']=None
    #d['logo']=data['result']['icon']
    d['url']=data['result']['url']
    if 'opening_hours' in data['result'].keys():
        d['time']=formatTime(data['result']['opening_hours']['weekday_text'])
    else:
        d['time']='no time listed'
    d['price']=data['result']['price_level']
    return d

if __name__ == "__main__":
    foods=searchFood(40.6653873,-73.9861546,10000,4)
    print foods
    i=0
    while i < len(foods['results']):
        print dispFoodResults(nextFood(foods, i))
        i+=1
