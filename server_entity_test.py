# TODO: Move this file to tests folder.
from entities.base_entity import Session, engine, Base
from entities.server import Server
import uuid
import os

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
servers = session.query(Server).all()

if len(servers) == 0:
    # create and persist dummy server
    py_server = Server(uuid.uuid4(), "localhost", "linux", 16, "intel", "test_script")

    session.add(py_server)
    session.commit()
    session.close()

    # reload servers
    servers = session.query(Server).all()

# show existing servers
print("### Servers:")
for server in servers:
    print(f"({server.id}) {server.hostname} - {server.os}")
