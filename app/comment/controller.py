from app.comment.service import CommentService
from flask import Blueprint, current_app, request
from werkzeug.local import LocalProxy
from app.utils import generate_query_model

from authentication import require_appkey

from app.utils.response import ResponseSuccess, ResponseError

logger = LocalProxy(lambda: current_app.logger)
commentService = CommentService()
commentController = Blueprint('comment', __name__)


@commentController.before_request
def before_request_func():
    current_app.logger.name = 'comment'


@commentController.route('/comment/add', methods=['POST'])
async def add():
    result = await commentService.add(request.get_json())

    if (result['success'] == True):
        return ResponseSuccess(result['data'], 'add successful').getResponse()
    else:
        return ResponseError(result['data'], 'add failed').getResponse()


@commentController.route('/comment/edit/<id>', methods=['PUT'])
async def edit(id):
    result = await commentService.edit(id, request.get_json())

    if (result['success'] == True):
        return ResponseSuccess(result['data'], 'edit successful').getResponse()
    else:
        return ResponseError(result['data'], 'edit failed').getResponse()


@commentController.route('/comment/remove/<id>', methods=['DELETE'])
async def remove(id):
    result = await commentService.remove(id)

    if (result['success'] == True):
        return ResponseSuccess(result['data'], 'remove successful').getResponse()
    else:
        return ResponseError(result['data'], 'remove failed').getResponse()
