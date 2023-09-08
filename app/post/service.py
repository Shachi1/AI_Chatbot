
from prisma import Prisma
from app.core.base_service import BaseService
from app.like.service import LikeService
from app.comment.service import CommentService

likeService = LikeService()
commentService = CommentService()


db = Prisma(http={
    'timeout': None,
},)

include = {
    'User': True,
}

order = {
    'id': 'asc',
}


class PostService(BaseService):
    def __init__(self):
        super().__init__(db.post)

    async def add(self, payload):
        try:
            await db.connect()

            print(type(payload))

            response = await super().create({
                'content': payload['content'],
                'userId': payload['userId'],

            })

            return {'success': True, 'data': response}

        except Exception as e:

            return {'success': False, 'data': e.args[0]}

        finally:
            await db.disconnect()

    async def edit(self, postId, payload):
        try:
            await db.connect()

            response = await super().update({
                'id': int(postId)
            }, {
                'content': payload['content'],
                'userId': payload['userId']

            })

            return {'success': True, 'data': response}

        except Exception as e:

            return {'success': False, 'data': e.args[0]}

        finally:
            await db.disconnect()

    async def getAll(self, queries):

        try:

            await db.connect()

            result = await super().read(None, include, order, int(queries['limit']), int(queries['page']))

            for datum in result:
                likes = await likeService.getAll(datum['id'])
                comments = await commentService.getAll(datum['id'])

                if (likes['success'] == True):
                    datum['likes'] = likes['data']

                if (comments['success'] == True):
                    datum['comments'] = comments['data']

            print(result)
            return {'success': True, 'data': result}

        except Exception as e:

            return {'success': False, 'data': e.args[0]}

        finally:
            await db.disconnect()

    async def remove(self, postId):
        try:
            await db.connect()

            response = await super().delete({
                'id': int(postId)
            })

            return {'success': True, 'data': response}

        except Exception as e:

            return {'success': False, 'data': e.args[0]}

        finally:
            await db.disconnect()
