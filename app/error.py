from rest_framework.views import exception_handler


def exc_handler(exc, context):
    reply = exception_handler(exc, context)

    _,val = reply.data.popitem()
    detail = val[0] if isinstance(val, list) else val

    if (detail.code == 'not_found') or \
        (detail.code == 'min_value') or \
        (detail.code == 'invalid') or \
        (detail.code == 'blank') or \
        (detail.code == 'required') or \
        (detail.code == 'does_not_exist'):
        reply.data.clear()
        reply.data['msg'] = detail

    return reply
