# dict is actually a hash table
book = dict()
book['apple'] = 0.37
book['milk'] = 1.49
book['avocado'] = 1.49
print(book)
print(book['avocado'])

# voting
voted = {}


def check_voter(name):
    if voted.get(name):
        print('kick them out!')
    else:
        voted[name] = True
        print('let them vote!')


check_voter('tom')
check_voter('mike')
check_voter('mike')
