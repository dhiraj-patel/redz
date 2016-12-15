# redz -- Event Planner

### Installation Instructions:
#### Our project should not require the installation of additional modules, but incase of trouble these are the libraries we imported:
+ from flask: Flask, render_template, url_for, request, redirect, session
+ from Python: hashlib, sqlite3, urllib2, json

### What our site is supposed to do:
Our site is an itinerary planner designed to help people find ways to spend their time. The user logs in, then inputs information to search events by including cost, location, and time. This then leads the user to a list of events, one they choose one it redirects to a list of restruants nearby the event. The user chooses one, and then is brought to a summary of their trip. The users homepage displays their list of plans.

### How to use our site:
1. Register and log in, your home page should be empty as you have not scheduled any events
2. Click the Find Event button, this will lead you to a form
3. Fill out the data about where you want the event, and other details such as time, budget and date.\
4. Once you submit you will see a list of events. You can read the descriptions, or go to the links to explore the event. Once you have made a decision click find eateries underneath the desired event.
5. You will see a list of restruants. Click summary under the desired restruant and you will be redirected to the summery page.
6. Finally go back to the homepage and you should see your new event as well as past ones
7. Repeat to your heart's content