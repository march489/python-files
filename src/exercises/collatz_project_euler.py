collatz_dictionary = {
    1: 0
}

def collatz_step(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(3 * n + 1)

def collatz_length(n):
    if n in collatz_dictionary:
        return collatz_dictionary[n]
    else:
        collatz_dictionary[n] = int(collatz_length(collatz_step(n)) + 1)
        return collatz_dictionary[n]

for n in range (1, 1001):
    collatz_length(n)

print([k for k, v in collatz_dictionary.items()])

def collatz_chain(n):
    if n == 1:
        return [1]
    else:
        if [n].extend(collatz_chain(collatz_step(n))) == None:
            print(n)
        return [n].extend(collatz_chain(collatz_step(n)))

collatz_chain(100)

print(len(collatz_dictionary))