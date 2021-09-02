import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd

# Reading the images 

top_left      = cv2.imread( 'top_left.jpg'     )
top_right     = cv2.imread( 'top_right.jpg'    )
bottom_left   = cv2.imread( 'bottom_left.jpg'  )
bottom_right  = cv2.imread( 'bottom_right.jpg' )
center        = cv2.imread( 'center.jpeg'      )

# Correcting the color of the images

top_left      = cv2.cvtColor( top_left     , cv2.COLOR_BGR2RGB )
top_right     = cv2.cvtColor( top_right    , cv2.COLOR_BGR2RGB )
bottom_left   = cv2.cvtColor( bottom_left  , cv2.COLOR_BGR2RGB )
bottom_right  = cv2.cvtColor( bottom_right , cv2.COLOR_BGR2RGB )
center        = cv2.cvtColor( center       , cv2.COLOR_BGR2RGB )

# Resizing the images

top_left      = cv2.resize( top_left     , (200,200) )
top_right     = cv2.resize( top_right    , (200,200) )
bottom_left   = cv2.resize( bottom_left  , (200,200) )
bottom_right  = cv2.resize( bottom_right , (200,200) )
center        = cv2.resize( center       , (100,100) )

# Adding borders to the images 

top_left      = cv2.copyMakeBorder( top_left     , 10,  5, 10,  5, cv2.BORDER_CONSTANT, value=[0,0,0] )
top_right     = cv2.copyMakeBorder( top_right    , 10,  5,  5, 10, cv2.BORDER_CONSTANT, value=[0,0,0] )
bottom_left   = cv2.copyMakeBorder( bottom_left  ,  5, 10, 10,  5, cv2.BORDER_CONSTANT, value=[0,0,0] )
bottom_right  = cv2.copyMakeBorder( bottom_right ,  5, 10,  5, 10, cv2.BORDER_CONSTANT, value=[0,0,0] )
center        = cv2.copyMakeBorder( center       , 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[0,0,0] )

# Combining the images 

top_output = cv2.hconcat([top_left, top_right])
bottom_output = cv2.hconcat([bottom_left, bottom_right])
output = cv2.vconcat([top_output, bottom_output])
x_offset=y_offset=155
output[y_offset:y_offset+center.shape[0], x_offset:x_offset+center.shape[1]] = center

# Saving as .csv

output = np.reshape(output,(-1,3))
pd.DataFrame(data = output).to_csv('output.csv', header = ['r','g','b'], index = False)

# View the output

plt.imshow(output)
plt.show()
