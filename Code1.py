# Lengkapilah potongan program di bawah ini
dataFloat = ()
dataList = []
dataDict = {}

random_list = [900, 3.1, 3078, "Hello", 737, "Python", 2.7, 2002, 50,
               "Tech Winter", 7.566, 40, 1, "Is", 60.5, "Better", 1000.1,
               4, "world", 412, 5.5, "AI", 99.234, 12000]

for data in random_list:
    if isinstance(data, float):
      dataFloat += (data,)
    elif isinstance(data, str):
      dataList.append(data)
    elif isinstance(data, int):
        if data < 10:
          dataDict[data] = None
print("string data Float = ", dataFloat )
print("string data list = ", dataList)
print("int data dictionary = ", dataDict)