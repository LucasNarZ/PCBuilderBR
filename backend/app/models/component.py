from datetime import datetime
from sqlalchemy import Column, DateTime, String, Float, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from app.database import Base

class Component(Base):
    __tablename__ = "components"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    part_type = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
    specs = Column(JSONB, nullable=False, default={})

    offers = relationship("ComponentOffer", back_populates="component", cascade="all, delete-orphan")


class ComponentOffer(Base):
    __tablename__ = "component_offers"

    id = Column(String, primary_key=True)
    component_id = Column(String, ForeignKey("components.id"), nullable=False)
    price = Column(Float, nullable=False)
    store = Column(String, nullable=False)
    url = Column(String, nullable=False)
    in_stock = Column(Boolean, default=True)
    last_updated = Column(DateTime, default=datetime.utcnow)

    component = relationship("Component", back_populates="offers")

