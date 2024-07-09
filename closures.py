import logging


def outer(msg):
    message = msg

    def inner():
        print(message)

    return inner


def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
    return wrap_text


temp_func = outer('potatoes')

temp_func()

temp_func2 = outer('mash em up')

temp_func2()

tagger = html_tag('p')

tagger('hobbits')


logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(f'Running {func.__name__} with arguments: {args}')
        print(func(*args))
    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(2, 2)
sub_logger(2, 3)
