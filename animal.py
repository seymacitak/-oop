import time 

class Animal():
    def __init__(self, name, lifespan, class_type, weight, age, nutrition ): 
        print("init function of animal class")
        self.name = name
        self.lifespan = lifespan
        self.class_type = class_type
        self.weight = weight
        self.age = age
        self.nutrition = nutrition 

    def information(self):
        print("information of the animal class..")
        time.sleep(1)
        print("Name: {} \nLifespan: {} \nClass type: {}\nWeight: {} \nAge: {}\nNutrition type: {}".format(self.name,self.lifespan,self.class_type,self.weight,self.age,self.nutrition))










