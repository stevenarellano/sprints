import yaml

with open('yourfile.yaml', 'r') as file:
    data = yaml.safe_load(file)
    print(data)
