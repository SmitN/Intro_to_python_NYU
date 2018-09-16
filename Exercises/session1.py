#Session 1 : Excercies
"""
# EX1.1

"""
Assign two new integer objects and one float object to three variable names. 
Sum up the three variables and assign the resulting object to a new variable name. 
Indicate (by printing) the value and type of this resulting object.
"""
var1 = 2
var2 = 5
var3 = 1.2345

result = var1 + var2 + var3
print (result)
print (type ( result ))

#EX1.2
"""
Assign two new integer objects to two variable names. 
Multiply the two variables and assign the resulting object to a new variable name. 
Indicate (by printing) the value and type of this resulting variable's object
"""

ex12_var1 = 10
ex12_var2 = 40

ex12_var3 = ex12_var1 * ex12_var2
print (ex12_var3)
print (type(ex12_var3))

#EX1.3

"""
Starting with the sample code (make sure it is included exactly as written) 
   sum up the values to produce the integer value 15.
   (Hint: apply a conversion function to each string so it can be used as a number.)
"""

ex13_var = '5'
ex13_var2 = '10'

ex13_sum = int(ex13_var) + int(ex13_var2)
print (ex13_sum)
print (type(ex13_sum))

#EX1.4
"""
Take user input for an integer and print that value doubled.
"""

ex14_a= input ('please enter an int value  :')
ex14_b = int(ex14_a)
print(ex14_b)

ex14_c = ex14_b * 2

ex14_d=str(ex14_c)
print(( ex14_a + ' doubled is ' + str(ex14_d) + '.' ))

#EX1.5
"""
Take user input for a 'place' and then greet the place enthusiastically.
"""

ex15_a = input( ' Enter a place you would like to visit  : ')
print ( 'Hello, ' + str(ex15_a) )


#EX1.6
"""
Take user input for an integer and apply that many exclamation points to the phrase,
"Hello, world!" (Hint: use the "string repetition" operator)
"""

ex16_a=input('Enter an Int value ')
ex16_b = len(ex16_a)
ex16_c = '!' * ex16_b
print ( 'Hello, World' + str( ex16_c))


