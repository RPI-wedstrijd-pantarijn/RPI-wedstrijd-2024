import json

Opened = {
    "Servo1": True,
    "Servo2": False,
}
with open("data.json", "w", encoding="utf8") as file_handle:
    json.dump(Opened, file_handle, indent=4)

with open("data.json", "r", encoding="utf8") as file_object:
    OpenedData = json.load(file_object)
    print(OpenedData)

print(OpenedData["Servo1"])
OpenedData["Servo1"] = False

with open("data.json", "w", encoding="utf8") as file_handle:
    json.dump(OpenedData, file_handle, indent=4)
