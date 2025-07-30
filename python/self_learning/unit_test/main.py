sister_age: int = 10
brother_age: int = 12


def is_sister_older_than_brother() -> bool:
    """
    Check if sister is older than brother.
    :return: True if sister is older, False otherwise.
    """
    print(f"Sister's age: {sister_age}, Brother's age: {brother_age}")
    if sister_age > brother_age:
        print("Sister is older than brother")
        return True
    else:
        print("Brother is older than sister")
        return False
