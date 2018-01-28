# functions which returns function
# example: when functions are started, additional check what user is LOGIN
def logger(func):
    def wrapped(num_list):
        result = func(num_list)
        with open('log.txt', 'w') as f:
            f.write(str(result))

        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)

summator([1, 2, 3, 4, 5])

with open('log.txt', 'r') as f:
    print('log.txt:',f.read())