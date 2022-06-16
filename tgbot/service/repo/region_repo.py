from sqlalchemy import select

from tgbot.models.region import Region
from tgbot.service.repo.base_repo import BaseSQLAlchemyRepo


class RegionRepo(BaseSQLAlchemyRepo):
    model = Region

    async def get_regions(self) -> list[Region]:
        sql = select(self.model)
        request = await self._session.execute(sql)
        return request.scalars().all()
