# this returns to 1 to 10
def count_up_to(n):
    for number in range(1, n + 1):
        yield number


## this 0 to 9
# def count_up_to(n):
#     for x in range(n):
#         yield x


a = count_up_to(n=10)
for value in a:
    print(value)
