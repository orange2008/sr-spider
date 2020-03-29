import json
def get(json):
    print("\n\n\n")
    print("RawJson: " + str(json))
    print("\n\n\n\n\n")
    for key, value in json.items():
        print(str(json['login']) + "'s " + str(key.title()) + " is " + str(value))
    return True
