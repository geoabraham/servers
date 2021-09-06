# coding=utf-8
from flask import Flask, jsonify, request
from entities.base_entity import Session, engine, Base
from entities.server import Server, ServerSchema

# creating the Flask application
app = Flask(__name__)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route("/servers")
def get_servers():
    # fetching from the database
    session = Session()
    server_objects = session.query(Server).all()
    
    # transforming into JSON-serializable objects
    schema = ServerSchema(many=True)
    servers = schema.dump(server_objects)
    
    # serializing as JSON
    session.close()
    return jsonify(servers)


@app.route("/servers", methods=["POST"])
def add_server():
    # mount server object
    posted_server = ServerSchema(only=("customer_id", "hostname", "os", "ram", "cpu")).load(request.get_json())
    server = Server(**posted_server, created_by="HTTP post request")
    
    # persist server
    session = Session()
    session.add(server)
    session.commit()
    
    # return created server
    new_server = ServerSchema().dump(server)
    session.close()
    
    return jsonify(new_server), 201
