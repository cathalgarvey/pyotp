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

Support is not given for any purpose, but actual identifiable and
characterised bug-reports *based on the codebase* are gratefully accepted.

## Quick overview of using One Time Passwords on your phone

* OTPs involve a shared secret, stored both on the phone and the server
* OTPs can be generated on a phone without internet connectivity (AT&T mode)
* OTPs should always be used as a second factor of authentication(if your phone is lost, you account is still secured with a password)
* Google Authenticator allows you to store multiple OTP secrets and provision those using a QR Code(no more typing in the secret)

## Installation

    pip install pyotp

## Use

### Time based OTP's

    totp = pyotp.TOTP('base32secret3232')
    totp.now() # => 492039

    # OTP verified for current time
    totp.verify(492039) # => True
    time.sleep(30)
    totp.verify(492039) # => False

### Counter based OTP's

    hotp = pyotp.HOTP('base32secret3232')
    hotp.at(0) # => 260182
    hotp.at(1) # => 55283
    hotp.at(1401) # => 316439

    # OTP verified with a counter
    hotp.verify(316439, 1401) # => True
    hotp.verify(316439, 1402) # => False

### Generating a Base32 Secret key

    pyotp.random_base32() # returns a 16 character base32 secret. Compatible with Google Authenticator

### Google Authenticator Compatible

The library works with the Google Authenticator iPhone and Android app, and also
includes the ability to generate provisioning URI's for use with the QR Code scanner
built into the app.

    totp.provisioning_uri("alice@google.com") # => 'otpauth://totp/alice@google.com?secret=JBSWY3DPEHPK3PXP'
    hotp.provisioning_uri("alice@google.com", 0) # => 'otpauth://hotp/alice@google.com?secret=JBSWY3DPEHPK3PXP&counter=0'

This can then be rendered as a QR Code which can then be scanned and added to the users
list of OTP credentials.

#### Working example

Scan the following barcode with your phone, using Google Authenticator

![QR Code for OTP](http://chart.apis.google.com/chart?cht=qr&chs=250x250&chl=otpauth%3A%2F%2Ftotp%2Falice%40google.com%3Fsecret%3DJBSWY3DPEHPK3PXP)

Now run the following and compare the output

    import pyotp
    totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
    print "Current OTP: %s" % totp.now()

### Licensing
See the file "HACKING.txt" in the root directory of the repo.

This code is licensed under the AGPL in order to encourage deriving projects
to further enrich our code commons.

Mark's original code was licensed under a very permissive license, only
those modifications I have made since the code-base are licensed under
the AGPL. So if you want to work from a more permissive license, roll back
the commits on this repository or [go to Nathan's](https://github.com/nathforge/pyotp).

True to the requirements of Mark's license, I've included his license text
in the commit history of this git repository; just roll back the commits
to see it. I haven't kept it in newer commits to avoid confusion over what
the newer revisions to the codebase are licensed under.

### Changelog

- 0.9 - Hard fork from Nathan's code as PRs had gone stale and I wanted
    to drop messy legacy support. Significant code reorganisations and clean-ups.
    As I'm maintaining a fork now, added a license I'm more comfortable with.

### See also:

* Original code-base by [Nathan Reynold](https://github.com/nathforge/pyotp)
* Original Ruby version of ROTP by [Mark Percival](https://github.com/mdp) - [ROTP](https://github.com/mdp/rotp)
* PHP port of ROTP by [Le Lag](https://github.com/lelag) - [OTPHP](https://github.com/lelag/otphp)
