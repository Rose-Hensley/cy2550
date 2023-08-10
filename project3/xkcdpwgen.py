import argparse, random

def main():
    parser = argparse.ArgumentParser(prog='xkcdwgen', description='Generate a secure, memorable password using the XKCD method')

    parser.add_argument('-w', '--words', type=int, default=4, help='include WORDS words in the password, defaults to 4')
    parser.add_argument('-c', '--caps', type=int, default=0, help='capitalize the first letter of CAPS random words, defaults to 0')
    parser.add_argument('-n', '--numbers', type=int, default=0, help='insert NUMBERS random numbers in the password, defaults to 0')
    parser.add_argument('-s', '--symbols', type=int, default=0, help='insert SYMBOLS random symbols in the password, defaults to 0')

    args = parser.parse_args()

    with open('words.txt') as file:
        words = file.readlines()

    # Selecting random words
    random_words = random.sample(words, args.words)
    selected_words = [word.rstrip() for word in random_words]

    # Capitalizing random amount words
    for i in range(min(args.words, args.caps)):
        selected_words[i] = selected_words[i].title()
    random.shuffle(selected_words)

    # Making it a long string
    ret = ''.join(selected_words)

    # Adding in numbers
    for i in range(args.numbers):
        loc = random.randrange(len(ret))
        ret = ret[0:loc] + str(random.randint(0, 9)) + ret[loc:len(ret)]

    # Adding in symbols
    symbols = '~!@#$%^&*.:;'
    for i in range(args.symbols):
        loc = random.randrange(len(ret))
        ret = ret[0:loc] + random.choice(symbols) + ret[loc:len(ret)]

    print(ret)

if __name__ == '__main__':
    main()
