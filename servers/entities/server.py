import uuid

from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from servers.entities.base_entity import Base, BaseEntity


class Server(BaseEntity, Base):
    __tablename__ = "servers"
    customer_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    hostname = Column(String)
    os = Column(String)  # TODO: To Enum
    ram = Column(Integer)
    cpu = Column(String)  # TODO: To Enum

    def __init__(self, customer_id, hostname, os, ram, cpu):
        super().__init__()
        self.customer_id = customer_id
        self.hostname = hostname
        self.os = os
        self.ram = ram
        self.cpu = cpu


class ServerSchema(Schema):
    id = fields.UUID(required=True)
    customer_id = fields.UUID(required=True)
    hostname = fields.Str(required=True)
    os = fields.Str(required=True)
    ram = fields.Number(required=True)
    cpu = fields.Str(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
