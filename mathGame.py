try:
	import myPythonFunctions as mpf

	print('What is your name: ')
	userName = input()
	userScore = int(mpf.getUserScore(userName))
	newUser = userScore == -1
	
	if newUser:
		userScore = 0
		
	userChoice = 0
	
	while userChoice != '-1':
		userScore += mpf.generateQuestion()
		print('Continue? (type -1 to exit)')
		userChoice = input()
		
	mpf.updateUserPoints(newUser, userName, str(userScore))
except Exception as e:
	print(e)
