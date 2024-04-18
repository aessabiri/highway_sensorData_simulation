import time
import os
import random

car = "🚗"
taxi = "🚕"
suv = "🚙"
police_car = "🚓"
ambulance = "🚑"
delivery_truck = "🚚"
lorry = "🚛"
no_car = '  '

cars = [taxi, suv, police_car, ambulance, delivery_truck, lorry, car]
road = "" #save the road created 

class HighwaySimulation:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        

    def display_highway(self):
        car_positions = [] # tupel of the distances from the start
        counter = length # used to measure the distance 
        global road 
        for i in range(length):
            left_value = 0
            right_value = 0
            middle_value = 0
            car_left = random.choices([random.choice(cars), no_car], weights=[0.02, 0.98], k=1)[0]
            car_middle = random.choices([random.choice(cars), no_car], weights=[0.05, 0.95], k=1)[0]
            car_right = random.choices([random.choice(cars), no_car], weights=[0.1, 0.9], k=1)[0]
            road += f'#{" " * (self.width)}{car_left}{" " * (self.width)}|{" " * (self.width)}{car_middle}{" " * (self.width)}|{" " * (self.width)}{car_right}{" " * (self.width)}#\n'
            if car_left != no_car:
                left_value = counter
            if car_middle != no_car:
                middle_value = counter
            if car_right != no_car:
                right_value = counter
            car_positions.append((left_value,middle_value,right_value))
            counter -= 1
        
        
        #Generate and print sensor data
       # 
        #print("Sensor Data:", sensor_data)

        return road, car_positions

    def generate_sensor_data(self, car_positions):
        sensor_data = []

        for position in car_positions:
            left_value, middle_value, right_value = position  # Unpack the tuple
            
            if left_value > 30:
                sensor_data.append(("🟢", left_value, "left"))
            elif 15 <= left_value <= 30:
                sensor_data.append(("🟡", left_value, "left"))
            elif 1 <= left_value <= 15:
                sensor_data.append(("🔴", left_value, "left"))

            if middle_value > 30:
                sensor_data.append(("🟢", middle_value, "middle"))
            elif 15 <= middle_value <= 30:
                sensor_data.append(("🟡", middle_value, "middle"))
            elif 1 <= middle_value <= 15:
                sensor_data.append(("🔴", middle_value, "middle"))

            if right_value > 30:
                sensor_data.append(("🟢", right_value, "right"))
            elif 15 <= right_value <= 30:
                sensor_data.append(("🟡", right_value, "right"))
            elif 1 <= right_value <= 15:
                sensor_data.append(("🔴", right_value, "right"))

        return sensor_data

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run_simulation(self):
        self.clear_terminal()
        the_road, car_pos = self.display_highway()
        
      
        for i in range(900):
            self.clear_terminal()
            print(the_road)
            #print(car_pos)
            sensor_data = self.generate_sensor_data(car_pos)
            print (sensor_data)
            print ("Sensor Data Monitor ...")
            for item in sensor_data:
                emoji, value, direction = item  # Unpack the item tuple here
                print(f"{emoji} Value: {value}, Direction: {direction}")



            the_road , pos = self.update_road(the_road)
            car_pos = car_pos + pos
            del car_pos[0]
            car_pos = [tuple(x - 1 if x > 0 else x for x in tpl) for tpl in car_pos]
            
            
           
            time.sleep(0.05)
    

    


    def update_road(self, road):

        car_position = []
        distance = length
        # Split the road into lines
        road_lines = road.split('\n')
        # Remove the last line
        road_lines.pop()
        # Insert a new line at the beginning
        

  
        car_left = random.choices([random.choice(cars), no_car], weights=[0.02, 0.98], k=1)[0]
        car_middle = random.choices([random.choice(cars), no_car], weights=[0.05, 0.95], k=1)[0]
        car_right = random.choices([random.choice(cars), no_car], weights=[0.1, 0.9], k=1)[0]
        road_lines.insert(0,f'#{" " * (self.width)}{car_left}{" " * (self.width)}|{" " * (self.width)}{car_middle}{" " * (self.width)}|{" " * (self.width)}{car_right}{" " * (self.width)}#')
        # Join the lines back into a single string
        updated_road = '\n'.join(road_lines)
        left_value = 0
        right_value = 0
        middle_value = 0
        if car_left != no_car:
                left_value = distance
        if car_middle != no_car:
                middle_value = distance
        if car_right != no_car:
                right_value = distance
        car_position.append((left_value,middle_value,right_value))
        
        return updated_road ,car_position
            

if __name__ == "__main__":
    width = 15
    length = 40
    

    highway_simulation = HighwaySimulation(width, length)
    the_road = highway_simulation.run_simulation()
    
