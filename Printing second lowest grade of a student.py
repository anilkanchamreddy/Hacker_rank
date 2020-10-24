std_re=[]
score_l=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_l.append(score)
        std_re.append([name,score])
score_l.sort()
score_final=[i for i in score_l if i!=score_l[0]]
result=[]
for i in std_re:
    if i[1]==score_final[0]:
        result.append(i[0])
result.sort()
for i in result:print(i)
