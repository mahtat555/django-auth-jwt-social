from typing import Any


def str_to_bool(value: Any) -> bool:
    """ Convert a string representation of truth to True or False.
    """
    if str(value).lower() in ("n", "no", "f", "false", "off", "0"):
        return False

    if str(value).lower() in ("y", "yes", "t", "true", "on", "1"):
        return True

    raise ValueError(f"invalid truth value '{value}'")
