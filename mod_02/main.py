result = None
operand = None
operator = None
wait_for_number = True
inp_num = None
inp_ch = None
while True:
    if wait_for_number:
        try:
            inp_try = input(">>> ")
            inp_num = int(inp_try)

            if (result == None) :
                result = float(inp_num)
            else:
                operand = float(inp_num)

                if (operator=="+"):
                    result = result + operand
                elif (operator=="-"):
                    result = result - operand
                elif (operator=="*"):
                    result = result * operand
                elif (operator=="/"):
                    result = result / operand
                operator = None
            wait_for_number = False
            inp_num = None
        except ValueError:
            print(f"'{inp_ch}' is not a number. Try again.") 
            inp_try = None
            continue    
    else:
        inp_ch = input(">>> ")
        operator = None
        if (inp_ch=="+") or (inp_ch=="-") or (inp_ch=="*") or (inp_ch=="/"):
            operator = inp_ch
            wait_for_number = True
            inp_ch = None
        elif (inp_ch=="="):
            print ('Result: ' + str(float(result)) )
            result = None
            operand = None
            operator = None
            wait_for_number = True
            inp_ch = None
        else:
            print(f"{inp_ch} is not '+' or '-' or '*' or '/' or '=' . Try again") 
            wait_for_number = False
            inp_ch = None

#Перша: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "], результат 18.0
#Друга: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0
