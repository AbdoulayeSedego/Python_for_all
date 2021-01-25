counter = 0
while counter <= 2700:
	if counter%7 == 0 or counter%5 == 0:
		print(counter)

		if counter == 1500:
			print(f"Got the {counter} here")
		if counter == 2700:
			print(f"Got the {counter} here")

	counter += 1