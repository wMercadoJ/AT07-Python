
# Replace words in a string


def replace(s, old, new):
    return s.replace(old, new)


if __name__ == '__main__':
    print "Enter String"
    chain = str(raw_input())
    print "Enter what word it replaces"
    old_word = str(raw_input())
    print "Enter new word"
    new_word = str(raw_input())
    print "Result-----", replace(chain, old_word,new_word)
