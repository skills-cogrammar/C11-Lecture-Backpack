'''
You are an event organiser. You have a file with 
the names of people you work with and the service
they offer. Our goal is to read the file and 
display the services offered by the people in your
contact list.
'''

with open('event_items.txt', 'r') as file:
    lines = file.readlines() 
    # print(lines) # just checking the contents of lines

# Initialise list for services
services = []

for line in lines:
    # for first iteration line = 'Sarah Baker: Catering\n'
    stripped = line.strip("\n").split()

    # stripped = ['Sarah', 'Baker:', 'Catering']
    services.append(stripped[-1])

# print(services)

for item in services:
    print(item)
    
'''
Just showing how we can use the split method
in another way to complete this task.
'''

with open('event_items.txt', 'r') as file:
    lines = file.readlines() 
    # print(lines) # just checking the contents of lines

# Initialise list for services
services = []

for line in lines:
    # for first iteration line = 'Sarah Baker: Catering\n'
    name, service = line.strip("\n").split(': ')

    # stripped = ['Sarah', 'Baker:', 'Catering']
    services.append(service.strip()) # get rid of leading white spaces

print(services)

'''
for item in services:
    print(item)
'''    




