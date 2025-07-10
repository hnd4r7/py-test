def my_decorator(value):
    def decorator(func):
        def wrapper():
            print(f"Decorator value: {value}")
            return func()

        return wrapper

    return decorator


def cf(x, i):
    @my_decorator(x)
    def func():
        print(f"Function called: {i}")

    return func


def create_decorated_functions():
    functions = []

    for i in range(3):
        x = i * 10
        functions.append(cf(x, i))

    return functions


# Test the functions
fs = create_decorated_functions()
fs[1]()
