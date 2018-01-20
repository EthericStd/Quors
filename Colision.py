class Collision():
    def __init__(self, objects):
        self.tags=[]
        self.objects=objects

    def add(self, tag):
        self.tags+=[tag]

    def del_tag(self, tag):
        self.tags.remove(tag)

    def find(self, tag, direction):
        #checking if self.tags (with s) overlap the unique tag in para
        #thank to a boxofsafety to the right/left/top/bottom
        #of the surfaces of the unique tag in para
        for tag2 in self.tags:
            for value in self.objects.get_valuesoftag(tag2):
                box=self.create_boxofsafety(value, direction)
                boxtest=pygame.Surface( (box[2], box[3]) )
                boxtest.fill((255,128,128))
                self.objects.del_tag("boxtest")
                self.objects.add(boxtest, box[0], box[1], "boxtest")
                for value2 in self.objects.get_valuesoftag(tag):
                    if not( (box[0]>value2[1]+value2[0].get_width())
                        or (box[0]+box[2]<value2[1])
                        or (box[1]>value2[2]+value2[0].get_height())
                        or (box[1]+box[3]<value2[2]) ):
                        return True
        return False

    @staticmethod
    def create_boxofsafety(value, direction):
            x=value[1]
            y=value[2]
            width=value[0].get_width()
            height=value[0].get_height()
            if direction==K_w:
               boxofsafety=[x, y-boxofsafety_length, width, boxofsafety_length]
            elif direction==K_s:
               boxofsafety=[x, y+height, width, boxofsafety_length]
            elif direction==K_a:
               boxofsafety=[x-boxofsafety_length, y, boxofsafety_length, height]
            elif direction==K_d:
               boxofsafety=[x+width, y, boxofsafety_length, height]
            return boxofsafety
