from typing import DefaultDict

dic = {}
lst = [['  vi a   ','sungmin'],['  ls -d  ','wonjo'],['hi', 'sunghoon'],['cd onedrive', 'sangha'],['ls -al','sungmin'],['ls -al','sungmin'],['open onedrive', 'sangha'],['ld onedrive', 'sangha'],['cd onedrive', 'sangha']]
dic = dict()

dic = DefaultDict(list)


for i in lst:
    if i[0] not in dic[i[1]]:
        i[0]=i[0].strip()
        dic[i[1]].append(i[0])


count = {}

for i in lst:
    if i[1] in count:
        count[i[1]] += 1
    else:
        count[i[1]] = 1

print(dic)

sorted_dic = dict(sorted(dic.items(), key=lambda x: len(x[1]), reverse=True))

sorted_keys = list(sorted_dic.keys())

print(sorted_keys)
number=(int)(input("rank 입력! "))
print("\n=====",number,"등 리스트=====\n")
number-=1

print("id: ", sorted_keys[number])
print("해당 id가 실행시킨 명령어의 총 수: ", count[sorted_keys[number]])
print("해당 id가 실행시킨 고유한 명령의 수: ",len(sorted_dic[sorted_keys[number]]))
print("\n======================")

