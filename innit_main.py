# class car:
#     def __init__(self, car_name, car_color, car_stripes):
#         self.name = car_name
#         self.color = car_color
#         self.stripes = car_stripes

# Bugatti = car("Bugatti Divo","Black","Blue")
# McLaren = car("McLaren 765LT","Orange","no stripes")

# # print(Bugatti.name, Bugatti.color)
# print(f"I have a {Bugatti.color} color {Bugatti.name} and it has {Bugatti.stripes} stripes on it.")
# print(f"I have a beautifull {McLaren.name} and it is {McLaren.color} in color.")


class Jet:
    def __init__(self, Company, Model, Capacity, Airline):
        self.jet_company = Company
        self.jet_model = Model
        self.jet_capacity = Capacity
        self.jet_airline = Airline


Jet1 = Jet("Boeing", 777, 180, "Air India")
Jet2 = Jet("Airbus", "A380", 250, "Emirates")
Jet3 = Jet("Boeing", 787, 300, "Etihad")

flist1 = [Jet1.jet_company, Jet1.jet_model, Jet1.jet_capacity, Jet1.jet_airline]
flight_no = int(input("Enter your flight number : "))
if flight_no >= 1000 and flight_no <= 2000:
    print("Jet Details")
    for i in flist1:
        print(i)
