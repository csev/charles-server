from fire_api import webtoken, scope, validate, accept, content_type, objectid
from fire_api import preflight, jsonapi, Error

from server import server
from models.user import User

@server.options('/v1/update-password/<userId>')
async def _(request, userId):
    return preflight(methods=['PATCH'])

@server.patch('/v1/update-password/<userId>')
@objectid('userId')
@webtoken
@scope({ 'update-password': '$userId' })
@content_type
@accept
@validate
async def _(request, userId, token):

    data = request.json.get('data')
    attributes = data.get('attributes')

    current_password = attributes.get('current_password')

    if not current_password:
        error = Error(
            title = 'Update Password Error',
            detail = 'Missing current_password attribute.',
            status = 403
        )
        return jsonapi({ 'errors': [ error.serialize() ] }, status=403)

    new_password = attributes.get('new_password')

    if not new_password:
        error = Error(
            title = 'Update Password Error',
            detail = 'Missing new_password attribute.',
            status = 403
        )
        return jsonapi({ 'errors': [ error.serialize() ] }, status=403)

    user = await User.find_by_id(userId)

    if not user:
        error = Error(
            title = 'Update Password Error',
            detail = 'User not found.',
            status = 403
        )
        return jsonapi({ 'errors': [ error.serialize() ] }, status=403)

    digest = f'hashed-{hashlib.sha256(current_password.encode()).hexdigest()}'

    if not digest == user.password:
        error = Error(
            title = 'Update Password Error',
            detail = 'Current password does not match.',
            status = 403
        )
        return jsonapi({ 'errors': [ error.serialize() ] }, status=403)

    user.password = new_password

    try:
        await user.save()
    except Exception as e:
        error = Error(
            title = 'Update Password Error',
            detail = str(e),
            status = 403
        )
        return jsonapi({ 'errors': [ error.serialize() ] }, status=403)

    return jsonapi({
        'data': {
            'attributes': {
                'status': 'Password updated.'
            }
        }
    }, status=200)
