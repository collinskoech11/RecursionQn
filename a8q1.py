InitialString = 'I CHOOSE YOU PIKACHU'
print(InitialString)

def rev_sentence(sentence):
    words = sentence.split(' ')

    reverse_phrase = ' '.join(reversed(words))

    return reverse_phrase

if __name__ == "__main__":
    input = InitialString
    print(rev_sentence(input))