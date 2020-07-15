def check_type(expected_type: type, value: any):
    """
    Checks the type of given value
    :param expected_type: A type to compare
    :param value: Value to be checked
    :return: None if type is correct, otherwise raise TypeError
    """
    if type(value) != expected_type:
        raise TypeError("Given value doesn't match expected type")
