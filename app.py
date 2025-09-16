# -*- coding: utf-8 -*-
import sys
from pathlib import Path
from flask import Flask

PARENT = Path(__file__).parent
sys.path.append(str(PARENT / "utils"))

# 自定義
import users
import auth

def required_auth():
    return auth.basic_auth()


app = Flask(__name__)

# 綁定 auth 攔截
bps = [users.bp_users]
for bp in bps:
    bp.before_request(required_auth)

app.register_blueprint(users.bp_users, url_prefix="/users")
