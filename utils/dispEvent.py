#from flask import Flask, render_template
import urllib2, json

#app = Flask(__name__)


#@app.route("/")
def root():
    u = urllib2.urlopen("https://www.eventbriteapi.com/v3/events/search/?token=COVN2QEFIDLBA54TVAVS")
    response = u.read()
    data = json.loads( response )
    print data

if __name__ == "__main__":
    root()
#    app.debug = True
#    app.run()
                          
