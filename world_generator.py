from flask import Flask, render_template, request
import classes

# Setting up the app
app = Flask(__name__)

# Disable template caching
app.debug = True

# Setting up a root : when going to / this is what happen
@app.route('/')
def hello_world():
    tavern = classes.Tavern()
    return render_template('index.html', tavern=tavern)

@app.route('/npc/<npc_name>')
def npc_page(npc_name):
    npc = classes.Npc(npc_name, request.args.get('npc_gender'))
    return render_template('npc.html', npc = npc)