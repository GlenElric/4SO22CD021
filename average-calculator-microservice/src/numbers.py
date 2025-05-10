from flask import Blueprint, jsonify
from flask import request
from number_fetcher import NumberFetcher
from calculator import Calculator
from flask import current_app
import time

numbers_blueprint = Blueprint('numbers', __name__)

# Initialize services
number_fetcher = NumberFetcher()
calculator = Calculator(max_window_size=current_app.config['MAX_WINDOW_SIZE'])

@numbers_blueprint.route('/numbers/<string:numberid>', methods=['GET'])
def get_numbers(numberid):
    start_time = time.time()
    
    # Fetch unique numbers based on the number ID
    unique_numbers = number_fetcher.fetch_numbers(numberid)
    
    # Calculate the average of the fetched numbers
    average = calculator.calculate_average(unique_numbers)
    
    # Get the previous and current state of stored numbers
    previous_state = calculator.get_previous_state()
    current_state = calculator.get_current_state(unique_numbers)
    
    # Ensure response time is within the configured limit
    elapsed_time = time.time() - start_time
    if elapsed_time < current_app.config['RESPONSE_TIME']:
        time.sleep(current_app.config['RESPONSE_TIME'] - elapsed_time)
    
    return jsonify({
        "average": average,
        "previous_state": previous_state,
        "current_state": current_state
    })