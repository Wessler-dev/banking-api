from sqlalchemy import Column, String, BIGINT, Float
from src.models.settings.base import Base

class Individual(Base):
    __tablename__ = "individual"

    id = Column(BIGINT, primary_key=True)
    monthly_income = Column(Float, nullable=False)
    age = Column(BIGINT, nullable=False)
    full_name = Column(String(150), nullable= True)
    phone_number = Column(String,nullable=True)
    email = Column(String(150),nullable=True)
    category = Column(String(150), nullable=True)
    balance = Column(Float,nullable=False)

    def __repr__(self):
        return f"[name={self.full_name,},email={self.email}, catetory={self.category}]"
