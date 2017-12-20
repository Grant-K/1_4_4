import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
myHand_file = os.path.join(directory, 'my_hand.jpg')

# Open and show the student image in a new Figure window
myHand_img = PIL.Image.open(myHand_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(myHand_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(myHand_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(700, 2300) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(3250, 1300)
fig.show()

# Open, resize, and display earth
fireBall_file = os.path.join(directory, 'newFireBall.png')
fireBall_img = PIL.Image.open(fireBall_file)
fireBall_small = fireBall_img.resize((1250, 2750)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(fireBall_img)
axes2[1].imshow(fireBall_small)
fig2.show()

# Paste earth into right eye and display
# Uses alpha from mask
myHand_img.paste(fireBall_small, (750, -100), mask=fireBall_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(myHand_img, interpolation='none')
axes3[1].imshow(myHand_img, interpolation='none')
axes3[1].set_xlim(700, 2300)
axes3[1].set_ylim(3250, 1300)
fig3.show()