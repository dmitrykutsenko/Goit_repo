def is_integer(s):
    s = s.strip()
    if len(s) == 0:
        return False
    if s[0] == "+" or s[0] == "-":
        return s[1:].isdigit()
    return s.isdigit()