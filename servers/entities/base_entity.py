import os
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, sessionmaker

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USERNAME = os.getenv("DB_USERNAME", "username")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "local-servers")


engine = create_engine(
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class BaseEntity(Base):
    __abstract__ = True
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)
    last_updated_by = Column(String)
