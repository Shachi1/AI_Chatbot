from app.like.service import LikeService
from flask import Blueprint, current_app, request
from werkzeug.local import LocalProxy
from app.utils import generate_query_model
from authentication import require_appkey
from app.utils.response import ResponseSuccess, ResponseError

logger = LocalProxy(lambda: current_app.logger)
likeService = LikeService()
likeController = Blueprint('like', __name__)


@likeController.before_request
def before_request_func():
    current_app.logger.name = 'like'


@likeController.route('/like/add', methods=['POST'])
async def add():
    result = await likeService.add(request.get_json())

    if (result['success'] == True):
        return ResponseSuccess(result['data'], 'add successful').getResponse()
    else:
        return ResponseError(result['data'], 'add failed').getResponse()


@likeController.route('/like/remove/<id>', methods=['DELETE'])
async def remove(id):
    result = await likeService.remove(id)

    if (result['success'] == True):
        return ResponseSuccess(result['data'], 'edit successful').getResponse()
    else:
        return ResponseError(result['data'], 'edit failed').getResponse()
