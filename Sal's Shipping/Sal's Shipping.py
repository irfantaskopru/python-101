weight = 1.5

#Ground Shipping Cost
if weight <= 2 :
  cost = weight * 1.5 + 20
elif weight <= 6:
  cost = weight * 3 + 20 
elif weight <= 10:
  cost = weight * 4 + 20 
else:
  cost = weight * 4.75 + 20 
print("Ground shipping cost",cost)

#Ground Shipping Premium Cost
ground_shipping_premium_cost = 125

print("Ground shipping premium cost:",ground_shipping_premium_cost)

#Drone Shipping Cost

if weight <= 2 :
  cost = weight * 4.5
elif (weight > 2) and (weight <= 6):
  cost = weight * 9 
elif (weight > 6) and (weight <= 10):
  cost = weight * 12
else:
  cost = weight * 14.25 
print("Drone shipping cost",cost)



