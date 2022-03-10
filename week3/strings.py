#Author: Regan Heil
#Description: String Formatting Lab
varRed="Red"
varGreen="Green"
varBlue="Blue"
varName="Timmy"
varLoot="10.4516295"
print(f"Hello {varName:<0s} ")
print(f"{varRed: <0s}-{varGreen: <0s}-{varBlue: <0s}")
print(f"Is this {varGreen.lower():<0s} or {varBlue.lower():<0s}? ")
print(f"My name is {varName.upper(): <0s}")
print(f"{varRed:+^7s}")
print(f"{varGreen.lower():=<7s}")
print(f"{varBlue.lower():*>9s}")
print(f"{varBlue*10}")
print(f"{varLoot}")
print(f"{varLoot[0:3:1]}5")
print(f"I have ${varLoot: <.5s}")
print(f"{varRed:$^10s} {varGreen:$^10s} {varBlue:$^10s}")
print(f"{varRed[::-1]} {varGreen} {varBlue[::-1]}")
print(f"First Color: {varRed} Second Color: {varGreen} Third Color: {varBlue}")
