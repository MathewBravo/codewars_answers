def valid_braces(string) -> bool:
    bracket_track = []
    for ch in string:
        if ch == "{":
            bracket_track.append("c_open")
        elif ch == "(":
            bracket_track.append("n_open")
        elif ch == "[":
            bracket_track.append("s_open")
        elif ch == "}":
            contains = False
            if len(bracket_track) == 0:
                return False
            if bracket_track[len(bracket_track) - 1] == "c_open":
                bracket_track.pop()
                contains = True
            if not contains:
                return False
        elif ch == ")":
            contains = False
            if len(bracket_track) == 0:
                return False
            if bracket_track[len(bracket_track) - 1] == "n_open":
                bracket_track.pop()
                contains = True
            if not contains:
                return False
        elif ch == "]":
            contains = False
            if len(bracket_track) == 0:
                return False
            if bracket_track[len(bracket_track) - 1] == "s_open":
                bracket_track.pop()
                contains = True
            if not contains:
                return False
    if len(bracket_track) > 0:
        return False
    else:
        return True


if __name__ == "__main__":
    if not valid_braces("[([]])"):
        print("1 Pass")

