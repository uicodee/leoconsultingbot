from sqlalchemy import Column, BigInteger, String, Integer

from tgbot.models import BaseModel


class Application(BaseModel):
    __tablename__ = 'registration_application'

    id = Column(BigInteger, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(length=50), nullable=False)
    surname = Column(String(length=100), nullable=False)
    age = Column(Integer(), nullable=False)
    email = Column(String(length=150), nullable=False)
    region = Column(String(length=75), nullable=False)
    phone_number = Column(String(length=13), nullable=False)

    def __repr__(self):
        return f'{self.id} | ' \
               f'{self.name} | ' \
               f'{self.surname} | ' \
               f'{self.age} | ' \
               f'{self.email} | ' \
               f'{self.region} | ' \
               f'{self.phone_number}'
