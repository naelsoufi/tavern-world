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

    # Prepare, launch and reset the query with $placeholders for the tavern generation
    query = "CREATE (tavern:BUILDING {{name: '{tavern_name}', type: 'tavern'}}) -[:OWNED_BY]-> (owner:NPC {{name: '{npc_name}', gender: '{npc_gender}' }}) RETURN id(tavern) AS tavern_id, id(owner) AS owner_id".format(tavern_name = tavern.name, npc_name = tavern.owner['name'], npc_gender = tavern.owner['gender'])
    result = graph.run(query)
    # Access the results since result is just a box with everything inside and we need to reach each piece individually
    records = result.data()

    if records:
        record = records[0]
        # Retrieve the id of the tavern and owner for future use
        tavern_id = record['tavern_id']
        owner_id = record['owner_id']  
    
    query = None

    # Create the relationship of ownership in the other direction (owner OWNS building)
    query = "MATCH (owner:NPC), (tavern:BUILDING) WHERE ID(tavern)={tavern_id} AND ID(owner)={owner_id} CREATE (owner) -[:OWNS]-> (tavern)".format(tavern_id = tavern_id, owner_id = owner_id)
    graph.run(query)
    query = None

    # Transfer the building and the owner's id in case user clicks on owner's name
    return render_template('index.html', tavern=tavern, owner_id=owner_id)

@app.route('/npc/<npc_name>')
def npc_page(npc_name):
    # Fetch the NPC based on the id
    query = "MATCH (npc:NPC) WHERE ID(npc)={npc_id} RETURN npc".format(npc_id=request.args.get('npc_id'))
    npc_records = graph.run(query)
    query = None
    
    # Extract data from the query. Here it's a dictionary and each row could contain one full node, hence the 'npc'
    npc_record = npc_records.data()
    npc_database_infos = npc_record[0]['npc']

    # Generate the NPC object with the infos we already have
    # Note that we will need at some point find a process to know if the npc is fully fledged or not
    # Could have a literal NPC level of rendering going from 0 to maybe 3
    npc = classes.Npc(npc_database_infos['name'], npc_database_infos['gender'])

    # Update the NPC in the database
    query = "MATCH (npc:NPC) WHERE ID(npc)={npc_id} SET npc.age = {npc_age}".format(npc_id=request.args.get('npc_id'), npc_age=npc.age)
    graph.run(query)
    query = None
    
    return render_template('npc.html', npc = npc)
    
if __name__ == '__main__':
    app.run(debug=True, port=8001)