#asking for basic information from the user 
print('Welcome to Prime Cineplex Encanto')
name = input ('What is your name? ')
isInvalidPhone = True
while isInvalidPhone:
    try: 
        phone = (input("what is your phone number in the format ????-?????????  "))
        if len(phone) != 14:
            print("Are you sure?")
            continue
        phoneParts = phone.split('-')
        if len(phoneParts[0]) != 4 or type(int(phoneParts[0])) != int:
            print("Are you sure?")
            continue
        elif len(phoneParts[1]) != 9 or type(int(phoneParts[1])) != int:
            print("Are you sure?")
            continue
    except ValueError:
            print("Are you sure?")
            continue
    isInvalidPhone = False


#revealing the 3 different movie options 
print("These are today's movies")
movies = [
        ['Encanto', [
                ['Morning', 
                 [1,2,3,4,5,6,7,8,9,10,'x',12,13,14,15]
                ],
                ['Afternoon', 
                 [1,2,3,4,5,6,'x',8,9,10,'x',12,13,14,15]
                ],
                ['Evening', 
                 [1,2,3,4,5,6,'x',8,9,10,11,12,13,14,15]
                ]
            ]
        ],
        ['Forrest Gump', [
                ['Morning', 
                 [1,2,3,4,5,'x',7,8,9,10,'x',12,13,'x',15]
                ],
                ['Afternoon', 
                 [1,2,3,4,5,6,'x',8,9,10,'x',12,13,14,15]
                ],
                ['Evening', 
                 [1,2,3,4,5,6,'x',8,9,10,11,'x',13,14,15]
                ]
            ]
        ],
        ['Avatar the last airbender', [
                ['Morning', 
                 [1,2,3,4,5,'x',7,'x',9,'x','x',12,'x',14,15]
                ],
                ['Afternoon', 
                 [1,2,3,4,5,6,'x',8,9,10,'x',12,13,'x','x']
                ],
                ['Evening', 
                 [1,2,'x',4,5,'x','x',8,9,'x',11,'x',13,'x','x']
                ]
            ]
        ],
    ]

#shows the movie options by enumerating the list. 
for count, movie in enumerate(movies):
    print (f"{count + 1}. {movie[0]}")
#the user needs to select a movie, so movie_selection starts off as none. 
movie_selection = None
#validating that the user chose a movie from the 3 different options with try and except 
while movie_selection not in range(1,4):
    try: 
        movie_selection = int(input('Please, enter your choice of movie from 1-3: '))
    except:
        print ("Nope")
#printing the movie_selection with the correct number (because the user does it in human numbers and this is code) 
smovie = movies[movie_selection-1]
print('you have chosen', smovie[0])
#asking the user to choose which out of the three sessions they would like to watch the movie in 
session_selection = None
while session_selection not in range(1,4):
    try: 
        session_selection = int(input(f"Which session would you like to watch {smovie[0]} in?  1) Morning, 2) Afternoon, or 3) Evening? please enter 1, 2 or 3 \n"))
    except:
        print ("Nope")
ssession = smovie[1][session_selection-1]
print("you chose the", ssession[0], "session")

#printing it in rows of 5
def print_movie_selection(ssession, smovie):
    print(f"{ssession[0]} session: {smovie[0]}")
    print("---------------------")
    seat_number = 0
    for seat in ssession[1]:
        seat_number += 1
        print(f"[{seat}]", end =" ")
        if seat_number % 5 == 0:
            print('\n')
        
#asking for the seat
seat_selection = None
while seat_selection not in range(1, 16):
    try:
        print_movie_selection(ssession, smovie)
        seat_selection = int(ssession[1][int(input(f"Which seat would you like to choose? X's are aleady taken. Please choose from the available seats 1-15 \n"))-1])
    except:
        print ("Nope")
print(f"Okay. You have chosen to watch {smovie[0]} in the {ssession[0]}, seat {ssession[1][seat_selection-1]}", )
#using a dictionary 
soda_dict = {"Coca Cola": 2, "Pepsi": 3, "Mountain Dew": 1}
soda_selection = "l"
while soda_selection not in soda_dict:
    try:
        soda_selection = input(f"Choose a soda. Coca Cola: 2, Pepsi: 3, Mountain Dew: 1    ")
    except:
        print ("Nope")

match soda_selection:
    case "Coca Cola": print("You have ordered")
    case "Pepsi": print("You have ordered")
    case "Mountain Dew": print("You have ordered")
    case _ : print("other error")

confirmation = input('Is all this information correct. Would you like to book again Y or N \n')




