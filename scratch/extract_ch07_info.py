import re

with open(r'scratch\ch07_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print("Learning Objectives:")
for match in set(re.findall(r'LO 7\.\d+', text)):
    print(match)

print("\nExercise sections:")
for match in set(re.findall(r'Brief Exercises|Exercises|Professional Application Cases|Multiple Choice|Chapter Review', text, re.IGNORECASE)):
    print(match)
