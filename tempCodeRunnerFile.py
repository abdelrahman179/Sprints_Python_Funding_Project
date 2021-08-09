import re
# for validating a Mobile number
def mobile_checker(mobile):
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("(0020|+20)?[7-9][0-10]{10}")
    return Pattern.match(mobile)

mobile = "01231234313"
test = mobile_checker(mobile)