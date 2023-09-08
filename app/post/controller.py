from app.post.service import PostService
from flask import Blueprint, current_app, request
from werkzeug.local import LocalProxy
from app.utils import generate_query_model

from authentication import require_appkey

from app.utils.response import ResponseSuccess, ResponseError

logger = LocalProxy(lambda: current_app.logger)
postService = PostService()
postController = Blueprint('post', __name__)


@postController.before_request
def before_request_func():
    current_app.logger.name = 'post'


@postController.route('/post/add', methods=['POST'])
async def add():
    result = await postService.add(request.get_json())

    if (result['success'] == True):
        return ResponseSuccess(result['data'], 'add successful').getResponse()
    else:
        return ResponseError(result['data'], 'add failed').getResponse()


@postController.route('/post/edit/<id>', methods=['PUT'])
async def edit(id):
    result = await postService.edit(id, request.get_json())

    if (result['success'] is True):
        return ResponseSuccess(result['data'], 'edit successful').getResponse()
    else:
        return ResponseError(result['data'], 'edit failed').getResponse()


@postController.route('/post/get', methods=['GET'])
async def getAll():
    result = await postService.getAll(generate_query_model(request.query_string))

    if (result['success'] is True):
        return ResponseSuccess(result['data'], 'fetch post successful').getResponse()
    else:
        return ResponseError(result['data'], 'fetch post failed').getResponse()


@postController.route('/post/remove/<id>', methods=['DELETE'])
async def remove(id):
    result = await postService.remove(id)

    if (result['success'] == True):
        return ResponseSuccess(result['data'], 'remove successful').getResponse()
    else:
        return ResponseError(result['data'], 'remove failed').getResponse()