import pygame.surface

pygame.init()
class Canvas:
    def __init__(self, root, x, y, width, height, color=(230,230,230)):
        self.x = x
        self.y = y
        self.surface = pygame.Surface( (width, height) )

        self.tags={}
        self.values=[]

        self.create_background(x, y, width, height, color)

        root.addCanvas(self)


    def exist(self, tag):
        for i in self.tags:
            if tag==i:
                return True
        return False

    def add(self, surface, posx, posy, tag):
        if self.exist(tag):
            self.values[self.tags[tag]]+=[[surface, posx, posy]]
        else:
            self.tags[tag]=len(self.values)
            self.values+=[[[surface, posx, posy]]]

    def delTag(self, tag):
        if self.exist(tag):
            memo=self.tags[tag]
            del self.values[self.tags[tag]]
            del self.tags[tag]
            for i in self.tags:
                if self.tags[i]>memo:
                    self.tags[i]-=1

    def blitAll(self):
        for groups in self.values:
            for objects in groups:
                self.surface.blit(objects[0], (objects[1], objects[2]) )

    def move(self, tag, x, y):
        for objects in self.values[self.tags[tag]]:
            objects[1]+=x
            objects[2]+=y

    def len(self, tag):
        return len(self.values[self.tags[tag]])

    def getValuesOfTag(self, tag):
        return self.values[self.tags[tag]]


    #---------------------------------------------------------------------

    def create_background(self, x, y, width, height, color):
        background = pygame.Surface( (width, height) )
        background.fill(color)
        self.add(background, 0 ,0, "background")


    def add_rectangle(self, x, y, width, height, tag, color=(250,100,20)):
        s = pygame.Surface( (width, height) )
        s.fill(color)
        self.add(s, x, y, tag)

    def add_image(self, x, y, tag, path):
        s = pygame.Image.load(path).convert_alpha()
        self.add(s, x, y, tag)
