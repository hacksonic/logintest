pw = 'a123456'
num = 3 #times

print('Please enter your password, you have 3 times chance')


while True:
    input_pw = input('Password:')
    if input_pw == pw:
        print('Login successful')
        break
    else:
        num = num -1
        print('Fail, please try again, you still have', num, 'times')
        if num == 0:
            print('Your IP was banned')
            break