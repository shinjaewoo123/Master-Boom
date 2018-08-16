# 4.1
guess_me = 7
if guess_me < 7:
	print('too low')
elif guess_me > 7:
	print('too high')
else:
	print('just right')
	
# 4.2
start = 1
while True:
	if guess_me > start:
		print('too low')
	elif guess_me < start:
		print('oops')
	else:
		print('found it!')
		break
	start += 1
	
# 4.3
for x in range(3,-1,-1):
	print(x)
	
# 4.4
num_list = [num for num in range(0,11,2)]
print(num_list)

# 4.5
squares_dic = {num:num*num for num in num_list}
print(squares_dic)

# 4.6
squares_set = {num for num in range(1,11,2)}
print(squares_set)

# 4.7 **
for thing in ('Got %s' % num for num in range(10)):
	print(thing)

# 4.8
def good():
	good_list = ['Harry', 'Ron', 'Hermione']
	return good_list

print(good())

# 4.9
def get_odds():
	for num in range(1, 10, 2):
		yield  num
		
for count, num in enumerate(get_odds(), 1):
	if count == 3:
		print(num)
		break

# 4.10 **
def test(func):
	def new_func(*args, **kwargs):
		print('start')
		result = func(*args, **kwargs)
		print('end')
	return new_func
	
@test
def greeting():
	print("greetings, earthlin")
	
greeting()

# 4.11 **
class OopsException(Exception):
	pass
	
try:
	raise OopsException
except OopsException:
	print('Caught an oops')

# 4.12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles,plots))
print(movies)
