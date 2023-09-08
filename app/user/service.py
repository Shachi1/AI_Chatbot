
from prisma import Prisma
from app.utils import generate_hash, check_hash
from app.core.base_service import BaseService
from prisma import Prisma

from app.utils.auth import generate_token

db = Prisma(http={
    'timeout': None,
},)


class UserService(BaseService):
    def __init__(self):
        super().__init__(db.user)

    async def signup(self, payload):

        try:

            await db.connect()

            user = await super().read({'email': payload['email']})

            if (len(user) > 0):
                raise Exception(
                    {'name': 'forbidden', 'message': 'User already exists'})

            response = await super().create({
                'email': payload.get('email'),
                'password': generate_hash(payload.get('password')),
                'name': payload.get('name'),
            })

            return {'success': True, 'data': response}

        except Exception as e:

            return {'success': False, 'data': e.args[0]}

        finally:
            await db.disconnect()

    async def signin(self, payload):

        try:

            await db.connect()

            user = await super().read({'email': payload['email']})

            if (len(user) == 0):
                raise Exception(
                    {'name': 'forbidden', 'message': 'User doesnt exist'})

            if (check_hash(payload['password'], user[0]['password']) == False):
                raise Exception(
                    {'name': 'forbidden', 'message': 'Passwords do not match'})

            user[0]['token'] = generate_token({
                'id': user[0]['id'],
                'name': user[0]['name'],
                'email': user[0]['email'],

            })

            return {'success': True, 'data': user[0]}

        except Exception as e:

            return {'success': False, 'data': e.args[0]}

        finally:
            await db.disconnect()
