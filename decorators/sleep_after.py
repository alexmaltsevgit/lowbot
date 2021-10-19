import time


def sleep_after(sleep_time):
    def decorator(function):
        def wrapper(*args, **kwargs):
            function()
            time.sleep(sleep_time)

        return wrapper
    return decorator
