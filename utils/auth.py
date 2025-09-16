from functools import wraps
from flask import request, Response

# ----------------------------
# Basic Auth
# ----------------------------
def _check_auth(username, password):
    return username == "admin" and password == "12345"

def _authenticate():
    return Response(
        "Failed to login", 401,
        {"WWW-Authenticate": 'Basic realm="Login Required"'}
    )

def basic_auth():
    auth = request.authorization
    if not auth or not _check_auth(auth.username, auth.password):
        return _authenticate()

def basic_auth_decorate(f):
    @wraps(f)  # 保留 function 原本的 __name__ 與一些屬性
    def wrapped(*args, **kwargs):
        rsp = basic_auth()
        return f(*args, **kwargs) if rsp is None else rsp
    return wrapped
