# create the planets.txt
planet_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planet_file = open('planets.txt', 'w', encoding='utf-8')

for planet in range(len(planet_list)):
    planet_file.writelines(planet_list[planet] + '\n')

planet_file.close()
