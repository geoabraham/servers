from sqlalchemy import Column, String, Integer
from .base_entity import BaseEntity, Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Server(BaseEntity, Base):
    __tablename__ = "servers"
    customer_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    hostname = Column(String)
    os = Column(String)  # TODO: To Enum
    ram = Column(Integer)
    cpu = Column(String)  # TODO: To Enum

    def __init__(self, customer_id, hostname, os, ram, cpu, created_by):
        BaseEntity.__init__(self, created_by)
        self.customer_id = customer_id
        self.hostname = hostname
        self.os = os
        self.ram = ram
        self.cpu = cpu
