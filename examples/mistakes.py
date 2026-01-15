 # import package(s) and create aliases
import numpy as np #np instead of numpy
from np import array #array instead of numpy.array
from numpy.linalg import inv as inv# inv instead of numpy. linalg.inv

#create arrays and do math on them−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
a1 = [ 5 , 8 , 13 ] #ok. but this is a ”list” not a mathematical array
a = array( [ 5 , 8 , 13 ] ) #ok? this neither a row nor a column
b1 = a.T # !!. .T transpose−does not work with a 1Darray
b = np.array([a]).T #ok. .T transpose−works with a 2Darray
c1 = a1 * 2 # surprised? intrigued?? correct??
c = a * 2 #ok. mathematically correct.
x = bˆ3 #?? bitwise XOR
d = b**3 #ok. use ∗∗ for exponentiation
p1 = a * b #ok. element−wise multiplication
p2 = b * a #ok. element−wise multiplication a∗b=b∗a
p3 = a * b.T #ok. element−wise multiplication (1x3) ... like .∗
p4 = a.T * b #ok. element−wise multiplication (3x1) ... like .∗q1 = a @ b #ok? correct inner product (?x3)(3x1) not(1x1) ?
q2 = np.array([a]) @ b #ok correct inner product (1x3)(3x1) = (1x1)
q3 = b @ a #?? not an outer product (3x1)(?x3) not (3x3)
q4 = b @ [a] #ok. correct outer product (3x1)(1x3) = (3x3)
q5 = [a].T @ b.T #?? can not transpose a list
q4 = np.array([a]).T @ b.T #ok. correct transpose of outer product
r1 = a / b #ok. element−wise operation, (1x3) like ”./”
r2 = a / b.T #ok. element−wise operation, (3x1) like ”./”
r3 = a \ b # !!. there’s no ”left divide” in Python
28 #multi−dimensional arrays (matrices) −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
A1 = [ a , a+21 , a**2 ] # !!. list of 2Darrays
A2 = array( a , a+21 , a**2 ) # !!. syntax error
A = np.array([ a, a+21, a**2 ])#ok. preferable!
x = inv(A) @ b #ok. solves A∗x=b for x
z = A @ x- b #ok. ... should be very close to zero
AtA = A.T @ A #a symmetric non−negative definite matrix
35 # stacking arrays horizontally and vertically−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
B = np.array([ b , b**2 ]) #ok. −−− but it will not work with np.block ...
B = np.hstack([ b , b**2 ]) #ok. −−− this will work with np.block
C = np.array([ c+13 , c**2 ]) #ok. ... even though the first try at Bwoudn’t work
D = np.zeros([2,2]) #ok.
S = np.block([[A, B], ([C, D]) ]) # [ A, B ; C, D ]
41 # indexing arrays−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
u = [ 0 : 10 ] # !!. syntax error
u = np.linspace(1,10,10) #ok! much better ...
v = u[10] # !!. Python array indices start at zero
v = u[0] #ok. Python array indices start at zero
v = u[-1] #ok. ... the last element of u
v = u[-2] #ok. ... the next to last element of u
v = u[2:5] #??. starting at index 2 and going to the 5th value
v = u[2:5+1] #ok. starting at index 2 and going to index 5
v = A[2,0] #ok. ... row 2, column 0 of A
v = A[2][0] #ok. C−syntax
v = A[1,:] #ok. row 1 of A ... (the second row of A”index−0”)
v = A[1:2,:] #ok. rows 2 and 3 and all columns
v = A[1:2,1:2] #ok. rows 2 and 3 and columns 2 and 3
v = u[6:-2:2] #!?!. not at all what matlab users would expect!
v = u[[6,4,2]] #ok. ... what we would expect , in any case
y1 = a.T @ a      # !!. transpose of 1D array does nothing
y  = np.array([a]).T @ np.array([a])   # ok. (3x1)(1x3) = (3x3)
z1 = a + b        # !!. shape mismatch (3,) + (3x1)
z  = a + b.T      # ok. both are (1x3)
E1 = inv(B)       # !!. B is not square
E  = inv(A)       # ok. A is (3x3)
F1 = A * A        # !!. element-wise multiplication
F  = A @ A        # ok. matrix multiplication