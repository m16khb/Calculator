import re


def tokenize(expStr):
    RE = re.compile(r'(?:(?<=[^\d\.])(?=\d)|(?=[^\d\.]))', re.MULTILINE)
    return [x for x in re.sub(RE, " ", expStr).split(" ") if x]
