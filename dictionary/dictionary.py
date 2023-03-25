songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Dict comprehension to create a dictionary from two lists
plays = {song:count for song,count in zip(songs,playcounts)}

#Add elements to a dictionary
plays["Purple Haze"] = 1

#Update elements in a dictionary
plays.update({"Respect":94})

#create a dictionary
library = {"The Best Songs" : plays,
"Sunday Feelings" : {}}

print(library)