from pygame.locals import *

#main
root_width = 1200
root_height = 675
timer_clock = 60 #fps max

#Binder
dico_key = {"a":K_a,"z":K_z,"e":K_e,"r":K_r,"t":K_t,"y":K_y,"u":K_u,"i":K_i,
            "o":K_o,"p":K_p,"q":K_q,"s":K_s,"d":K_d,"f":K_f,"g":K_g,
            "h":K_h,"j":K_j,"k":K_k,"l":K_l,"m":K_m,"w":K_w,"x":K_x,"c":K_c,
            "v":K_v,"b":K_b,"n":K_n}

#general
g = 9.81

#movement
wall_speed = 8 #pixel per frame update

#collision
boxofsafety_length = 8 #in pixel

#Perso
p_right = "/right"
p_left = "/left"
p_run_right = "/run_right"
p_run_left = "/run_left"
