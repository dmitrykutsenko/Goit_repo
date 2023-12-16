def is_valid_pin_codes(pin_codes):
    res = False
    check = set(pin_codes)
    print("1)")
    print(check)
    for each in check:
        print("2)")
        print(each)
        try:
            res = int(each)
            if res >= 0:
                res = bool(len(pin_codes) == len(check) and len(each) == 4)        
        except:
            res = False
            break

    print("res")
    print(str(res))


is_valid_pin_codes(['1102', '9034', '9034', '0011'])