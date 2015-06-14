import random
import os

def getUserScore(userName):
	try:	
		read = open('userScores.txt', 'r')
		content = []
		for line in read:
			content.append(line.split(', '))
		read.close()
	
		for item in content:
			if item[0] == userName:
				return item[1]
		return -1
	
	except IOError:
		fileNotFound()

def updateUserPoints(newUser, userName, score):
	if newUser:
		try:
			add = open('userScores.txt', 'a')
			add.write(userName + ', ' + score)
			add.close()
		except IOError:
			fileNotFound()

	else:
		try:
			modify = open('userScores.tmp', 'w')
			read = open('userScores.txt', 'r')
		
			for line in read:
				splice = line.split(', ')
				if splice[0] == userName:
					modify.write(userName + ', ' + score + '\n')
				else:
					modify.write(line)
		
			modify.close()
			read.close()
		
			os.remove('userScores.txt')
			os.rename('userScores.tmp', 'userScores.txt')
		except IOError:
			fileNotFound()
			
def generateQuestion():
	operandList, operatorList = [0,0,0,0,0], ['','','','']
	operatorDict = {1:"+", 2:"-", 3:"*", 4:"/", 5:"**"}

	for operand in range(len(operandList)):
		operandList[operand] = random.randint(1, 9)

	for operator in range(len(operatorList)):
		operatorList[operator] = operatorDict[random.randint(1, 5)]
		if operator > 0:
			if operatorList[operator] == operatorList[operator-1]:
				operatorList[operator] = operatorDict[random.randint(1, 4)]
			
	questionString = ''
	for number in range(len(operandList)):
		if number == len(operandList)-1 :
			questionString += str(operandList[number])
		else:
			questionString += str(operandList[number]) + operatorList[number]

	result = eval(questionString)

	#Display question
	questionString = questionString.replace('**','^')
	print('What is the result of ' + questionString + ' ?'
	'(round your answer)')
	userAnswer = input()

	try:
		if(round(int(userAnswer)) == round(result)):
			print('Keep it up!')
			return 1
		else:
			print('correct anser is: ' + str(result))
			return 0
	except Exception as e:
		print(e)
		print('\nYou must type a number')
	
def fileNotFound():
	print('File not found, creating file')
	create = open('userScores.txt', 'w')
	create.close()
