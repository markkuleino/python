import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import numpy as np


names =     [ r'N5414A.jp2' ]
names.append( r'N5414C.jp2' )
names.append( r'N5414E.jp2' )
names.append( r'N5413B.jp2' )
names.append( r'N5413D.jp2' )
names.append( r'N5413F.jp2' )
names.append( r'N5413C.jp2' )

imgs = []
for n in names:
    imgs.append( rasterio.open( n ) )

row1 = []
row2 = []
row3 = []

def normalize(a):
    print( a.max(),   a.min() )
    a_min, a_max = a.min(), a.max()
    a_min, a_max = 75, 144
    #Clip: if
    #a[ np.where( a< a_min ) ] = -1
    return (a- a_min) / (a_max - a_min)

for i,img in enumerate(imgs):
        #Convert to numpy
        height = img.read(1)
        height = normalize( height )

        if i == 0:
            row1 = height
        if i == 1:
            row1 = np.concatenate( (row1, height),1 )
        if i == 2:
            row1 = np.concatenate( (row1, height),1 )
        if i == 3:
            row2 = height
        if i == 4:
            row2 = np.concatenate( (row2, height),1 )
        if i == 5:
            row2 = np.concatenate( (row2, height),1 )
        if i == 6:
            row3 = np.concatenate( (np.zeros(np.shape(height)), height, np.zeros(np.shape(height))),1 )


        #fig, ax = plt.subplots ( figsize=plt.figaspect( height )  )
        #fig.subplots_adjust(0,0,1,1)
        #
        #ax.imshow(height, cmap="Greys")
        #plt.axis('off')
        #plt.show()
        #plt.savefig("test"+str(i)+".png" , dpi=300 )

image = np.concatenate( (row1, row2, row3), axis=0 )
print( image.max() )
print( image.min() )
fig, ax = plt.subplots ( figsize=plt.figaspect(image)  )
fig.subplots_adjust(0,0,1,1)

ax.imshow(image, cmap="Greys")
plt.axis('off')
plt.show()
plt.savefig("map.png" , dpi=1200 )

print("Ok")
