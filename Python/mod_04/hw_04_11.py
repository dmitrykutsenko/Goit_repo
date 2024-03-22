def is_valid_password(password):
    got_upr = False
    got_low = False
    got_num = False

    if len(password)==8:

        for i in range(0, len(password)):
            if ord(password[i]) >= 65 and ord(password[i]) <= 90:
                print("upr = " + password[i])
                got_upr = True
                break

        for j in range(0, len(password)):
            if ord(password[j]) >= 97 and ord(password[j]) <= 122:
                print("low = " + password[j])
                got_low = True
                break

        for k in password:
            if k in "0123456789":
                print("num = "+k)
                got_num = True
                break

    print(str(got_upr and got_low and got_num))

is_valid_password('z,qrE*IE')
is_valid_password('b8g^ro4^')