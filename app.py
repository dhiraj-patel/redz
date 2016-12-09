from flask import Flask, render_template, url_for, request, redirect, session
from utils import auth, dispEvent, dispFood

app = Flask(__name__)
app.secret_key = 'nine'

@app.route('/')
@app.route('/login')
def login():
    if 'user' in session:
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    if 'user' in session:
        mHome = "Welcome back " + session['user'] + "!"
        return render_template('home.html', messageHome = mHome)
    else:
        return redirect(url_for('login'))

@app.route("/authenticate", methods=['POST'])
def authenticate():
    u = request.form['username']
    p = request.form['password']
    a = request.form['action']
    data = auth.authenticate([u, p, a])
    if data[1]: #['message', boolean]
        session['user'] = u
        return redirect(url_for('home'))
    else:
        return render_template('login.html', messageLogin = data[0])

@app.route('/logout', methods=['POST'])
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('login'))


@app.route('/findEvents')
def find():
    return render_template('newEvent.html')
        

@app.route('/viewEvent', methods=["POST"])
def outputResults():
    formzip = request.form["Zip Code"]
    budgetrange = request.form["Budget"]
    distance = request.form["Radius"]
    time = request.form["Time"]
    date = request.form["Date"]
    
    timex = time.split(':')
    datex = date.split('-')

    year = int(datex[0])
    month = int(datex[1])
    day = int(datex[2])
    hour = int(timex[0])
    minute = int(timex[1])
    if year < 2015:
        return render_template('newEvent.html',errorMessage="Bad Request For Year")

    else: 
        events = dispEvent.searchEvents(formzip,distance,year,month,day,hour,minute)
        i = 0
        allEvents = []
        while i<5: 
            d=dispEvent.dispEventResults(dispEvent.nextEvent(events,budgetrange))
            allEvents.append(d)
            i+=1
        return render_template('listEvent.html', eventpar = allEvents, number = i)
    
@app.route('/viewFoods',methods=["POST"])
def foodResults():
    formlat = request.form['lat']
    formlong = request.form['long']
    formbudget = 4
    formRadius = 1609 #1 mile in meters

    i = 0
    allFoods = []
    while i<5:
        foodFound = dispFood.searchFood(formlat,formlong,formRadius,formbudget)
        f = dispFood.dispFoodResults(dispFood.nextFood(foodFound))
        print f 
        allFoods.append(f)
        i+=1
    return render_template('listFood.html', foodpar = allFoods, number=i)
    

if __name__ == "__main__":
    app.debug = True
    app.run()
