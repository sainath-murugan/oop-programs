import random
class Greather(BaseException):
    def __init__(self, number, greather = "enter a number greather than 0"):
        self.salary = number
        self.greather_than_0 = greather
        super().__init__(self.greather_than_0)

class Lesser(BaseException):
      def __init__(self,number,lesser = "enter a number less than 10"):
         self.number = number
         self.lesser_than_10 = lesser
         super().__init__(self.lesser_than_10)


random_number = random.randint(0,10)
while True:

    try:
        number = int(input())
        if number == random_number:
          print("you win")
          break
        elif number < 0 :
           raise Greather(number)
        elif number > 10:
            raise Lesser(number)
        else:
            print("your guessing is wrong try again")

    except ValueError as error:
        print(f"it is {error.__class__}")






