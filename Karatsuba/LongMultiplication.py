import time

#normal way for a computer to do multiplication
def multiply(a,b):
   result = 0
   for i in range(a):
      result = result + b
   return result

def not_karatsuba(x,y):
   str_x = str(x)
   str_y = str(y)
   n = int(len(str(str_x)))
   a = int(str_x[0] + str_x[1])
   b = int(str_x[2] + str_x[3])
   c = int(str_y[0] + str_y[1])
   d = int(str_y[2] + str_y[3])
   ac = a*c
   bd = b*d
   ad = a*d
   bc = b*c
   return (((10**n)*ac)+ ((10**(n/2))*(bc+ad)) + bd )

# function with karatsuba optimisation
def karatsuba(x,y):
   str_x = str(x)
   str_y = str(y)
   n = int(len(str(str_x)))
   a = int(str_x[0] + str_x[1])
   b = int(str_x[2] + str_x[3])
   c = int(str_y[0] + str_y[1])
   d = int(str_y[2] + str_y[3])
   ac = a*c
   bd = b*d
   buffer =ac + bd + (a*d) +(b*c)
   Gauss_trick = buffer - ac - bd
   return (((10**n)*ac)+ ((10**(n/2))*(Gauss_trick)) + bd )
   
#print(multiply(1234,5678))

start_1 = time.time()
print(not_karatsuba(5678,1234))
end_1 = time.time()
not_k_time = end_1 - start_1
print("not karatsuba time: {}".format(str(not_k_time)))


start_2 = time.time()
print(karatsuba(5678,1234))
end_2 = time.time()
k_time = end_2 - start_2
print("karatsuba time: {}".format(str(k_time)))
if(k_time < not_k_time):
   print("Karatsuba is faster")
else:
   print("Karatsuba is not faster!")



