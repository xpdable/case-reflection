import os


def fooONE(**kwargs):
    return kwargs


def fooTWO(**kwargs):
    return os.name


def foo(**kwargs):
    print(os.name)


