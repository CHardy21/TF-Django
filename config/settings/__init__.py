import os

env = os.getenv("ENV", "local").lower()

if env == "production":
    from .produccion import *
else:
    from .local import *
