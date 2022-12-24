"""To master yield, you must understand that when you call the function, 
the code you have written in the function body does not run.
The function only returns the generator object, this is a bit tricky :-)
Then, your code will be run each time the "for" uses the generator.

Now the hard part:
The first time the for calls the generator object created from your function,
it will run the code in your function from the beginning until it hits yield, 
then it'll return the first value of the loop. 
Then, each other call will run the loop you have written in the function one more time, 
and return the next value, until there is no value to return.

The generator is considered empty once the function runs but does not hit yield anymore. 
It can be because the loop had come to an end, or because you do not satisfy a "if/else" anymore.
"""

# print __doc__
myGenerator = (x*x for x in range(3))
for i in myGenerator:
	print i

for j in myGenerator:
	print j

def createGenerator():
	myList = range(3)
	print "Son"
	# for i in myList:
	# 	yield i*i
	init = 0
	while True:
		init = init + 1
		yield init

print "\n========"
gener = createGenerator()
print(gener)

for k in range(3):
	print gener.next()

for h in range(3):
	print gener.next()

class Bank():
	crisis = False
	def createATM(self):
		n = 99
		while not self.crisis:
			n = n + 1
			yield "$%s" % n

hsbc = Bank()
cornerStreetATM = hsbc.createATM()
print cornerStreetATM.next()
print cornerStreetATM.next()
print [cornerStreetATM.next() for cash in range(5)]

hsbc.crisis = True
try:
	print cornerStreetATM.next()
except Exception as ex:
	print "Exception: %s" % type(ex)

wallStreetATM = hsbc.createATM()

try:
	print wallStreetATM.next()
except Exception as ex:
	print "Exception: %s" % type(ex)

hsbc.crisis = False

try:
	print cornerStreetATM.next()
except Exception as ex:
	print "Exception: %s" % type(ex)

brandNewATM = hsbc.createATM()

for i in range(3):
	print brandNewATM.next()

for j in range(3):
	print brandNewATM.next()