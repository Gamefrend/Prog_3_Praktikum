import re


def Wortderehen(s):
    return s[::-1]


input = "eiD 17 adnaP-nereaB dnis, eniem hci , ZNAG_giztup!"
output = ""
for s in re.split(r'[_\W]+', input):
    if len(output) < len(input):
        while re.compile(r'[_\W]+').match(input[len(output)]) is not None:
            output += input[len(output)]
            if len(output) == len(input):
                break
    output += Wortderehen(s)
print(output)
