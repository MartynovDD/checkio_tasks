def type_checker(expected_type: type, value: any):
    if type(value) != expected_type:
        raise TypeError
