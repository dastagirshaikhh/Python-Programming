def calculator(num1,num2,operation='all'):
    if operation=='add':
        print (num1 + num2)
    elif operation=='sub':
        print (num1 - num2)
    elif operation=='mul':
        print (num1 * num2)
    elif operation=='div':
        print (num1 // num2)
    elif operation=='all':
        print ('addition ',num1+num2)
        print ('subtraction ',num1-num2)
        print ('multiplication', num1*num2)
        print ('division ',num1/num2)
    else:
        print ("Choose the correct option")
calculator(40,10,'all')