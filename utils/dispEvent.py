#from flask import Flask, render_template
import urllib2, json

#app = Flask(__name__)


#@app.route("/")
def root():
    q = "https://www.eventbriteapi.com/v3/events/search/?token=COVN2QEFIDLBA54TVAVS"
    q+="&location.address=11215"
    u = urllib2.urlopen(q)
    response = u.read()
    data = json.loads( response )
    events = data["events"]
    for event in events:
        print event
        print "That was an event\n\n\n\n"

if __name__ == "__main__":
    root()
#    app.debug = True
#    app.run()
                          
