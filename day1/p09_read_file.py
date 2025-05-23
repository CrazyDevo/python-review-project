import  json

def read_config():
    file_path = "../conf.json"
    with open(file_path) as file:
      return json.load(file)

config=read_config()

print(config["password"])