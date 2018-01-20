import pygame.surface

pygame.init()
class Canvas:
    def __init__(self, root, x, y, width, height):
        self.x = x
        self.y = y
        self.surface = pygame.Surface( (width, height) )
        root.addCanvas(self)
        
        self.tags={}
        self.values=[]

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
