'''
You are an event organiser. Your client has a list of VIP 
guests for their event. Write a program that creates this 
guest list. Ask the client how many VIPs will be there. 
Each time you ask the user for a guest name, 
you should write these details into a file, with each entry 
on a new a line.
'''

num_vips = int(input("How many VIPs will be attending? "))

with open('event_guest_list.txt', 'w') as file:

    for i in range(num_vips):       # Also: for _ in range(num_vips):
        name = input("Enter guest name: ")
        file.write(f"{name}\n")




