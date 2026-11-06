import numpy as np

# 1. Creating arrays
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])
c = np.array( [ [[1,2],[3,4]], [[5,6],[7,8]] ])
print(np.zeros(5))          
print(np.ones((2, 3)))       
print(np.arange(0, 10, 2))   
print(np.linspace(0, 1, 5))


# 2. Array properties
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])
c = np.array( [ [[1,2],[3,4]], [[5,6],[7,8]] ])
# Array a
print("a shape:", a.shape)   #(4,)   
print("a ndim:", a.ndim)     #1     
print("a size:", a.size)     #4
print("a dtype:", a.dtype)   #int64
print()
# Array b
print("b shape:", b.shape)   #(2,2) 
print("b ndim:", b.ndim)     #2
print("b size:", b.size)     #4
print("b dtype:", b.dtype)   #int64
print()
# Array c
print("c shape:", c.shape)   #(2, 2, 2)
print("c ndim:", c.ndim)     #3 
print("c size:", c.size)     #8 
print("c dtype:", c.dtype)   #int64  

# #other dtypes: int8, int16, int32, int64, uint8, uint16, uint32, uint64, 
# # float16, float32, float64, complex64, complex128, bool, str, object


# 3. Indexing, subsetting & slicing
a = np.array([10, 20, 30, 40, 50])
print(a[0])        #10
print(a[-1])       #50
print(a[[1,2,3]])  #[20 30 40]
# print(a[-12]) 
print(a[1:4])      #20 30 40


# # For 2D arrays:
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
#syntax: 
# 1-D array: arr[indices]
# 2-D array: arr[row indices, col indices]
print(b[0, 1])            
print(b[[0,1], [1, 2]] )  
print(b[[0,1], [0]]) 
print(b[[0], [0,2]]) 
print(b[:, 1]) 
print(b[1, :])  
print(b[0:2,1:3])    


# # 4. Array calculations
# # NumPy performs operations element-by-element:
a = np.array([1, 2, 3])
print(a + 10)     #[11 12 13]
print(a * 2)      #[2 4 6]
print(a ** 2)     #[1 4 9]
print(a + a)      #[2 4 6]
# Useful functions:
print("sum:", np.sum(a))       
print("mean:", np.mean(a))     
print("median:", np.median(a)) 
# print("mode:", np.mode(a))  
print("min:", np.min(a))    
print("max:", np.max(a))      
print("std:", np.std(a))       


# 5. Boolean filtering
a = np.array([10, 20, 30, 40, 50])   
# a > 25 returns a boolean array
print(a > 25)     #[F F T T T]                    
# a[boolean_array] gives elements wherever True
print(a[a > 25])  #[30 40 50]             
# Multiple conditions:
b= (a > 15) & (a < 45)
print(a[b])  


# 6. Reshaping
a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2,3)
print(a)   
print(b)    
# Other useful operations:
print(b.flatten())        
# Transpose for 2D arrays
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(b.T)  


# 7. Matrix operations
A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])
print(A * B)            
print(A @ B)             
print(np.dot(A, B))      
print(np.linalg.det(A))  
print(np.linalg.inv(A))  


# 8. Random numbers
# For reproducible results:
np.random.seed(1)
print(np.random.rand(3))         
print(np.random.randint(1, 10, 5))   
print(np.random.rand(2, 4))           


# 9. Broadcasting
# NumPy can automatically apply operations between compatible shapes:
a = np.array([1, 2, 3])
print(a * 10)
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(A + np.array([10, 20, 30]))