import numpy as np
import math
import matplotlib.pyplot as plt
def display_network(A, opt_normalize = True, opt_graycolor = True, cols = -1, opt_colmajor = False):
	A = np.asarray(A)
	m = A.mean()
	B = A - m
	A = B

	#
	#Colormap
	#

	s = A.shape()
	L = s[0] #Row
	M = s[1] #column

	sz = math.sqrt(L)

	buf = 1

	if cols == -1:
		if (math.floor(math.sqrt(M))**2) != M :
			n = math.ceil(math.sqrt(M))
			while M%n != 0 and n < 1.2*math.sqrt(M) :
				n = n+1
			m = math.ceil(M/n)
		else :
			n = math.sqrt(M)
			m = n

	else : 
		n = cols
		m = math.ceil(M/n)

	array = -1*np.ones((buf+m*(sz+buf),buf+n*(sz+buf)))

	if opt_graycolor == False :
		array = 0.1*array

	if opt_colmajor == False :
		k = 1
		for i in range(1,m+1) :
			for j in range(1,n+1) :
				if k > M :
					continue
				clim = math.max(math.abs(A[:,k])) #Check this line
				if opt_normalize :
					array[np.ix_(buf+(i-1)*(sz+buf)+range(1,sz+1)-1,buf+(j-1)*(sz+buf)+range(1,sz+1)-1)] = np.reshape(A[:,k],(sz,sz))/clim
				else :
					xx = A
					array[np.ix_(buf+(i-1)*(sz+buf)+range(1,sz+1),buf+(j-1)*(sz+buf)+range(1,sz+1)-1)] = np.reshape(A[:,k],(sz,sz))/abs(xx.flat[abs(xx).argmax()])
				k = k + 1
	else :
		k = 1
		for j in range(1,n) :
			for i in range(1,m) :
				if k > M :
					continue
				clim = math.max(math.abs(A[:,k])) #Check this line
				if opt_normalize :
					array[np.ix_(buf+(i-1)*(sz+buf)+range(1,sz+1)-1,buf+(j-1)*(sz+buf)+range(1,sz+1)-1)] = np.reshape(A[:,k],(sz,sz))/clim
				else :
					array[np.ix_(buf+(i-1)*(sz+buf)+range(1,sz+1),buf+(j-1)*(sz+buf)+range(1,sz+1)-1)] = np.reshape(A[:,k],(sz,sz))
				k = k + 1

	fig,ax = plt.subplots()
	ax.plot(array)
	ax.axis('off')
	f = plt.figure(1)

	return f,array

