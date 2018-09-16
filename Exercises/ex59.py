mylist = ['Hey', 'there', 'I', 'am', 'amazing!']
mydict = {}

for word in mylist:
    mydict[word] = len(word)

uinput = input("Please enter a word: ")

input_val = mydict[uinput]
print('the word "{}" is len {}'.format(uinput, input_val))

