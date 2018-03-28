import random
print('This program generates a passphrase from words in the diceware database.')
print('')
length = input('Desired length of passphrase (words): ')

def generator():
    words = ''
    n = 0
    while n < 5:
        number = random.randrange(1,7)
        words += str(number)
        n += 1
    return(words)

def read_file(numberlist):
    password = []
    for item in numberlist:
        with open('diceware.txt', 'r') as f:
            for line in f:
                if str(item) in line:
                    password.append(line[6:-1])
    passwordstring = ' '.join(password)
    print(passwordstring)

L = int(length)
numberlist = []
while L > 0:
    numberlist.append(int(generator()))
    L -= 1
read_file(numberlist)
