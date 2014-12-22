import sys
import urllib
import base64
import os
import math

def build_uri(secret, name, initial_count=None, issuer_name=None):
    """
    Returns the provisioning URI for the OTP; works for either TOTP or HOTP.

    This can then be encoded in a QR Code and used to provision the Google
    Authenticator app.

    For module-internal use.

    See also:
        http://code.google.com/p/google-authenticator/wiki/KeyUriFormat

    @param [String] the hotp/totp secret used to generate the URI
    @param [String] name of the account
    @param [Integer] initial_count starting counter value, defaults to None.
        If none, the OTP type will be assumed as TOTP.
    @param [String] the name of the OTP issuer; this will be the
        organization title of the OTP entry in Authenticator
    @return [String] provisioning uri
    """
    # initial_count may be 0 as a valid param
    base = 'otpauth://'
    base += 'hotp/' if initial_count is not None else 'totp/'

    if issuer_name:
        base += urllib.parse.quote(issuer_name) + ":"
    base += urllib.parse.quote(name, safe='@')

    params = {
        'secret': secret,
    }
    if initial_count is not None:
        params['counter'] = initial_count
    if issuer_name is not None:
        params['issuer'] = issuer_name
    
    return base + "?" + urllib.parse.urlencode(params, safe='@')


def safe_compare_strint_int(str_or_number: (str, int), number: int)->bool:
    """
    Offers as safe a way to compare *either* a string-of-int value or int
    with an integer value. That is, either comparing "12"==12 or 12==12,
    as securely as possible versus timing attacks either way.

    Either way, the secret value is "number" and is presumed to be shipped
    here by trusted code, whereas str_or_number is user-provided and may be
    crafted to attempt to reveal information about number. The fewer queries
    that interact with the *value* of number, the better.
    
    For this reason, code that might otherwise conveniently cast str/float
    to int for number is avoided. For the same reason, casting number to
    bytes/string for comparison is avoided, in favour of converting
    str_or_number to int instead.

    Raises:
        RuntimeError when a bug sends "number" a non-int value
        TypeError when str_or_number is outside (int, str)
        ValueError when str_or_number is str and not castable to int
    """
    if not isinstance(number, int):
        raise RuntimeError("Argument 'number' provided to safe_compare_strint_int is not an int, was instead type '{}'".format(type(number)))
    if isinstance(str_or_number, str):
        query_value = int(str_or_number[:309])  # Limit size of number created by user (to len(str(2**1024)))
    elif isinstance(str_or_number, int):
        query_value = str_or_number
    else:
        raise TypeError("Argument str_or_number must be string or integer, was: {}".format(str_or_number))
    return (query_value ^ number) == 0


def random_base32(length:int=16, chars=base64._b32alphabet)->str:
    byte_length = math.ceil(length / 1.6)
    randval = os.urandom(byte_length)
    return base64.b32encode(randval)[:length].decode()
