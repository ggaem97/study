dic = {'pop': 3100, 'classic': 1450, 'trot':620}
# # key 값을 기준으로 오름차순 정렬하여 리스트 반환
# print(sorted(dic))
# print(sorted(dic, reverse=True))

# value 값을 기준으로 오름차순 정렬하여 (k, v) 리스트 반환
print(sorted(dic.items(), key=lambda x:x[1]))
# # 위 값을 딕셔너리로 변환
print(dict(sorted(dic.items(), key=lambda x:x[1])))
# value 값을 기준으로 오름차순 정렬
print(sorted(dic,key=lambda x:dic[x]))


# print(sorted(dic.items()))
# # print(dic)
# dic = dict(sorted(dic.items()))
# print(dic)