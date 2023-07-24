from PIL import Image
import os

SPRITE_DIMENSIONS = (16, 16)
STARTING_POS = (0, 0)

path_in = 'c:/Users/szomi/Dropbox/Komputer/Desktop/NinjaAdventure'
to_rotate = ['/weapons/']

def cut(path_in):
    for path, dir_names, file_names in os.walk(path_in):
        path = path.replace('\\', '/')
        for file in file_names:
            if file.split('.')[-1] == '.png':
                if not os.path.isdir(path.replace('/'+file,'/') + file.split('.')[0]):
                    os.mkdir(path +'/' + file.split('.')[0])
                        
                image = Image.open(path + '/' + file)
                width, height = image.size
                
                # rotate selected images
                for part in to_rotate:
                    if part in path:
                        rotate(image, path.replace('/'+file,'/')+file.split('.')[0])
                
                # cut sprites from image
                left = STARTING_POS[1]
                top = STARTING_POS[0]
                right = left + SPRITE_DIMENSIONS[1]
                bottom = left + SPRITE_DIMENSIONS[0]
                
                num = 0
                
                while bottom <= height:
                    while right <= width:
                        sprite_image = image.crop((left, top, right, bottom))
                        sprite_image.save(path.replace('/'+file,'/') + file.split('.')[0] + '/' + str(num) + '.png')
                        left += SPRITE_DIMENSIONS[1]
                        right += SPRITE_DIMENSIONS[1]
                        num += 1
                    top += SPRITE_DIMENSIONS[0]
                    bottom += SPRITE_DIMENSIONS[1]
                    left, right = STARTING_POS
            
def rotate(image, directory):
        
        up = image.rotate(0)
        up.save(directory + '/up.png')
        left = image.rotate(90)
        left.save(directory + '/left.png')
        down = image.rotate(180)
        down.save(directory + '/down.png')
        right = image.rotate(270)
        right.save(directory + '/right.png')
        
        