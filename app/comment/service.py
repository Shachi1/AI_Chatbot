
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


class CommentService(BaseService):
    def __init__(self):
        super().__init__(db.comment)

    async def add(self, payload):
        try:
            await db.connect()
            print(type(payload))

            response = await super().create(payload)
            print(response)

            return {'success': True, 'data': response}

        except Exception as e:
            print('error:', e.args[0])
            return {'success': False, 'data': e.args[0]}

        finally:
            await db.disconnect()

    async def edit(self, commentId, payload):
        try:
            await db.connect()

            response = await super().update({
                'id': int(commentId)
            }, {
                'postId': payload['postId'],
                'userId': payload['userId'],
                'content': payload['content'],

            })

            return {'success': True, 'data': response}

        except Exception as e:

            return {'success': False, 'data': e.args[0]}

        finally:
            await db.disconnect()

    async def getAll(self, postId):

        try:
            await db.connect()

            likes = await super().read({'postId': postId}, include, order)

            return {'success': True, 'data': likes}

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
