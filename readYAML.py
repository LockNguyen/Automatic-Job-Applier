import yaml
from pathlib import Path

filename = Path(__file__).with_name("config.yml")

# Read config.yml
with open(filename, 'r') as file:
    try:
        diction = yaml.safe_load(file)
    except yaml.YAMLError as err:
        print(err)

# Print the resulting 'diction' variable
for key in diction.keys():
    print(key)
    print(diction[key], "\n")

my_list = list(diction["page_1"].values())
print(my_list)