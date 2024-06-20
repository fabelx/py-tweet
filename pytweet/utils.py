import math
from string import ascii_lowercase, digits


def validate_tweet_id(tweet_id: str) -> bool:
    """Validates a tweet ID.

    This function checks if the given tweet ID is less than 40 characters long and
    consists only of numeric characters.

    Args:
        tweet_id: The tweet ID to be validated.

    Returns:
        bool: True if the tweet ID is valid, False otherwise.
    """
    return len(tweet_id) < 40 and tweet_id.isdigit()


def base36_encode(number: float) -> str:
    """Encodes a given number into a base36 string.

    This function takes a floating-point number, separates it into integer and fractional parts,
    and encodes each part into base36. The base36 encoding uses digits (0-9) and lowercase
    letters (a-z).

    Args:
        number: The number to be encoded.

    Returns:
        str: The base36 encoded string representation of the number.
    """
    chars = digits + ascii_lowercase
    integer_part = int(number)
    fractional_part = number - integer_part

    # Encode the integer part
    encoded = ""
    while integer_part > 0:
        integer_part, remainder = divmod(integer_part, 36)
        encoded = chars[remainder] + encoded

    # Encode the fractional part (if necessary)
    if fractional_part > 0:
        encoded += "."
        while fractional_part > 0:
            fractional_part *= 36
            digit = int(fractional_part)
            encoded += chars[digit]
            fractional_part -= digit

    return encoded


def get_id_token(tweet_id: str) -> str:
    """Generates a token from a tweet ID.

    This function converts the tweet ID (assumed to be a numeric string) into a float, scales it,
    and then encodes it into a base36 string. The resulting string is cleaned by removing '0'
    characters and the decimal point.

    Args:
        tweet_id: The tweet ID to be converted into a token.

    Returns:
        str: The generated token.
    """
    return (
        base36_encode((int(tweet_id) / 1e15) * math.pi)
        .replace("0", "")
        .replace(".", "")
    )
