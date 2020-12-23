#reverse a word using oop

class reverse_sentence:

     def __init__(self, word):
         self.word = word

     def reverse(self):
         return "".join(list(reversed(self.word)))
    

constructor_1 = reverse_sentence(input("enter the word"))

print(constructor_1.reverse())

