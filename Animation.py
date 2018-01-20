class Animation():
    def __init__(self, objects):
        self.dico={}
        self.list=[]
        self.load()
        self.objects=objects
        self.ticks = pygame.time.get_ticks
        self.uid = 0

    def load(self):
        for folder in os.listdir("animation"):
            for subfolder in os.listdir(os.path.join("animation",folder)):
                self.dico[folder+"/"+subfolder]=[]
                for i in range(len(os.listdir(os.path.join("animation",folder,subfolder)))):
                    path=subfolder+str(i)+".png"
                    frame=pygame.image.load(os.path.join("animation",folder,subfolder,path)).convert()
                    self.dico[folder+"/"+subfolder]+=[frame]

    def start(self, name, posx, posy, time, repetition, tag):
        path=os.path.join("animation",name)
        N=len(os.listdir(path))
        self.list+=[[name, posx, posy ,time, repetition, tag, N, self.ticks(), tag+self.get_uid()]]
        print(self.list)

    def find(self):
        for i, [name, posx, posy, time, repetition, tag, N, ticks, tag2] in enumerate(self.list):
            nb_img = (N*(self.ticks()-ticks)) // time
            if nb_img < (N*repetition):
                self.objects.del_tag(tag2)
                self.objects.add(self.dico[name][nb_img%N], posx, posy, tag2)
            else:
                self.stop_uid(tag2)

    def move(self, tag, x, y):
        for anim in self.list:
            if anim[5]==tag:
                anim[1]+=x
                anim[2]+=y

    def stop_uid(self, tag2):
        self.objects.del_tag(tag2)
        for i, anim in enumerate(self.list):
            if anim[8]==tag2:
                self.list.pop(i)

    def stop(self, tag):
        self.objects.del_tag(tag)
        for i, anim in enumerate(self.list):
            if anim[5]==tag:
                self.list.pop(i)

    def get_uid(self):
        self.uid += 1
        return str(self.uid - 1)
