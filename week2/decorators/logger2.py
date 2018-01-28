#logger with different file


def logger(filename):
    def decorator(func):
        def decorated(*args, **kwargs):
            res = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(f'res= {str(res)}')
                return res
        return decorated
    return decorator


@logger('new_log.txt')
def summator(num_list):
    return sum(num_list)


summator([1,2,4,5,6,7])


with open('new_log.txt', 'r') as f:
    print(f.read())


# summator = logger(.txt, summator)