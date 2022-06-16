from sqlalchemy import Column, String, BigInteger

from tgbot.models import BaseModel


class Region(BaseModel):
    __tablename__ = 'registration_region'

    id = Column(BigInteger, nullable=False, autoincrement=True, primary_key=True)
    region_name = Column(String(length=75), nullable=False)

    def __repr__(self):
        return f'{self.region_name}'
