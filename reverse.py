
vector = [0,1,2,3,4,5,6,7,8,9,10]
i = 0
j = (len(vector))-1
print(vector)
while i < (len(vector)/2):
    vector[i],vector[j] = vector[j],vector[i]
    i+=1
    j-=1
print(vector)
