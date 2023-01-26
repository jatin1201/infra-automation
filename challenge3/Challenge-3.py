def get_value(obj, key):
    """
    This function takes in a nested object and a key in the format "a/b/c" and returns the corresponding value.
    It uses the "/" as a delimiter to split the key and access the nested object
    """
    keys = key.split("/")
    for k in keys:
        if k in obj:
            # if key exists in object, assign the object value to obj
            obj = obj[k]
        else:
            # if key not found in object, return None
            return None
    # return the final value
    return obj

def test_get_value():
    """
    This function tests the get_value function with sample inputs and expected outputs
    """
    object = {"a":{"b":{"c":"d"}}}
    key = "a/b/c"
    assert get_value(object, key) == "d"

    object = {"x":{"y":{"z":"a"}}}
    key = "x/y/z"
    assert get_value(object, key) == "a"

    # You can add more test cases here

    print("All test cases pass")

test_get_value()
