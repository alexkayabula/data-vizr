"""This module contain functions validates product inputs."""
import re
def validate_product(data):
    """Validates product inputs."""
    try:
        if not type(data['product_name']) == str or not type(data['price']) == str or not type(data['category']) == str:
            return 'Invalid entry, Input should be in a valid json format.'
        if not data['product_name'].strip() or not data['price'].strip() or not data['category'].strip():
            return  "All fields are required."
        if not re.match("^[a-zA-Z]*$", data['product_name'].strip()):
            return "The product name should only contain alphabetic characters."
        if not re.match("^[a-zA-Z]*$", data['category'].strip()):
            return "The category should only contain alphabetic characters."
        elif  not re.match("^[0-9]*$", data['price'].strip()):
            return "The price should only contain numeric characters."
        else:
            return 'valid'
    except KeyError:
        return "All keys are required."
