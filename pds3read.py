import matplotlib.pyplot as plt
from planetaryimage import PDS3Image
import glob
for i in glob.glob('*.*LBL'): 
    image = PDS3Image.open('0794ML0034670030400663E01_DRCL.LBL')
    #print(image.record_bytes)
    #print(image.label['FILE_RECORDS'])
    plt.imsave(f"{i}.png",image.image, cmap='gray')
