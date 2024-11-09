from typing import Callable

from .custom_exceptions import InputException, RecordNotFountException


def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (InputException, RecordNotFountException) as e:
            return f"{e}" if e.args else "Please, input data correctly"
        except ValueError as e:
            return f"{e}" if e.args else "Incorrect value!"
        except KeyError as e:
            return f"{e}" if e.args else "Item not found"
        except IndexError as e:
            return f"{e}" if e.args else "Incorrect number of arguments"
        except Exception as e:
            return f"{e}" if e.args else "Oops! Something went wrong..."

    return inner
