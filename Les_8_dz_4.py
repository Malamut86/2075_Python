from functools import wraps


def check_arg(arg):
    if len(arg) != 1:
        msg = f'wrong val {arg}'
        raise ValueError(msg)
    if not isinstance(arg[0], int) or arg[0] <= 0:
        msg = f'wrong val {arg[0]}'
        raise ValueError(msg)


def val_checker(chek_func):
    def _val_checker(func):
        @wraps(func)
        def valide_wrap(arg):
            chek_func(arg)
            result = func(arg)
            return result
        return valide_wrap
    return _val_checker


@val_checker(check_arg)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))