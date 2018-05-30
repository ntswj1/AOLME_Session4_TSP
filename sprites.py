from parts import *
'''
This class simply creates a part of a sprite and allows it to be placed on a sprite map.
'''

class sprite(object):
    def __init__(self,rows,cols): 
        self.row_count = cols
        self.col_count = rows
        self.pic =  np.array([[None for col in range(cols)] for row in range(rows)])
        self.x_loc = 0
        self.y_loc = 0
        self.part_map = []
        self.animations = []         # a dict of lists holding frames of an animation, the name, and the movement involved.
        self.a_state = {}    # tells which animation is playing and what frame it's on
        self.name = ' '
        
    @property   
    def pos(self):
        return [self.x_loc,self.y_loc]
    
    @pos.setter
    def set_pos(self,value):
        self.x_loc = value[0]
        self.y_loc = value[1]
        
    @property
    def full_sprite(self):
        return self.pic
        
        
    @full_sprite.setter
    def set_sprite(self, value):
        '''
        Allow storing into class
        
        '''
        self.pic = value

    @full_sprite.deleter
    def del_sprite(self):
        print "Instance Terminated"
        del self.pic   
    
    @property
    def sprite_name(self):
        return self.name
        
    @sprite_name.setter
    def set_name(self, value):
        self.name = value
        
    @sprite_name.deleter
    def del_name(self):
        del self.name
        
    @property
    def anim_state(self):
        return self.a_state
        
    @anim_state.setter
    def append_anim(self,value):
        self.a_state = value

    @anim_state.deleter
    def del_anim_state(self):
        del self.a_state
    
    @property
    def anims(self):
        return self.animations
         
    def add_part(self,part,loc,name):
        #keep track of parts instead so they can be rotated/etc
        part.x_loc = loc[0]
        part.y_loc = loc[1]
        part.part_name = name
        self.part_map.append({"part":part, "loc":loc})
        self.pic = part.place_on_frame(self.pic,loc)
    
    def clear_sprite(self):
        self.pic =  np.array([[None for col in range(self.col_count)] for row in range(self.row_count)])
        
    def delete_part(self,which):
        #Find in the list and delete it, then rebuild the sprite        
        [idx] = [i for i, t in enumerate(self.part_map) if t['part'].part_name==which]
        del self.part_map[idx]
        self.clear_sprite()
        for part in self.part_map:
            part['part'].place_on_frame(self.pic,[part['part'].y_loc,part['part'].x_loc])
            
       
    def place_on_frame(self,frame_name,loc):
        self.x_loc = loc[1]
        self.y_loc = loc[0]
        for i in range(0,self.col_count):
                if i <= frame_name.shape[0]:
                    for j in range(self.row_count):
                        if j <= frame_name.shape[1]:
                            if self.pic[i][j] != None:
                                frame_name[(loc[0]+i)%frame_name.shape[0]][(loc[1]+j)%frame_name.shape[1]] = self.pic[i][j]
        return frame_name
    
    def add_animation(self,anim_list,name, movements, repeat):
        #movements 0 is the number of pixels to move by, movements 1 is the direction
        self.anims.append({"name":name, "list":anim_list, "movements":movements, "repeat":repeat})
        
    def rotate_90(self):
        self.pic = np.rot90(self.pic)
        t=self.row_count 
        self.row_count = self.col_count 
        self.col_count =t
        
    def view_sprite(self):
        #change None to 1's and display
        for i in range(self.col_count):
            for j in range(self.row_count):
                if self.pic[i][j] == None:
                    self.pic[i][j] = "FF"
        im_show(self.pic)