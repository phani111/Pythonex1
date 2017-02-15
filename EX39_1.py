# create a mapping of state to abbrevation
states = { 'Oregon': 'OR', 'Florida': 'FL', 'California': 'CA', 'New York': 'NY', 'Michigan': 'MI' }

# create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detriot',
    'FL' : 'Jacksonville'
    }

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('_' * 50)
print("NY state has:",cities['NY'])
print("OR state has:",cities['OR'])

#print some stats
print('_' * 50)
print("Michigans abbv is:",states['Michigan'])
print("Floriba Abbrv is:",states['Florida'])

# print every state abrev
print('_'*50)
for state, abbrev in states.items():
    print ("%s has the city %s" %(state,abbrev))

# print eveery city in state
print('_'*50)
for abbrev,city in cities.items():
    print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('_'*50)
for state,abbrev in states.items():
    print("%s state in abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

# safely get an abbrevation by state that might not be there
state = states.get('Texas',None)

if not state:
    print("Sorry no Texas")

# get a city with a default value
city = cities.get('TX','Does not exist')
print("The city for the state 'TX' is: %s" % (city))
    

