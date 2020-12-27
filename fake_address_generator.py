import random

for i in range(100):
 class Fake_address:

  def __init__(self,first_name, last_name, state, city):
     self.first_name = first_name
     self.last_name = last_name
     self.state = state
     self.city = city

  def random_name(self):
    return random.choice(self.first_name)
  def random_last_name(self):
     return random.choice(self.last_name)
  def random_state(self):
     return random.choice(self.state)
  def random_city(self):
     return random.choice(self.state)

  def phone_number(self):
      return random.randint(0000000000,9999999999)
  def email_address(self):
      return random.choice(self.first_name) + str(random.randint(20, 999)) + "@gmail.com"

  def pin_code(self):
      return random.randint(0000000,9999999)


 s1 =Fake_address(
 ["Sai", "Ram", "Hari", "Baskar", "Ajay", "Aswin", "Geo", "Ravi", "Aravind", "Mike", "Joe", "David", "Rockie","Naasar","Vishnu"],
 ["krishna", "balaram", "johar", "Muthu", "Sagar", "Anyhony", "kumar", "Risha", "periyassamy", "enniya", "Manu", "radha"],
 ["Ariyalur","Chengalpattu","Kallakurichi","Kanchipuram","Kanyakumari","Karur","Krishnagiri","Madurai","Nagapattinam","Namakkal",
 "Nilgiris","Perambalur","Pudukkottai","Ramanathapuram","Ranipet","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode",],
 ["Kodungaiyur (West)","Kodungaiyur (East)","Dr.Radhakrishnan Nagar (North)","Cherian Nagar (North)","Jeeva Nagar (North)","Cherian Nagar (South)","Jeeva Nagar (South)","Korukupet","Mottai Thottam",
 "Kumaraswamy Nagar (South)", "Dr.Radhakrishnan Nagar (South)", "Kumaraswamy Nagar (North)",	"Dr. Vijayaraghavalu Nagar", "Tondiarpet", "Sanjeevarayanpet",
 "Old Washermenpet","Meenakshiammanpet","Kondithope","Seven Wells (North)","Amman Koil","Muthialpet","Vallal Seethakadhi Nagar",	"Katchaleeswarar Nagar",])
 
 
 print(f"Name:{s1.random_name()} {s1.random_last_name()}\n phone number:{s1.phone_number()}\n address:{s1.random_city()},{s1.random_state()}\n pincode: {s1.pin_code()}\n Email:{s1.email_address()}\n\n")

