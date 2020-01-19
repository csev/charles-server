from fire_api import webtoken, scope, validate, accept, content_type, objectid
from fire_api import preflight, jsonapi, Error

from server import server
from models.user import User

@server.options('/v1/update-username/<userId>')
async def _(request, userId):
    return preflight(methods=['PATCH'])

@server.patch('/v1/update-username/<userId>')
@objectid('userId')
@webtoken
@scope({ 'update-username': '$userId' })
@content_type
@accept
@validate
async def _(request, userId, token):

    data = request.json.get('data')
    attributes = data.get('attributes')

    new_username = attributes.get('new_username')

    if not new_username:
        error = Error(
            title = 'Update Username Error',
            detail = 'Missing new_username attribute.',
            status = 403
        )
        return jsonapi({ 'errors': [ error.serialize() ] }, status=403)

    user = await User.find_by_id(userId)

    if not user:
        error = Error(
            title = 'Update Username Error',
            detail = 'User not found.',
            status = 403
        )
        return jsonapi({ 'errors': [ error.serialize() ] }, status=403)

    user.username = new_username

    try:
        await user.save()
    except Exception as e:
        error = Error(
            title = 'Update Username Error',
            detail = str(e),
            status = 403
        )
        return jsonapi({ 'errors': [ error.serialize() ] }, status=403)

    return jsonapi({
        'data': {
            'attributes': {
                'status': 'Username updated.'
            }
        }
    }, status=200)
