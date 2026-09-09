#to avoid working directory issues, download the folder "deliverable2Theo",
#open VSC and click "Open Folder"--> Open the "deliverable2Theo" folder

import math  #this imports math such as the square root
from pathlib import Path  #locates the file together with the script

def main():  #our main funtion
      file_path = Path(__file__).parent / "output-Set0.txt" #path to text file
      with open(file_path, "r") as file:  #opening the text file
            lines = file.readlines()  #letting python read the file line by line
      for line in lines [1:]:  #this makes sure every line is read except for line 1
            values = line.split()  #this splits each line into seperate values
      
            x = float(values[0])   #here we assign the values to variables xyz and the id
            y = float(values[1])
            z = float(values[2])
            molec_id = int(values[3])
            result = momentum(x, y, z)  #calling the result of the momentum function and defining it
            if result is not None:   #if the result is valid, print this
                  print(f"#ID: {molec_id} Total Momentum: {result}")
            else:
                  print("All variables are equal to zero.")  #for an invalid return (000) of the momentum function
             #the first entry of the text file was changed to 0, 0, 0 to test this     

def momentum(x, y, z):   #defining the momentum fucntion
      if x == 0 and y == 0 and z == 0:  #if all values are zero, the functions returns None
            return None
      else:
            return math.sqrt(x**2 + y**2 + z**2)  #returns the suqare root calculation

         

main()  #calling the main function