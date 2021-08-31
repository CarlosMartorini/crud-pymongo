import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["blog"]

class Post:
    def __init__(self, id=1, created_at='', updated_at='', title='', author='', tags=[], content=''):
        ...