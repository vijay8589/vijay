"""reverse the words in the given string program"""

# To reverse words in a given string

# input string
string = "vijay software developer"

# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
    # apending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))




""" Function to reverse words of string."""

def rev_sentence(sentence):
    # first split the string into words
    words = sentence.split(' ')

    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))

    # finally return the joined string
    return reverse_sentence


if __name__ == "__main__":
    input = 'vijay software developer'
    print(rev_sentence(input))