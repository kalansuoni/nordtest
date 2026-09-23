guest_list = ['Teppo Tervanen', 'Taneli Taateli', 'Herra Hai']
del guest_list[2]
guest_list.insert(2, 'Hannu Koivisto')
guest_list.insert(0, 'Tohtori Tommi')
guest_list.insert(1, 'Herra Tiikeri')
guest_list.append('Rouva Kissa')

message = f"Hey, {guest_list[0].title()} I would like to invite you for a tasty selfmade dinner at the bungaloo."
message1 = f"Hey, {guest_list[1].title()} I would like to invite you for a tasty selfmade dinner at the bungaloo."
message2 = f"Hey, {guest_list[2].title()} I would like to invite you for a tasty selfmade dinner at the bungaloo."
message3 = f"Hey, {guest_list[3].title()} I would like to invite you for a tasty selfmade dinner at the bungaloo."
message4 = f"Hey, {guest_list[4].title()} I would like to invite you for a tasty selfmade dinner at the bungaloo."
message5 = f"Hey, {guest_list[5].title()} I would like to invite you for a tasty selfmade dinner at the bungaloo."

removed = guest_list.pop(0)
removed1 = guest_list.pop(1)
removed2 = guest_list.pop(3)
removed3 = guest_list.pop(2)

#print(message)
#print(message1)
#print(message2)
#print(message3)
#print(message4)
#print(message5)

#print(f'{guest_list[2].title()}')



#print('Hey everybody, Unfortunately i can only invite only 2 people to this dinner afterall. All the best.')
#print(f"Hey, {removed} I'm sorry but unfortunately i must withdraw your invite to dinner due to facilitation issues.")
#print(f"Hey, {removed1} I'm sorry but unfortunately i must withdraw your invite to dinner due to facilitation issues.")
#print(f"Hey, {removed2} I'm sorry but unfortunately i must withdraw your invite to dinner due to facilitation issues.")
#print(f"Hey, {removed3} I'm sorry but unfortunately i must withdraw your invite to dinner due to facilitation issues.")
#print(f"Hey, {guest_list[0].title()} you are still invited for dinner.")
#print(f"Hey, {guest_list[1].title()} you are still invited for dinner.")


len(guest_list)
#print(guest_list)
del guest_list[0]
del guest_list[0]
print(guest_list)
