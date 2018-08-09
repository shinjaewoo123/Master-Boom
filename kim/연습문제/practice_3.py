# 3.1
year_list = [1980,1981,1982,1983,1984] 

# 3.2
print(year_list[2]) 

# 3.3
print(year_list[-1]) 

# 3.4
things = ["mozzarella", "cinderella", "salmonella"] 

# 3.5
print(things[1].capitalize())
print(things) 

# 3.6
print(things[0].upper()) 

# 3.7
things.remove("salmonella")
print(things) 

# 3.8
surprise = ["Groucho", "Chico", "Harpo"]

# 3.9
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()
print(surprise[-1])

# 3.10
e2f = {'dog':'chien','cat':'chat','walrus':'morse'}

# 3.11
print(e2f['walrus'])

# 3.12
f2e = {}
for eng, fre in e2f.items():
	f2e[fre] = eng
print(f2e)

# 3.13
print(f2e['chien'])

# 3.14
print(e2f.keys())

# 3.15
life = {
	'animals':
	{
		'cats':['Henri', 'Grumpy', 'Lucy'],
		'octopi': {},
		'emus': {}
	},
	'plants': {},
	'other': {}
}

print(life)

# 3.16
print(life.keys())

# 3.17
print(life['animals'].keys())

# 3.18
print(life['animals']['cats'])
