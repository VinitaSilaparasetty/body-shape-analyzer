bust = input("Enter the measurement of your bust  : ")  
waist = input("Enter the measurement of your waist : ") 
hips = input("Enter the measurement of your hips : ") 

if ((bust-hips) <= 1 and (hips-bust) < 3.6 and (bust-waist) >= 9 or (hips-waist) >= 10):
      print ("Your body type is Hourglass")
elif ((hips-bust) >= 3.6 and (hips-bust) < 10 and (hips-waist) >= 9 and (hip/waist) < 1.193 ):
      print ("Your body type is Bottom Hourglass")
elif ((bust-hips) > 1 and (bust-hips) < 10 and (bust-waist) >= 9):
      print ("Your body type is Top Hourglass")
elif ((hips-bust) > 2 and (hips-waist) >= 7 and (hip/waist) >= 1.193):  
      print ("Your body type is Spoon")
elif ((hips-bust) >= 3.6 and (hips-waist) < 9):
      print ("Your body type is Triangle")
elif ((bust-hips) >= 3.6 and (bust-waist) < 9): 
      print ("Your body type is Inverted Triangle")
elif ((hips-bust) < 3.6 and (bust-hips) < 3.6 and (bust-waist) < 9 and (hips-waist) < 10):
      print ("Your body type is Rectangle")
else:
      print ("Error. Undefined body type.")
