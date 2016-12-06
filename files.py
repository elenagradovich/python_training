import json

f = open("c:/temp/config.json")
try:
    res = json.load(f)
except ValueError as ex:
    print(ex)
    res = {}
finally:
    f.close()

print(res)