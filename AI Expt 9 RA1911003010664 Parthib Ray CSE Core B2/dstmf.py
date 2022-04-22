from numpy import *
def DempsterRule(m1, m2):
## extract the frame of discernment
sets=set(m1.keys()).union(set(m2.keys()))
result=dict.fromkeys(sets,0)
## Combination process
for i in m1.keys():
for j in m2.keys():
if set(str(i)).intersection(set(str(j))) == set(str(i)):
result[i]+=m1[i]*m2[j]
elif set(str(i)).intersection(set(str(j))) == set(str(j)):
result[j]+=m1[i]*m2[j]
## normalize the results
f= sum(list(result.values()))
for i in result.keys():
result[i] /=f
return result
m1 = {'a':0.4, 'b':0.2, 'ab':0.1, 'abc':0.3}
m2 = {'b':0.5, 'c':0.2, 'ac':0.3, 'a':0.0}
print(DempsterRule(m1, m2))
