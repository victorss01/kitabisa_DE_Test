import itertools
import oldstr

input_1= [4,3,6,5,1,2]
input_2= ['F','C','D','B','A']
input_1.sort()
input_2.sort()

res = [i for i in itertools.zip_longest(input_1,input_2, fillvalue='Null')] 
res = oldstr.replace('', )
print(res)

