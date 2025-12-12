from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def init_limiter(app):
    Limiter(
        get_remote_address,
        app=app,
        default_limits=["200 per hour"]
    )
