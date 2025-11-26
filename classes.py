from server import assignWithCsv

class Soldier:
    def __init__(self, soldier_number, first_name, last_name, gender, city, distance):
        self.soldier_number = soldier_number
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city = city
        self.distance = distance
    
soldiers = []
for i in 