import operator as op


def duplicate_encode(word) -> str:
    word = word.lower()
    new_string = ""
    for i in word:
        count = op.countOf(word, i)
        if count > 1:
            new_string += ")"
        else:
            new_string += "("
    return new_string

                            
if __name__ == "__main__":
    print(duplicate_encode("Success"))






