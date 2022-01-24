#Use of this page is optional. If you use code here, make sure either import page4 or from page4 import * appear on your main.py page.

Name = input("Enter a surname: ")
Noun1 = input("Enter a noun: ")
place = input("Enter a place: ")
Adj1 = input("Enter an adjective: ")
Noun2 = input("Enter a noun: ")
Adj2 = input("Enter another adjective: ")
Adj3 = input("Enter another adjective: ")
Adj4 = input("Enter another adjective: ")
Adj5 = input("Enter another adjective: ")
Adj6 = input("Enter another adjective: ")
number = input("Enter a number: ")
adverb = input("Enter an adverb: ")
Name2 = input("Enter another surname: ")
Noun3 = input("Enter a noun: ")
Noun4 = input("Enter a plural noun: ")
sentence1 = 'Mr. and Mrs. ' + Name + ', of number ' + number + ', ' + place + ', were '+ Adj1 + ' to say that they were ' + adverb + ' ' + Adj2 + ', thank you very much. '
sentence2 = 'They were the last people you’d expect to be involved in anything ' + Adj3 + ' or ' + Adj4 + ', because they just didn’t hold with such nonsense. '
sentence3 = 'Mr. '+ Name2 + ' was the director of a firm called Grunnings, which made ' + Noun3 + '. '
sentence4 = 'He was a ' + Adj5 + ', ' + Adj6 + ' man with hardly any ' + Noun4 + ', although he did have a very large mustache.'
print(sentence1 + sentence2 + sentence3 + sentence4)