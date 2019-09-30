import imagehash
import timeit
from PIL import Image
hash0 = imagehash.average_hash(Image.open('https://storage.cloud.google.com/loblaw_digi/master/Pshirt-1.jpeg')) 
hash1 = imagehash.average_hash(Image.open('https://storage.cloud.google.com/loblaw_digi/master/Pshirt-3.jpeg')) 
cutoff = 5
if hash0 - hash1 < cutoff:
  print('images are similar')
else:
  print('images are not similar')
'''
Since the images are not exactly the same, there will be some differences.
But imagehash will work even if the images are resized,
compressed, different file formats or with adjusted contrast or colors.
The hash (or fingerprint, really) is derived from a 8x8 monochrome
thumbnail of the image.
But even with such a reduced sample,
the similarity comparisons give quite accurate results.
Adjust the cutoff to find a balance between false positives and false negatives that is acceptable.
'''
