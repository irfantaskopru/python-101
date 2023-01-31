"""
Carly's Clippers
You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

You have been provided with three lists:

hairstyles: the names of the cuts offered at Carly’s Clippers.
prices: the price of each hairstyle in the hairstyles list.
last_week: the number of purchases for each hairstyle type in the last week.
Each index in hairstyles corresponds to an associated index in prices and last_week.

For example, The hairstyle "bouffant" has an associated price of 30 from the prices list, and was purchased 2 times in the last week as shown in the last_week list. Each of these elements are in the first index of their respective lists.

Let’s get started!
"""
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for i in prices:
  total_price += i

average_price = total_price / len(prices)
print(f"Average Haircut Price: {average_price}")

# That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.
new_prices= [i-5 for i in prices]
print("New Prices",new_prices)

#Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.
total_revenue = 0
for i in range(0,len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
print("Total Revenue: ",total_revenue)
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue",average_daily_revenue)

#Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i]<30]
print("Hairstyle under 30 dollars:",cuts_under_30)





