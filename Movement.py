class Movement():
    def __init__(self, objects, collision):
        self.tags=[]
        self.directions={K_w:[0,1], K_s:[0,-1], K_a:[1,0], K_d:[-1,0]}
        self.objects=objects
        self.collision=collision

    def add(self, tag):
        self.tags+=[tag]

    def del_tag(self, tag):
        self.tags.remove(tag)

    def processing(self, key):
        for direction in self.directions:
            if key==direction:
                for tag in self.tags:
                    if not self.collision.find(tag, direction):
                        self.objects.move(tag, wall_speed*self.directions[direction][0], wall_speed*self.directions[direction][1])

