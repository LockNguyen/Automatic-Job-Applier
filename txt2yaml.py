import sys

# Convert each text line to YAML (page 1)
new_phrases = []

for line in sys.stdin:
    if line == "\n":
        break
    keys = line.split("= ")
    new_phrase = ': '.join(keys)
    new_phrases.append(new_phrase)

for x in new_phrases:
    print(x, end="")



# Convert each text line to YAML (page 5)
lines = []

for line in sys.stdin:
    if line == ".\n":
        break
    lines.append(line)

i = 1
print("question_1:")

for line in lines:
    if line == "\n":
        i+=1
        if i > 7:
            break
        else:
            print("question_{}:".format(i))
    else:
        print("  - {}".format(line.rstrip("\n")))