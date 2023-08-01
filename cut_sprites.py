from PIL import Image
import os

SPRITE_DIMENSIONS = (16, 16)
STARTING_POS = (0, 0)

class Modified_img:
    def __init__(self, img):
        self.img = img
        self.size = self.width, self.height = img.size
    
    def cut_sprites(self, to_path):
        # cut sprites from image
        left = STARTING_POS[1]
        top = STARTING_POS[0]
        right = left + SPRITE_DIMENSIONS[1]
        bottom = top + SPRITE_DIMENSIONS[0]
        
        num = 0
        
        while bottom <= self.height:
            while right <= self.width:
                sprite_image = self.img.crop((left, top, right, bottom))
                sprite_image.save(to_path + '/' + str(num) + '.png')
                left += SPRITE_DIMENSIONS[1]
                right += SPRITE_DIMENSIONS[1]
                num += 1
            top += SPRITE_DIMENSIONS[0]
            bottom += SPRITE_DIMENSIONS[1]
            left = STARTING_POS[0]
            right = left + SPRITE_DIMENSIONS[1]
    
    def rotate(self, directory):
        directory.replace('/up', '')
        directory.replace('/down', '')
        directory.replace('/left', '')
        directory.replace('/right', '')
        
        up = self.img.rotate(0, expand = True)
        up.save(directory + '/up.png')
        left = self.img.rotate(90, expand = True)
        left = self.img.resize((self.height, self.width), resample = 0)
        left.save(directory + '/left.png')
        down = self.img.rotate(180, expand = True)
        down.save(directory + '/down.png')
        right = self.img.resize((self.height, self.width), resample = 0)
        right = self.img.rotate(270, expand = True)
        right.save(directory + '/right.png')

def main():
    path_in = 'c:/Users/szomi/Dropbox/Komputer/Desktop/NinjaAdventure'
    to_rotate = ['/Weapons/']


    for path, dir_names, file_names in os.walk(path_in):
        path = path.replace('\\', '/')
        print(path)
        for file in file_names:
            if file.split('.')[-1] == 'png':
                if not os.path.isdir(path + '/' + file.removesuffix('.png')):
                    os.mkdir(path +'/' + file.split('.')[0])
                    
                image = Modified_img(Image.open(path + '/' + file))
                
                image.cut_sprites(path + '/' + file.removesuffix('.png'))
                
                # rotate selected images
                """
                for part in to_rotate:
                    if part in path:
                        image.rotate(path + '/' + file.remove('.png'))
                        """
        
        
if __name__ == '__main__':
    main()
        
        