class Player():
    counter = 0
    def __init__(self, objects, animation):
        self.tag = "perso" + str(Perso.counter)
        Player.counter += 1
        self.objects = objects
        self.animation = animation
        self.subfolder_sprites = None
        self.ticks = pygame.time.get_ticks

        self.position = None
        self.velocity = []
        self.acceleration = []

    def subfolder_sprites(self, subfolder):
        self.subfolder_sprites = subfolder

    def spawn(self, x, y, xp=0, yp=0, xpp=0, ypp=0):
        self.position = [x, y]
        self.add_velocity(xp, yp)
        self.add_acceleration(xpp, ypp)
        #self.animation.start(self.subfolder+p_right, x, y, -1, self.tag)
        perso=pygame.Surface( (50,100) )
        perso.fill((50,50,50))
        self.objects.add(perso, self.position[0], self.position[1], self.tag)

    def add_acceleration(self, x, y):
        if x != 0 or y != 0:
            self.acceleration += [[x, y, 0, 0, 0]]

    def add_velocity(self, x, y):
        if x != 0 or y != 0:
            self.velocity += [[x, y, 0]]

    def move(self, x, y):
        self.objects.move(self.tag, x, y)

    def refresh(self):
        incr_x = 0
        incr_y = 0
        for acc in self.acceleration:
            #acc[2] et acc[3] sont la valeur entre deux temps (ticks)
            tick = self.ticks()
            acc[2] = 0.5*acc[0]*( ((tick-acc[4])/1000)*((tick-acc[4])/1000) ) - acc[2]
            acc[3] = 0.5*acc[1]*( ((tick-acc[4])/1000)*((tick-acc[4])/1000) ) - acc[3]
            incr_x += acc[2]
            incr_y += acc[3]

        for vel in self.velocity:
            #ici on calcul direct la différence
            tick = self.ticks()
            incr_x += vel[0]*(tick-vel[2])/1000
            incr_y += vel[1]*(tick-vel[2])/1000
            vel[2] = tick

        self.move(incr_x, incr_y)
