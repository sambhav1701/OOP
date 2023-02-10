import InsectClass as IC


mosquito = IC.Insect('mosquito', 4, 2)
housefly = IC.Insect('housefly', 4, 2)

mosquito.length_of_flight()
housefly.length_of_flight()

print(f'The {mosquito.get_name()} flew {mosquito.get_flight()} miles')
print(f'The {housefly.get_name()} flew {housefly.get_flight()} miles')