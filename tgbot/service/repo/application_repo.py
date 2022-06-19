import datetime

from sqlalchemy import insert

from tgbot.models import Application
from tgbot.service.repo.base_repo import BaseSQLAlchemyRepo


class ApplicationRepo(BaseSQLAlchemyRepo):
    model = Application

    async def new_application(self, name: str, surname: str, age: int, email: str, region: str, phone_number: str):
        sql = insert(self.model).values(
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            name=name,
            surname=surname,
            age=age,
            email=email,
            region=region,
            phone_number=phone_number
        )
        await self._session.execute(sql)
        await self._session.commit()
