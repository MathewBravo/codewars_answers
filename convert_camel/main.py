import re

def to_camel_case(text):
    if len(text) == 0:
        return text
    split_text = re.split('[^a-zA-Z]', text)
    final_string = split_text[0]
    for i,value in enumerate(split_text):
        if i != 0:
            final_string = final_string + value.capitalize()

    return final_string



if __name__ == "__main__":
    test = "the_stealth_warrior"
    if to_camel_case(test) == "theStealthWarrior":
        print("t1 passed")
    test = "The-Stealth-Warrior"
    if to_camel_case(test) == "TheStealthWarrior":
        print("t2 passed")
    test = "A-B-C"
    if to_camel_case(test) == "ABC":
        print("t3 passed")
