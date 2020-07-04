import itertools
import oldstr

#input nilai ke-1
input_1= [4,3,6,5,1,2]
#input nilai ke-2
input_2= ['F','C','D','B','A']

#sort nilai Ke-1 dan ke-2
input_1.sort()
input_2.sort()

#combine nilai ke-1 dan ke-2, jika length dari nilai ke-1>ke-2 maka akan diberikan hasil NULL
res = [i for i in itertools.zip_longest(input_1,input_2, fillvalue='Null')]
#print hasil res
print(res)

