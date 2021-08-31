import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["blog"]

class Post:
    
    
    def __init__(self, id=1, created_at='', updated_at='', title='', author='', tags=[], content=''):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content


    @staticmethod
    def get_data():
        
        all_posts = []
        posts_list = db.posts.find()
        
        for post in posts_list:
            all_posts.append(post)
        
        return all_posts


    def handle_id(self):
        
        data = self.get_data()
        id = data[-1]['id']
        self.id = id + 1


    def create_post(self):
        
        self.handle_id()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        post = {
            "id": self.id,
            "created_at": self.created_at,
            "update_at": self.updated_at,
            "title": self.title,
            "author": self.author,
            "tags": self.tags,
            "content": self.content 
        }

        db.posts.insert_one(post)

