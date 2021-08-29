guest_list = ['Dylan', 'Haley', 'Steve', 'Rick']
print('Come to the party, ' + guest_list[0])
print('You should come too ' + guest_list[1])
print(guest_list[2] + ' and ' + guest_list[3] + ' will be there.')
print(guest_list)
print('The number of people on the guest list is ' + str(len(guest_list)))

print()

print(guest_list[2] + ' can no longer make it.')
guest_list.remove('Steve')
print('I will invite Matt instead.')
guest_list.append('Matt')
print(guest_list)
print('The number of people on the guest list is ' + str(len(guest_list)))

print()

print('We found a bigger table! Inviting Sam, Chris, and Joe.')
guest_list.insert(0, 'Sam')
guest_list.insert(3, 'Chris')
guest_list.append('Joe')
print(guest_list)
print('The number of people on the guest list is ' + str(len(guest_list)))

print()

print("Whoops, nevermind we lost the big table. Some of you can't come")
removed = guest_list.pop()
print("Sorry " + removed + ", you can no longer come.")
removed = guest_list.pop()
print("Sorry " + removed + ", you can no longer come.")
removed = guest_list.pop(0)
print("Sorry " + removed + ", you can no longer come.")
removed = guest_list.pop(2)
print("Sorry " + removed + ", you can no longer come.")

print()

print("The final guest list is: " + str(guest_list))
print("The final guest list is: " + guest_list[0] + ", " + guest_list[1] + ", and " + guest_list[2] + ".")
print('The number of people on the guest list is ' + str(len(guest_list)))

print()

del guest_list[2]
del guest_list[1]
del guest_list[0]
print(guest_list)
print('The number of people on the guest list is ' + str(len(guest_list)))
