from rest_framework.views import exception_handler


ERROR_MSGS = {
    'not_found': "The requested resource was not found",
    'min_value': "The provided value for '{}' must be greater than 0",
    'invalid': "The provided value for '{}' is invalid",
    'blank': "The '{}' field cannot be blank",
    'required': "The '{}' field is required",
    'does_not_exist': "The provided '{}' does not exist"
}


def exc_handler(exc, context):
    reply = exception_handler(exc, context)

    _,val = reply.data.popitem()
    detail = val[0] if isinstance(val, list) else val

    if detail.code in ERROR_MSGS.keys():
        reply.data.clear()
        reply.data['msg'] = detail

    return reply
