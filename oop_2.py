#reverse a word using oop

class reverse_sentence:

     def __init__(self, word):
         self.word = word


     def reverse_a_sentence(self,):
         return " ".join(list(map(str,self.word.split(" ")[::-1])))



constructor_1 = reverse_sentence(input("enter the sentence"))


print((constructor_1.reverse_a_sentence()))
