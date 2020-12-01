import matplotlib.pyplot as plt
from planetaryimage import PDS3Image
import glob
for i in glob.glob('*.*LBL'): 
    image = PDS3Image.open(i)
    #print(image.record_bytes)
    #print(image.label['FILE_RECORDS'])
    plt.imsave(f"{i}.png",image.image, cmap='gray')
