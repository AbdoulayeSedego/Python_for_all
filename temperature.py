question = int(input("""Choose (1) to convert to fahrenheit and 
	                (2) to convert to celsius \n"""))
if question == 1:
	user_input = float(input("Enter temperature in celsius >"))
	result = (user_input * 9/5 ) + 32
	print(result)

if question == 2:
	user_input = float(input("Enter temperature in fahrenheit >"))
	result = (user_input - 32 ) * 5/9
	print(result)
