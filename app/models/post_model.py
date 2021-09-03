from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")

db = client['kenzie']
collection = db['posts']

needed_params = ['title', 'author', 'tags', 'content']

class Post:
    
    
    def __init__(self, title='', author='', tags=[], content='', id=1, created_at='', updated_at=''):
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
        posts_list = collection.find()
        
        for post in posts_list:
            del post['_id']
            all_posts.append(post)
        
        return all_posts
    

    @staticmethod
    def get_specific_data(post_id: int):

        request = collection.find_one({'id': int(post_id)})
        print(request)
        if request == None:
            return {'msg': 'Post not exists!'}, 404
        else:
            del request['_id']
            return request


    def handle_id(self):
        data = self.get_data()
        if len(data) < 1:
            self.id = 1
        else:
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

        collection.insert_one(post)

    
    def info(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "title": self.title,
            "author": self.author,
            "tags": self.tags,
            "content": self.content
        }


    @staticmethod
    def have_all_info(request):

        dont_have_params = [item for item in needed_params if item not in request]
        if dont_have_params != []:
            return {'msg': 'Some keys are missing!'}, 400
    

    @staticmethod
    def is_correct_info(request):

        not_correct_info = [item for item in request if item not in needed_params]
        if not_correct_info != []:
            return {'msg': 'Some keys are not correct!'}, 400
    

    @staticmethod
    def update_post(request_post, updated_post: dict):

        updated_post['updated_at'] = datetime.now()
        post = {'$set': updated_post}
        changed_post = collection.update_one(request_post, post)
        return changed_post
    

    def delete_post(self):

        data = self.get_specific_data(self.id)
        if data != None:
            collection.delete_one(data)
        else:
            return {'msg', 'Post not founded!'}, 404

