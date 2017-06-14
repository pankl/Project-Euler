import random
import string


def valid(ch):
    if ch.isalpha() and len(ch) == 1:
        return True
    return False


def main():
    listWords = ['elephant', 'whale', 'dog', 'dinosaur', 'plant']
    word = listWords[random.randint(0, len(listWords)-1)]
    numTries = 5
    maskedWord = [[x,0] for x in word]
    numMasked = len(word)
    while numTries > 0:
        printWord = ''
        for x in maskedWord:
            c = '#' if x[1] == 0 else x[0]
            printWord += c
        print printWord
        ch = raw_input('type your guess:')
        ch = string.lower(ch)
        if valid(ch):
            if ch in word:
                numMasked -= 1
                for x in maskedWord:
                    if ch == x[0]:
                        x[1] = 1
                if numMasked == 0:
                    print 'You\'ve won'
                    print 'The word is: ' + word
                    numTries = 0
                    break
            else:
                numTries -= 1
                if numTries != 0:
                    print 'wrong guess\nyou\'ve left with %d guesses' % numTries
                else:
                    print 'You lost\nThe word was: ' + word
                    break
        else:
            print "Input only one char at a time"

if __name__ == "__main__":
    main()
