from flask import Flask, render_template, request
from py2neo import Graph
import classes

# Setting up the app
app = Flask(__name__)

# Create a Neo4j driver and session
graph = Graph("bolt://localhost:7687", auth=("neo4j", "nanou9673"))

# Setting up a root : when going to / this is what happen
@app.route('/')
def hello_world():
    # Generate the tavern object
    tavern = classes.Tavern()

    # Prepare the query with $placeholders
    query = "CREATE (tavern:BUILDING {{name: '{tavern_name}', type: 'tavern'}}) -[:OWNED_BY]-> (owner:NPC {{name: '{npc_name}', gender: '{npc_gender}' }})".format(tavern_name=tavern.name, npc_name=tavern.owner['name'], npc_gender=tavern.owner['gender'])

    graph.run(query)

    return render_template('index.html', tavern=tavern)

@app.route('/npc/<npc_name>')
def npc_page(npc_name):
    npc = classes.Npc(npc_name, request.args.get('npc_gender'))
    return render_template('npc.html', npc = npc)