#Averaging Algorithm Python Module
average=0
total=0
how_many_entered=0
print ('How many test score would you like to average?')
how_many = int(input(''))
print('Enter Test Score')
test_score = int(input(''))
total = total + test_score
how_many_entered= how_many_entered + 1
while how_many_entered < how_many:
	print('Enter Test Score')
	test_score = int(input(''))
	total = total + test_score
	how_many_entered= how_many_entered + 1
average = total/how_many
print('The average for the test scores you entered is:')
print(average)
