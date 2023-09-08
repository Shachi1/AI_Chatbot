import json


class BaseService:
    def __init__(self, db):
        self.db = db

    async def create(self, data):
        print(data)
        result = await self.db.create(data)
        print(result)
        return dict(result)

    async def read(self, where=None, include=None, order=None, limit=None, page=None):

        results = await self.db.find_many(where=where,  include=include, order=order, take=limit, skip=(page-1)*limit if (page and limit) else None)

        new = []
        for result in results:
            new.append(json.loads(result.json()))

        return new

    async def update(self, where, data):
        result = await self.db.update(where=where, data=data)
        return dict(result)

    async def delete(self, where):
        result = await self.db.delete(where=where)
        return dict(result)
