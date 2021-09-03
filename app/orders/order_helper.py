"""This module contain functions validates order inputs."""
import re
def validate_order(data):
    """Validates order inputs."""
    try:
        if not type(data['product_name']) == str or not type(data['quantity']) == str:
            return 'Invalid entry, Input should be in a valid json format.'
        if not data['product_name'].strip()  or not data['quantity'].strip():
            return "All fields are required."
        if not re.match("^[a-zA-Z]*$", data['product_name'].strip()):
            return "Product name should only contain alphabetic characters."
        elif not re.match("^[0-9_]*$", data['quantity'].strip()):
            return "Quantity should be an integer."
        else:
            return 'valid'
    except KeyError:
        return "All keys are required."
