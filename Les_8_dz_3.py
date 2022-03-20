from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args_list = []
        for arg in args:
            args_list.append(f'{arg}: {type(arg)}')
        for kwarg in kwargs:
            print(f', {kwarg}={kwarg}:', type(kwarg), end='')
            print(f'{")"} -> {result}:', type(result))
        return result
    return wrapper


@type_logger
def calc_cube(x, y, z, arg1=0, arg2=''):
    return x ** 3


a = calc_cube(5, 'asd', [12, 22, 'wer'], arg1='po', arg2=33)

