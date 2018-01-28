def bold(func):
    def wrapped1():
        return "<b>" + func() + "</b>"
    return wrapped1


def italic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped


@bold
@italic
def hello():
    return "hello"

print(hello())

# hello = bold(italic(hello))
