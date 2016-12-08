from flask import Flask, render_template, url_for, request, redirect, session
from utils import auth, dispEvent

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
        placesData = placesAPI.getInfo()
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
        

@app.route('/viewEvent', methods=["GET"])
def outputResults():
    #zip = request.form["Zip Code"]
    #range = request.form["Budget"]
    events = dispEvent.searchEvents(10282,10, 2016, 12, 15, 12, 30)
    d=dispEvent.dispEventResults(dispEvent.nextEvent(events,100))
    return render_template('listEvent.html', eventpar = d)
    

if __name__ == "__main__":
    app.debug = True
    app.run()
