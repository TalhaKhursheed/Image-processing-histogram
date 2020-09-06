#Histogram of image
histogram=[0]*256 
PDF=[0]*256 
CDF = [0]*256 TF = [0]*256 histogram1=[0]*256 for x in range(row):     for y in range(col): 
        histogram[img[x][y]]+=1 x_axis=np.arange(256) m.title('Histogram') 
m.plot(x_axis,histogram) 
m.show() 
m.savefig('Figure1.png') 

#probability density function
for i in range(256):     PDF[i]=histogram[i]/(row*col) 
m.title('Probability Distribution Function') 
m.plot(x_axis,PDF) 
m.show() 
m.savefig('Figure2.png') 


#cdf
CDF[0]=PDF[0] for i in range(1,256):     CDF[i]=PDF[i]+CDF[i-1] 
m.title('Cumulative Distribution Function') 
m.plot(x_axis,CDF) 
m.show() 
m.savefig('Figure3.png') 


#trandformation function
 for i in range(256):     TF[i]=round(CDF[i]*255) 
m.title('Transfer Function') 
m.plot(x_axis,TF) 
m.show() 
m.savefig('Figure4.png') 

normalized = np.zeros([row,col], dtype=np.uint8) for x in range(row):     for y in range(col):         normalized[x][y]=TF[img[x][y]] cv2.imshow('lab1', normalized) cv2.waitKey(6000) cv2.imwrite('Figure_5.jpg', normalized) 


