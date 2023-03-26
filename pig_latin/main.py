def pig_it(text):
    split_text = text.split()
    new_str = ""
    for i in split_text:
        if (i.isalpha()): 
            new_str += i[1:] + i[0] + "ay "
        else:
            new_str += i + " "
    return new_str[:len(new_str)-1]


def test_result(one, two):
    if one == two:
        print("pass")

if __name__ == "__main__":
    test_result(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
    test_result(pig_it('This is my string'),'hisTay siay ymay tringsay')
    test_result(pig_it('Quis custodiet ipsos custodes ?'), 'uisQay ustodietcay psosiay ustodescay ?')
