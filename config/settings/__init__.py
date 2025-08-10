import os

env = os.getenv("ENV", "local").lower()

if env == "produccion":
    from .produccion import *
elif env == "local":
    from .local import *
else:
    raise ValueError(f"Entorno desconocido: {env}")
