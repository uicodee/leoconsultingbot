from sqlalchemy import Column, BigInteger, String, Integer, func, DateTime

from tgbot.models import Base


class Application(Base):
    __tablename__ = 'registration_application'

    created_at = Column(DateTime(True), server_default=func.now(), nullable=True)
    updated_at = Column(DateTime(True), default=func.now(), onupdate=func.now(), server_default=func.now(), nullable=True)
    id = Column(BigInteger, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(length=50), nullable=False)
    surname = Column(String(length=100), nullable=False)
    age = Column(Integer(), nullable=False)
    region = Column(String(length=75), nullable=False)
    phone_number = Column(String(length=13), nullable=False)
    status = Column(String(length=20), nullable=False)
    source = Column(String(length=20), nullable=False)

    def __repr__(self):
        return f'{self.id} | ' \
               f'{self.name} | ' \
               f'{self.surname} | ' \
               f'{self.age} | ' \
               f'{self.email} | ' \
               f'{self.region} | ' \
               f'{self.phone_number}'
