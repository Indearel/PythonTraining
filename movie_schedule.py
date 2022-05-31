current_movies = {'Top Gun: Maverick':'11:00am',
                  'Doctor Strange in the Multiverse of Madness': '1:00pm',
                  'Jurrasic World Dominion': '3:00pm',
                  'Infinite Storm':'5:00'}

print("We are currently showning follownig movies:")
for key in current_movies:
    print(key)

movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("Chosen movie is not displayed currently in the Cinema")
else:
    print(movie, 'is displayed at', showtime)