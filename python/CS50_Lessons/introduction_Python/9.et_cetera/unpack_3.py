def f_args(*args, **kwargs):
    print("Positional:", args)

def f_kwargs(*args, **kwargs):
    print("Kwargs:", kwargs)


f_args(100, 50, 25)
f_kwargs(100,50,25)
# TODO, print this user name
name = "Jack"
f_kwargs(print="Hello, f'{name}'")