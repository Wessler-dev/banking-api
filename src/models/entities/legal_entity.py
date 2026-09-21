from sqlalchemy import Column, String, BIGINT, Float
from src.models.settings.base import Base

class LegalEntity(Base):
    __tablename__ = "LegalEntity"

    id = Column(BIGINT, primary_key=True)
    revenue = Column(Float, nullable=False)
    age = Column(BIGINT,nullable=False)
    trade_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    corporate_email = Column(String, nullable=True)
    category = Column(String, nullable=False)
    balance = Column(Float, nullable=False)

    def __repr__(self):
        return f"[name={self.trade_name}, email={self.corporate_email}, balance={self.balance}]"
