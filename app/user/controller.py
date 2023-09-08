from flask import Blueprint, current_app, request
from werkzeug.local import LocalProxy

from authentication import require_appkey
from app.user.service import UserService
from app.utils.response import ResponseSuccess, ResponseError

userController = Blueprint('user', __name__)
logger = LocalProxy(lambda: current_app.logger)

userService = UserService()


@userController.before_request
def before_request_func():
    current_app.logger.name = 'user'


@userController.route('/user/signup', methods=['POST'])
async def signup():
    result = await userService.signup(request.get_json())

    if (result['success'] == True):
        return ResponseSuccess(result['data'], 'signup successful').getResponse()
    else:
        return ResponseError(result['data'], 'signup failed').getResponse()


@userController.route('/user/signin', methods=['POST'])
async def signin():
    result = await userService.signin(request.get_json())

    if (result['success'] == True):
        return ResponseSuccess(result['data'], 'signin successful').getResponse()
    else:
        return ResponseError(result['data'], 'signin failed').getResponse()
