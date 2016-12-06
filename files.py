import json

with open("c:/temp/config.json") as f:#with-обЪект будет исп-ся в рамках данного блока и зачистка не нужна
    try:
        res = json.load(f)
    except ValueError as ex:
        print(ex)
        res = {}

print(res)