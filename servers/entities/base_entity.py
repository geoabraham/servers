from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import sessionmaker, declarative_base
import uuid

db_url = "localhost:5432"
db_name = "electric-servers"
db_user = "gabraham"
db_password = "#pSQL_00!"

engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_url}/{db_name}")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class BaseEntity(Base):
    __abstract__ = True
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)
    last_updated_by = Column(String)
