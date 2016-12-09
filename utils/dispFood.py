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
    return data

#nextFood(events)
#Params:
# events - list of events
#Returns: api url to next event
#What it does: removes the first event from the list and checks the price, if
#it is below the cost it returns the event, if not it recursively calls itself
def nextFood(foods):
    food = foods["results"][0];
    q = "https://maps.googleapis.com/maps/api/place/details/json?"
    q+="key=AIzaSyADc7Kdirb61v6g5LBZdisoLLeG3q_j03g"
    q+= "&placeid="+str(food["place_id"])
    foods["results"].pop(0)
    return q

#dispFoodResults(event)
#Params:
# event - event url
#Returns: dictionary with all of the data for the food
#What it does: grabs data from api
def dispFoodResults(food):
    print food
    u = urllib2.urlopen(food)
    response = u.read()
    data = json.loads( response )
    d = {}
    d['name']=data['result']['name']
    d['address']=data['result']['formatted_address']
    d['logo']=data['result']['icon']
    d['url']=data['result']['url']
    return d

if __name__ == "__main__":
    foods=searchFood(40.6653873,-73.9861546,1000,4)
    print dispFoodResults(nextFood(foods))
