"""
Preserve the Verse has one task for you. They have delivered you a string that contains a list of poems, titled highlighted_poems, they want to highlight on the site, but they need your help to parse the string into something that can display the name, title, and publication date of the highlighted poems on the site.
"""
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

"""The information for each poem is separated by commas, and within this information is the title of the poem, the author, and the date of publication."""

highlighted_poems_list = highlighted_poems.split(",")

#Notice that there is inconsistent whitespace in highlighted_poems_list. Let’s clean that up

highlighted_poems_stripped = [i.strip(" ") for i in highlighted_poems_list]

#Next we want to break up all the information for each poem into it’s own list, so we end up with a list of lists.

highlighted_poems_details = [i.split(":") for i in highlighted_poems_stripped]

#Great! Now we want to separate out all of the titles, the poets, and the publication dates into their own lists.

titles = []
poets = []
dates = []

for i in highlighted_poems_details:
    print(i)
    titles.append(i[0])
    poets.append(i[1])
    dates.append(i[2])

"""
Finally, write a for loop that uses .format() to print out the following string for each poem:
The poem TITLE was published by POET in DATE.
"""

for i,j,k in zip(titles,poets,dates):
    print("The poem {} was published by {} in {}.".format(i,j,k))