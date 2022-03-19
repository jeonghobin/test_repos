from random import random

import time
import random

lunch = ["된장찌개","피자","제육"] # 리스트 형태
info = {"고향":"대전", "취미": "게임"} # 딕셔너리 형태

info["특기"] = "피아노"
info["사는곳"] = "서울"


del info["사는곳"]

for i, j in info.items():
    print(i, j)

print(info, len(info))
info.clear()
print(info)

print(lunch[2])

lunch.append("김밥")
print(lunch)
lunch.remove("피자")
del lunch[1]
print(lunch)



