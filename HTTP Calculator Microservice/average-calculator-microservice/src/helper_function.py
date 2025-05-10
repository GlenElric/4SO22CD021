def is_valid_number_id(number_id):
    valid_ids = {'p', 'f', 'e', 'r'}
    return number_id in valid_ids

def format_response(prev_num, curr, avg):
    return {
        "previous_number": prev_num,
        "current_number": curr,
        "average": avg
    }