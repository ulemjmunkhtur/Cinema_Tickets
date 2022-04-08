#asking for basic information from the user 
print('Welcome to Prime Cineplex Encanto')
name = input ('What is your name? ')
phone_number = input('What is your phone number? ')
#validate phone number#

#revealing the 3 different movie options 
print("These are today's movies")
movies = ['Encanto','Forrest Gump', 'Avatar the Last Airbender']

#shows the movie options by enumerating the list. 
for count, movie in enumerate(movies):
    print (f"{count + 1}. {movie}")
#the user needs to select a movie, so movie_selection starts off as none. 
movie_selection = None
#validating that the user chose a movie from the 3 different options with try and except 
while movie_selection not in range(1,4):
    try: 
        movie_selection = int(input('Please, enter your choice of movie from 1-3: '))
    except:
        print ("Nope")
#printing the movie_selection with the correct number (because the user does it in human numbers and this is code) 
print('you have chosen', movies[movie_selection-1])
#asking the user to choose which out of the three sessions they would like to watch the movie in 
session = input(f"Which session would you like to watch {movies[movie_selection-1]} in? Morning, Afternoon, or Evening?")
print("you chose the", session, "session")

#MATCH SESSION TO LOWERCASE OR UPPERCASE. lOWERCASE WITH THE KEY 

print("Okay. You have chosen to watch", movies[movie_selection-1])
