import math
score = {'A':84,'B':90,'C':75,'D':82}

print("最高分為：")
print(max(score.values()))

print("最低分為：")
print(min(score.values()))

print("人數為：")
print(len(score))

print("平均分：")
print(sum(score.values())/len(score))