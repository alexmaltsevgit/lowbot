import time


def decorate_all_methods(decorator, exclude=None):
    if exclude is None:
        exclude = []

    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)) and attr not in exclude:
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls

    return decorate


def sleep_after(sleep_time):
    def decorator(function):
        def wrapper(*args, **kwargs):
            res = function(*args, **kwargs)
            time.sleep(sleep_time)
            return res

        return wrapper

    return decorator


def return_default_on_exception(default, exception=Exception):
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except exception:
                return default

        return wrapper

    return decorator


def pass_exception(exception=Exception):
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except exception:
                pass

        return wrapper

    return decorator
