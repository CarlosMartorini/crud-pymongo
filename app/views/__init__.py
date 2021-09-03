from flask import Flask

def init_app(app: Flask):
    from app.views.routes_view import routes_view
    routes_view(app)
    return app