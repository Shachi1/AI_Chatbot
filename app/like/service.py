
from prisma import Prisma
from app.core.base_service import BaseService


db = Prisma(http={
    'timeout': None,
},)

include = {
    'User': True,
}

order = {
    'id': 'asc',
}


class LikeService(BaseService):
    def __init__(self):
        super().__init__(db.like)

    async def add(self, payload):
        try:
            await db.connect()

            response = await super().create({
                'postId': payload['postId'],
                'userId': payload['userId'],

            })

            return {'success': True, 'data': response}

        except Exception as e:

            return {'success': False, 'data': e.args[0]}

        finally:
            await db.disconnect()

    async def remove(self, id):
        try:
            await db.connect()

            response = await super().delete({
                'id': int(id)
            })

            return {'success': True, 'data': response}

        except Exception as e:

            return {'success': False, 'data': e.args[0]}

        finally:
            await db.disconnect()

    async def getAll(self, postId):

        try:
            await db.connect()

            likes = await super().read({'postId': postId}, None, order)

            return {'success': True, 'data': likes}

        except Exception as e:

            return {'success': False, 'data': e.args[0]}
        finally:
            await db.disconnect()
