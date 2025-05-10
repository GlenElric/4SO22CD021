from flask import Flask
from config import MAX_WINDOW_SIZE, RESPONSE_TIME
from numbers import numbers_bp

def create_app():
    app = Flask(__name__)
    app.config['MAX_WINDOW_SIZE'] = MAX_WINDOW_SIZE
    app.config['RESPONSE_TIME'] = RESPONSE_TIME
    app.register_blueprint(numbers_bp, url_prefix='/numbers')
    return app
app = create_app()

if __name__ == '__main__':
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)