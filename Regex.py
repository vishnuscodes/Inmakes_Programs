import re

pattern = "wis"

result = re.match(pattern,"Wisdom",re.I)

if result:
    print("Matched")

else:
    print("Not matched")

pattern1 = "Dev"

string1 = "Who doesn't want to be a developer"

result1 = re.search(pattern1,string1,re.I)

if result1 is None:
    print("No match found")
else:
    print(result1.string)

pattern = "[A-Z][0-9][a-z]"

if re.search(pattern,"B1b"):
    print("Enik onnum cheyanilla")


else:
    print("Kill them all")

string2 = "It is sunny today. It might be sunny tomorrow as well"
pattern = "Sunny"

result = re.findall(pattern,string2,re.IGNORECASE)
print(result)

result2 = re.sub("<name>","Vishnu","My name is <name>")
print(result2)

pattern = "V..hnu"

if re.match(pattern,"Vishnu"):
    print("Match")

else:
    print("No match")