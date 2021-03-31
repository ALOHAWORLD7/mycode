farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


for animal in farms[0]["agriculture"]:
    print(animal)

print(farms[0]["agriculture"])

print('challenge 2')

choice = input("What farm you wanna look at?")
for eachdict in farms:
    if choice in eachdict['name']:
       # print(eachdict['agriculture'])
       for agitem in eachdict['agriculture']:
           print(agitem)

choice = input("What farm you wanna look at?")
yuck = ["carrot", 'celery']
for eachdict in farms:
    if choice in eachdict['name']:
       # print(eachdict['agriculture'])
       for agitem in eachdict['agriculture']:
           if agitem not in yuck:
           print(agitem)



        
