import time 

class Animal():
    def __init__(self, name, lifespan, class_type, weight, age, nutrition = "no information " ): 
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
        print("Name: {} \nLifespan: {} \nClass type: {}\nWeight: {} \nAge: {}\nNutrition: {}".format(self.name,self.lifespan,self.class_type,self.weight,self.age,self.nutrition))

    def nutrition_type(self):
        print("Nutrition types: \n1. Only meat\n2. Only plants\n3. Both of them")
        animal = input("Choose nutrition type: ")
        if animal == 1:
            print("This animal is a carnivore.")
            form = "Carnivore"
            self.nutrition = format
                
        elif animal == 2:
            print("This animal is a herbivore.")
            form = "Herbivore"
            self.nutrition = form
          
        else:
            print("This animal is a omnivore.")
            form = "Amnivore"
            self.nutrition = form
        

cat= Animal("susi", 33, "fdf", 434,4,)
cat.information()
cat.nutrition_type()
cat.information()





