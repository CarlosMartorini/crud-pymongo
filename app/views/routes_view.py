from flask import Flask, request, jsonify
from app.models.post_model import Post
import json

def routes_view(app: Flask):

    @app.post('/posts')
    def create_post():
        data = request.get_json()
        try:
            Post.have_all_info(data)
            Post.is_correct_info(data)
            post_to_add = Post(**data)
            post_to_add.create_post()
            return post_to_add.info(), 201
        except:
            return {'msg': 'Something is wrong with post infos!'}, 400
        
    
    @app.get('/posts')
    def get_posts():
        try:
            request = Post.get_data()
            return jsonify(request), 200
        except:
            return {'msg': 'Sorry, you dont have posts yet!'}
    

    @app.get('/posts/<int:post_id>')
    def get_specific_post(post_id: int):
        try:
            request = Post.get_specific_data(int(post_id))
            return jsonify(request), 200
        except:
            return {'msg': 'Post not exists!'}, 404
    

    @app.patch('/posts/<int:post_id>')
    def update_post(post_id: int):
        data = request.get_json()
        try:
            Post.have_all_info(data)
            Post.is_correct_info(data)
            to_update = Post.get_specific_data(int(post_id))
            Post.update_post(to_update, data)
            show_post = Post.get_specific_data(int(post_id))
            return jsonify(show_post), 200
        except:
            return {'msg': 'Something is wrong post cant updated!'}, 400
    

    @app.delete('/posts/<int:post_id>')
    def delete_post(post_id: int):
        try:
            to_delete = Post(id = int(post_id))
            to_delete.delete_post()
            return {'msg': 'Post successfully deleted!'}, 200
        except:
            return {'msg': 'Something went wrong when deleting the post!'}, 400

