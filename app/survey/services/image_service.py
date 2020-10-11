from PIL import Image
import urllib.request
class ImageService(object):

    @classmethod
    def generate_thumbnail(cls,image_url):
        try:
            image = urllib.request.urlretrieve(image_url)
            image = Image.open(image[0]) 
            
            SIZE = (50, 50) 
            
            image.thumbnail(SIZE) 
            
            image.show()
            s = image.tobytes().decode("latin1") 
            return {
                'image': s
            }
        except:
            return None