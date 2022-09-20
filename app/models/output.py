from sqlalchemy import Column, String, Float, Integer
from db.base_class import Base


class Output(Base):
    id = Column(String, primary_key=True, index=True)
    executed_at = Column(Float, nullable=False)
    pred_class = Column(Integer, nullable=False)
