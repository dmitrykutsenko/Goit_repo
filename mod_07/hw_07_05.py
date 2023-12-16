def capital_text(s):
    if "." in s:
        s = s.split(".")
        s1 =list()
        for i in s:
            n = 0
            while i[n] == " ":
                n+=1
            m = " "*n+i[n].upper()+i[n+1:]
            s1.append(m)
        s = ".".join(s1)
    if "?" in s:
        s = s.split("?")
        s1 = list()
        for i in s:
            n = 0
            while i[n] == " ":
                n += 1
            m = " "*n+i[n].upper()+i[n+1:]
            s1.append(m)
        s = "?".join(s1)
    if "!" in s:
        s = s.split("!")
        s1 = list()
        for i in s:
            n = 0
            while i[n] == " ":
                n += 1
            m = " "*n+i[n].upper()+i[n+1:]
            s1.append(m)
        s = "!".join(s1)
    return s