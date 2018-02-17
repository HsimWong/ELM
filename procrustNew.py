import numpy as np
def procrustNew(A,B,nargout = 2):
	A = np.asarray(A)
	B = np.asarray(B)
	C = np.dot(B.transpose(),A)
	U1,S1,V1 = np.linalg.svd(np.dot(C.transpose(),C),full_matrices = True)
	U2,S2,V2 = np.linalg.svd(np.dot(C,C.transpose()),full_matrices = True)
	Q = np.dot(U2,V1.transpose())
	A2 = np.dot(B,Q)
	if nargout > 2 :
		R = np.linalg.norm(np.subtract(A,A2),ord = 'fro')
		return A2,Q,R
	return A2,Q

print(procrustNew([[1,2],[3,4]],[[1,23],[5,64]]))