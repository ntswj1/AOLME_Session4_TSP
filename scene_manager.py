from sprites import *

class scene(object):
    def __init__(self,size_x,size_y):
        self.pic =  np.array([["ffffff" for col in range(size_y)] for row in range(size_x)])
        self.x = size_x
        self.y = size_y
        self.sprites = []
        self.frames = []
        
    def add_sprite(self,sprite, loc, animated, anim_name):
        self.sprites.append({"sprite":sprite, "loc":loc})
        #keep location of all sprites in scene
        if animated == False:
            self.sprites[len(self.sprites)-1]['sprite'].append_anim = {"playing":False, "anim":anim_name, "current_frame":0}
        else:
            self.sprites[len(self.sprites)-1]['sprite'].append_anim = {"playing":True, "anim":anim_name, "current_frame":0}

    def move(self, which, by, where):
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        if where == 'down':
            self.sprites[idx]['loc'][0] += by        
        elif where == 'up':
            self.sprites[idx]['loc'][0] -= by        
        elif where == 'left':
            self.sprites[idx]['loc'][1] -= by
        elif where == 'right':
            self.sprites[idx]['loc'][1] += by 
        elif where == 'none':
            pass     
            
    #when adding the sprite, set the animation state, if it has no animations to be played it will be false.  
    
    def add_anim(self,which,anim_name):
        # reference the animation and turn it on, set its playframe to zero.
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        self.sprites[idx]['sprite'].append_anim = {"playing":True, "anim":anim_name, "current_frame":0}
    
    def clear_scene(self):
        self.pic =  np.array([["ffffff" for col in range(self.y)] for row in range(self.x)])
        
    def add_frame(self):
        self.clear_scene()
        # first handle animations if any have been added
        for sprite in self.sprites:
            if sprite['sprite'].anim_state['playing'] == True:
                #get the animation
                print sprite['sprite'].anims[0]['name']
                which = sprite['sprite'].anim_state['anim']
                [idx] = [i for i, t in enumerate(sprite['sprite'].anims) if t['name']==which]
                #grab the frame and update the sprite.
                sprite['sprite'].set_sprite = sprite['sprite'].anims[idx]['list'][sprite['sprite'].anim_state['current_frame']]
                self.move(sprite['sprite'].sprite_name, sprite['sprite'].anims[idx]["movements"][sprite['sprite'].anim_state['current_frame']][1], sprite['sprite'].anims[idx]["movements"][sprite['sprite'].anim_state['current_frame']][0]) 
                if sprite['sprite'].anim_state['current_frame'] < len(sprite['sprite'].anims[idx]["list"]):
                    sprite['sprite'].anim_state['current_frame']+=1
                else:
                    sprite['sprite'].anim_state['current_frame'] = 0    
            sprite['sprite'].place_on_frame(self.pic,sprite['loc'])
        self.frames.append(self.pic)
        #im_show(self.pic)
        
        #to play the video, add frames one by one after moving an object to a list
    def play_game(self):
        return vid_show(self.frames,30)
