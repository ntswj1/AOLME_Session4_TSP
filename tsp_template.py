from scene_manager import *
from math import *

# Set up the video as a scene
scene = scene(268,372)

def move(obj, dx, dy, string_x, string_y):
    scene.move(obj, dx, string_x)
    scene.move(obj, dy, string_y)
    distance = sqrt(dx*dx + dy*dy)
    return distance    


# Initialize 
total_distance = 0.0

# Read the background image
img = read_img("bg.png")
res = shrink_img(img,29) 
cv2_1 = cv_to_hex(res)

img = read_img("dog.png")
res = shrink_img(img,50) 
cv2_2 = cv_to_hex(res)



temp = map(list,cv2_2)
for col in range(cv2_2.shape[0]):
    for row in range(cv2_2.shape[1]):
        if cv2_2[col][row]== 'ffaec9':
           temp[col][row] = None
       


dog_sprite = sprite(26,22)
dog_sprite.set_sprite = temp
dog_sprite.set_name = 'dog'

bg_sprite = sprite(268,372)
bg_sprite.set_sprite = cv2_1


scene.add_sprite(bg_sprite,[0,0], False, 'bg')
scene.add_sprite(dog_sprite,[120,0], False, 'dog')

scene.add_frame()

total_distance = total_distance + move('dog', 65, 12, 'right', 'up')
scene.add_frame()




print "Total distance travelled = "+str(total_distance)+" pixels."
show = scene.play_game()

