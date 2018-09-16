mylist = ['Hey', 'there', 'I', 'am', 'amazing!']
mydict = {}

for word in mylist:
    mydict[word] = len(word)

uinput = input("Please enter a word: ")
if uinput in mydict:
    input_val = mydict[uinput]
    print('the word "{}" is len {}'.format(uinput, input_val))
else:
    print('the word "{}" does not '.format(uinput))
    print('exist in the dictionary')

