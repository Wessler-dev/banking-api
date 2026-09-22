from sqlalchemy import Column, String, BIGINT, Float
from src.models.sqlite.settings.base import Base

class LegalEntityTable(Base):
    __tablename__ = "LegalEntity"

    id = Column(BIGINT, primary_key=True)
    revenue = Column(Float, nullable=False)
    age = Column(BIGINT,nullable=False)
    trade_name = Column(String(150), nullable=True)
    phone_number = Column(String(30), nullable=True)
    corporate_email = Column(String(150), nullable=True)
    category = Column(String(150), nullable=False)
    balance = Column(Float, nullable=False)

    def __repr__(self):
        return f"[name={self.trade_name}, email={self.corporate_email}, balance={self.balance}]"
