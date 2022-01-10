import datetime

# print(datetime.datetime.now())
# 2021-12-16 11:06:10.077664

words = ["frodo","front","frost","frozen", "frame","kakao"]
rev_words = [word[::-1] for word in words]
print(words)
print(rev_words)
queries = ["fro??","????o","fr???","fro???","pro?"]
wordsLen = dict()
for word in words:
    if len(word) in wordsLen.keys():
        wordsLen[len(word)].append(word)
    else:
        wordsLen[len(word)]= [word]
for k,v in wordsLen.items():
    wordsLen[k].sort()
print(wordsLen)

res = []
for query in queries:
    l = len(query)
    a =''; b=''
    # for s in query:
    #     if query[0] == '?' and
    # if l in wordsLen.keys():
    #     if idx == 0:
    #         for word in wordsLen[l]:
    #
    #     else:
    #         for word in wordsLen[l]:
    #             pass

    # else:
    #     res.append(0)