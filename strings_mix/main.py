def mix(s1, s2):
    #only track lowercase letters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    string_resp = ""
    string_array = []
    for l in letters:
        s1_count = s1.count(l)
        s2_count = s2.count(l)
        if s2_count <= 1 and s1_count <= 1:
            continue
        if s1_count == s2_count:
            dif = "="
        else:
            dif = "1" if s1_count > s2_count else "2"
        letter_visual = l * max(s1_count, s2_count)
        string_resp = dif + ":" + letter_visual
        string_array.append(string_resp)
    sort_key = lambda s: (-len(s),  s[0], s[-1])
    string_array = sorted(string_array, key=sort_key)
    string_resp = ""
    for s in string_array:
        string_resp+=s + "/"
    return string_resp[:-1]


if __name__ == '__main__':
    test1 = "Are the kids at home? aaaaa fffff"
    test = "Yes they are here! aaaaa fffff"
    print(mix(test, test1))
