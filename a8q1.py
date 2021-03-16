

InitialString = 'I CHOOSE YOU PIKACHU'
print(InitialString)

def rev_sentence(sentence):
    words = sentence.split(' ')

    reverse_phrase = ' '.join(reversed(words))
    print("reversed string :\n")
    return reverse_phrase

if __name__ == "__main__":
    input = InitialString
    print(rev_sentence(input))
#REcursive function
def reverse(str):
    print("Reversed string")
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]
    
mystr = InitialString