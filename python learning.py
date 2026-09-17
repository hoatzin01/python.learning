message_1 = "reseach and analysis wing"
print (message_1)
print(55-47)
print(67+238)
question = "who wrote bhagwad geeta"
answer = "ved vyas"
print(question)
print(answer)
print(message_1,question,answer)
who = 'i stole my owe watch'
print(who)
who = "myself"
print(who)

#title,upper,lowercases.
question = "who the hell are you suppose to be"
answer = "i m vengence"
print(question, answer. title())
print(question, answer. upper())
print(question, answer. lower())
print(question, answer. capitalize()) 
first_name = "narendra"
middle_name = "damodar das"
last_name = "modi"
age = "75"
post = "prime minister of india"
full_details = f"{first_name}  {middle_name}  {last_name}  {age}  {post}"
print(full_details)
print(f"namste {full_details.title()}+")
message_2 = f"namste,  {full_details.title()}+"
print(message_2)
print(message_1)
print(message_2)
print(message_1, message_2 + post)

#paras.
print("asia")
print("\tBRICS")
print("BRICS: \nbrazil \nRUSSIA \nIndia \nchina \nsouth africa")

#left,rightstrip.
favorite_language = 'hindi  '
print(repr(favorite_language))
print(repr(favorite_language.rstrip()))
print(repr(favorite_language))
favorite_language = 'hindi  '
favorite_language =  favorite_language.rstrip()
print(repr(favorite_language))

print(repr(favorite_language))

who_you = "  bruce wayne  "
print(repr(who_you))
print(repr(who_you.rstrip()))
print(repr(who_you.lstrip()))
print(repr(who_you.strip()))
print(repr(who_you))

who_you = who_you.strip()
print(repr(who_you))

#removing
safeexit_url = 'https://safeexit.com'
print(safeexit_url.removeprefix('https://'))
finance_notes = "files_notes.txt"

#understand numbers.
print(finance_notes.removesuffix('txt'))
print(2*9)
print(8/1)
print(9-5)
print(52+76)

print(3**6)
print(5**6)
print(0.5+5.9)
print(1+7.8)
elon_musk_worth = 1_000_0000_000_000_00
print(elon_musk_worth)


#say hello to everyone.
print("hello devs wassupp")

#chapter 3
places = [ 'delhi  ', 'banaras', 'patna' ]
print(places)
print(repr(places[0].rstrip()))
print(places[0].title())
print(places[-2])
print(places[0])
print(places[1])

print(places[0].upper())

mesage_3 = f"i've studied in {places[0].upper()}"
print(mesage_3)

motorcycles = ['honda', 'yamaha', 'ducati']
print(motorcycles)

motorcycles[0] = 'suzuki'
print(motorcycles)

cars = ['alfa', 'lambo', 'gtr', 'bugatti', 'benz']
print(cars)
cars[0] = 'ferrari'
cars[1] = 'genesis'
print(cars)
cars.insert(1, 'gm')
print(cars)

prints = ['myself']
prints.insert(0,'yourself')
print(prints)

del cars[1]
del motorcycles[0]
print(cars)
print(motorcycles)
del prints[1]
print(prints)
popped_cars = cars.pop()
print(cars)
print(popped_cars)
last_owned = cars.pop()
print(f"my last owned car was {last_owned.title()}.")
first_owned = cars.pop(0)
print(f"my first owned car was {first_owned.title()}.")

cars_2 = ['hyundai','kia','tata','mahindra']
print(cars_2)
cars_2.remove('kia')
print(cars_2)
cars.remove('gtr')
print(cars)
too_weak = 'hyundai'
cars_2.remove(too_weak)
print(cars_2)
print(f"\nA {too_weak.title()} have too weak build")
print(cars_2)
#did it alone.
guest_list = ['amisha', 'raja', 'sadhna']
print(f"you r invited in party {guest_list [0]}.")
print(f"{guest_list[-1]} will not be there in party.")
guest_list.remove('sadhna')
print(guest_list)
print(f"we lost our one member to party but {guest_list}  are most invited in today's dinner party")
guest_list.insert(0, 'suhani')
guest_list.insert(2, 'tannu')
guest_list.append('sakshi')
print(guest_list)
print(f"\n{guest_list[0]} you are most invited in today's dinner party")
print(f"\n{guest_list[1]} you are most invited in today's dinner party")
print(f"\n{guest_list[2]} you are most invited in today's dinner party")
print(f"\n{guest_list[3]} you are most invited in today's dinner party")
print(f"\n{guest_list[-1]} you are most invited in today's dinner party")

print(f"{guest_list} \n due to sudden table cancelation i won'tbe able to invite everyone, but i m inviting {guest_list[1]} and {guest_list[2]}.")
popped_guest_list = guest_list.pop(0)
popped_guest_list = guest_list.pop(-1)
popped_guest_list = guest_list.pop()
print(guest_list)
print(f"\n{guest_list[0]} \nand \n{guest_list[1]} \nyou are still invited")
del guest_list[1]
del guest_list[0]

subject = ['maths', 'hindi', 'physics', 'chemistry', 'biology']
subject.sort()
print(subject)
subject.sort(reverse=True)
print(subject)

print("her's the original list:")
print(subject)

print("\nhere's the sorted list:")
print(sorted(subject))
print("\nhere's the original  list again: ")
print(subject)
subject.reverse()
print(subject)
subject.reverse()
print(subject)
len(subject) 
print(len(subject))

vacations = ['monaco', 'switzerland', 'amazon rainforest', 'tanzania', 'italy' ]
print(vacations)
print("here's  the sorted list:")
print(sorted(vacations))
print(sorted(vacations, reverse=True))
print(vacations)
vacations.reverse()
print(vacations)
vacations.reverse()
print(vacations)
vacations.sort()
print(vacations)
vacations.sort(reverse=True)
print(vacations)
len(guest_list)
print(len(guest_list))

#print(variable[]),.title(),f", .append, .insert, del, .pop
#accesing elements in list.
randoms = ['everest','pacific','modi','switzerland','lenovo','ganga','tokyo','french','australia']
print(randoms[1]) 
print(randoms[3].title())
print(randoms[0].upper())
print(randoms[0].lower())
#index position
print(randoms[-2])
#individual values
message = f"i wanna go to {randoms[3].title()} trip."
print(message)
#modifying element in a list
print(randoms)
randoms[-1] = 'europe'
print(randoms)
#adding elements
randoms.append('italy')
print(randoms)
#.insert
randoms.insert(0, 'ruler')
print(randoms)
#pop, de4l
popped_randoms = randoms.pop()
print(randoms)
print(popped_randoms)
del randoms[0]
print(randoms)
last_trip = randoms.pop(3)
print(f"{last_trip} was my last trip.")
randoms.remove('lenovo')
print(randoms)
ocean = 'pacific'
randoms.remove(ocean)
print(randoms)
#sort
print(sorted(randoms))
print(randoms)
randoms.reverse()
print(randoms) 
len(randoms)
print(len(randoms))

magicians = ['alice','david','vincy','victor']
for magician in magicians:
       print(f"{magician.title()} you did great job")
       print(f"i can't wait to see your next trick {magician.title()} \n")


