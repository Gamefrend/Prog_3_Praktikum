vowels = ['a', 'e', 'i', 'o', 'u']


def devocalize(s):
    """
    devocalize(string) -> string
    :rtype: object
    """
    out = ""
    for letter in s:
        if letter.lower() not in vowels:
            out = out + letter
    return out


print(devocalize('WTF warum ist die IDE so krass'))
