from flask import Flask
from config import MAX_WINDOW_SIZE, RESPONSE_TIME
from numbers import numbers_bp

app = Flask(__name__)
app.config['MAX_WINDOW_SIZE'] = MAX_WINDOW_SIZE
app.config['RESPONSE_TIME'] = RESPONSE_TIME

app.register_blueprint(numbers_bp, url_prefix='/numbers')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)