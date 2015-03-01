"""
# OTPy - One Time Password in Python
*It's pronounced "Oaty Pie"*

A Python library for generating one time passwords according to
[RFC 4226](http://tools.ietf.org/html/rfc4226) and the
[HOTP RFC](http://tools.ietf.org/html/draft-mraihi-totp-timebased-00),
adapted for Python 3 (removing legacy code for Python 2) from
[Nathan Reynold's port](https://github.com/nathforge/pyotp) of
Mark Percival's [ ROTP ](https://github.com/mdp/rotp). Phew!

This is compatible with Google Authenticator apps available for Android
and iPhone, and should work similarly to GMail, World of Warcraft, and
other OTP based authenticators.
"""

VERSION = '1.3.0'

#import base64
#import os
#import math

from .otp import OTP
from .hotp import HOTP
from .totp import TOTP
from . import utils

from .utils import random_base32


