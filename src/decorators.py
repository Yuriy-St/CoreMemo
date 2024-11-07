from typing import Callable

from .custom_exceptions import InputException, RecordNotFountException


# TODO: to be updated for each exception type
def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (InputException, RecordNotFountException) as e:
            return f"{e}"
        except ValueError as e:
            return f"{e}"
        except KeyError as e:
            return f"{e}"
        except IndexError as e:
            return f"{e}"

    return inner
