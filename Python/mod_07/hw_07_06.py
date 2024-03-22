def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse:
        riddle = riddle[::-1]
    n = riddle.find(start_letter)
    if n != -1 and len(riddle) >= n + word_length:
        s = riddle[n: n + word_length]
        return s
    return  ""
print(solve_riddle('mi1powperet', 3, 'r', True))