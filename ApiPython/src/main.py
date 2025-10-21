# import sys
# import os
# dir = __file__[:-12]
# os.chdir(dir)
# if dir not in sys.path:
#     sys.path.append(dir)

from fastapi import FastAPI
from src.api import register_routes

app = FastAPI()

register_routes(app)