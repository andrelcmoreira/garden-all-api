from rest_framework.views import exception_handler


ERROR_TYPES = [
    'not_found',
    'min_value',
    'invalid',
    'blank',
    'required',
    'does_not_exist'
]


def exc_handler(exc, context):
    reply = exception_handler(exc, context)

    _,val = reply.data.popitem()
    detail = val[0] if isinstance(val, list) else val

    if detail.code in ERROR_TYPES:
        reply.data.clear()
        reply.data['msg'] = detail

    return reply
