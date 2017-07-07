# https://www.codewars.com/kata/regex-validate-pin-code/train/python
def validate_pin(pin):
    if (pin.isdigit()):
        if (len(pin) == 4 or len(pin) == 6):
            return True
    return False


print ".234".isdigit()
