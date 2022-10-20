#import matplotlib.pyplot as plt
#import numpy as np

#list = [1, 2, 3, 2, 7]
#plt.plot(list)

#plt.show()

#plt.style.use('_mpl-gallery')

#$ make data
#np.random.seed(3)
#x =  0.5 + np.arange(8)
#y = np.random.uniform(2,7 , len(x))

## plot
#fig, ax = plt.subplots()

#ax.stem(x, y)

#ax.set(xlim=(0,8 ), xticks=np.arange(1,8 ),
#       ylim=(0,8 ), yticks=np.arange(1,8 ))

#plt.show()





#import emoji

#print(emoji.emojize('Python is :thumbs_up:'))
#print(emoji.emojize('Python is :thumbsup:', language='alias'))
#print(emoji.demojize('Python is 👍'))
#print(emoji.emojize("Python is fun :red_heart:"))
#print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
#print(emoji.is_emoji("👍"))




#from progress.bar import Bar
#import time

#bar = Bar('Processing', max=20)
#for i in range(20):
#    time.sleep(1)
#    bar.next()
#bar.finish()




#from isOdd import isOdd

#print(isOdd(0)) 
#print(isOdd(5))