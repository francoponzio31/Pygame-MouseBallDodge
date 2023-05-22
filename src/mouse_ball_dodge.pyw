import pygame, sys, random  
from math import sin, sqrt

pygame.init()

# SETEOS Y CONFIGURACIONES PREVIAS:

pantalla = pygame.display.set_mode((1200,700))
pygame.display.set_caption("__MOUSE BALL DODGE__")

# OCULTAR EL PUNTERO DEL MOUSE:
pygame.mouse.set_visible(False)

# Fuentes:
fuente_cuenta_regresiva_y_game_over = pygame.font.SysFont("Verdana", 55)
fuente_puntaje = pygame.font.SysFont("Verdana", 18)
color_fuente = (120,120,120)

# Clock:
clock = pygame.time.Clock()

# Color fondo:
color_fondo = "#303030"

# --------------- Funcion que chequea la colision con la bola blanca (Jugador) -----------------------

def colision_con_bola_blanca(radio_enemigo, coord_x_enemigo, coord_y_enemigo):

    radio_bola_blanca = 38.5

    distancia_bola_blanca_enemigo = sqrt((coord_x_mouse - coord_x_enemigo-radio_enemigo)**2 + (coord_y_mouse - coord_y_enemigo-radio_enemigo)**2)

    if distancia_bola_blanca_enemigo < radio_enemigo + radio_bola_blanca:
        return True
    else:
        return False   

# ------------------ Clase bola -----------------------------

class Bola:

    def __init__(self, color, coord_x, coord_y, speed_x, speed_y, radio):
    
        self.color = color
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radio = radio
        self.activacion = False


# -------------------------- Efectos de sonido ---------------------------------

cuenta_regresiva_sfx_1 = pygame.mixer.Sound("media\Cuenta_regresiva_sfx_1.wav")
cuenta_regresiva_sfx_2 = pygame.mixer.Sound("media\Cuenta_regresiva_sfx_2.wav")
bola_negra_sfx =  pygame.mixer.Sound("media\Bola_negra_sfx.wav")
colision_sfx = pygame.mixer.Sound("media\Colision_sfx.wav")


# ---------- Variables que no quiero reiniciar al empezar una nueva partida ----------
acumulador_tiempo_pasado_partidas_pasadas = 0
high_score = 0


# BUCLE DE PARTIDAS:
while True:

    # CREACION DE LOS OBJETOS BOLAS:

    # bola_blanca:
    bola_blanca = Bola(color = "#CCCBCB", coord_x = None, coord_y = None, speed_x = None, speed_y = None, radio = 38.5)

    # bola_roja:
    bola_roja = Bola(color = "#C70039", coord_x = 1240, coord_y = 70, speed_x = -1.8, speed_y = 2.7, radio = 51)
    bola_roja.en_pantalla = False

    # bola_violeta:
    bola_violeta = Bola(color = "#96429B", coord_x = -160, coord_y = 245, speed_x = 1, speed_y = None, radio = 51.5)

    # bola_amarilla:
    bola_amarilla = Bola(color = "#FFC801", coord_x = -171, coord_y = 250, speed_x = 3.8, speed_y = 0.9, radio = 66)
    bola_amarilla.en_pantalla = False

    # bola_azul:
    bola_azul = Bola(color = "#335189", coord_x = 1240, coord_y = 200, speed_x = -5, speed_y = 0.9, radio = 61)
    bola_azul.en_pantalla = False

    # bola_verde:
    bola_verde = Bola(color = "#1E8449", coord_x = None, coord_y = None, speed_x = random.uniform(2, 5.5), speed_y = random.choice((-0.8, 0.8)), radio = 81.5)
    bola_verde.coord_x_inicial = random.choice((-202, 1364))
    bola_verde.coord_y_inicial = random.randrange(20, 680, 20)
    bola_verde.coord_x = bola_verde.coord_x_inicial
    bola_verde.coord_y = bola_verde.coord_y_inicial

    # bola_negra:
    bola_negra = Bola(color = "#202020", coord_x = 1240, coord_y = 280, speed_x = None, speed_y = None, radio = 85)


    # ------------------ Variables del juego -------------------------

    game_over = False
    numero_cuenta_regresiva = ""
    score = 0

    # ------------ BUCLE PRINCIPAL --------------------------------
    while True:

        for evento in pygame.event.get():
        
            # Configuracion del cierre de la ventana:
            if evento.type == pygame.QUIT:
                sys.exit()

        # CRONOMETRO
        tiempo_pasado_partida_actual = round(pygame.time.get_ticks()/1000) - acumulador_tiempo_pasado_partidas_pasadas
            
        # COORDENADAS DEL JUGADOR (BOLA BLANCA) TOMADAS DEL MOUSE:
        coord_x_mouse, coord_y_mouse = pygame.mouse.get_pos()   
        bola_blanca.coord_x = coord_x_mouse 
        bola_blanca.coord_y = coord_y_mouse 

        # --------------- ACTIVACION ----------------------
        if tiempo_pasado_partida_actual == 7:  
            bola_roja.activacion = True
        if tiempo_pasado_partida_actual == 13:
            bola_violeta.activacion = True
        if tiempo_pasado_partida_actual == 18:   
            bola_amarilla.activacion = True 
        if tiempo_pasado_partida_actual == 23: 
            bola_azul.activacion = True
        if tiempo_pasado_partida_actual == 28:    
            bola_verde.activacion = True    
        if tiempo_pasado_partida_actual == 46:
            if bola_negra.activacion == False:
                bola_negra_sfx.play()    
            bola_negra.activacion = True

        #--------------- IMPRESION DE IMAGENES -------------------
        pantalla.fill(color_fondo)

        pygame.draw.circle(pantalla, bola_blanca.color, (bola_blanca.coord_x, bola_blanca.coord_y), bola_blanca.radio)

        # Cuenta regresiva:
        if tiempo_pasado_partida_actual < 6:
                
            if tiempo_pasado_partida_actual == 2:
                if numero_cuenta_regresiva == "":
                    cuenta_regresiva_sfx_1.play()
                numero_cuenta_regresiva = "3"
            elif tiempo_pasado_partida_actual == 3:
                if numero_cuenta_regresiva == "3":
                    cuenta_regresiva_sfx_1.play()            
                numero_cuenta_regresiva = "2"    
            elif tiempo_pasado_partida_actual == 4:
                if numero_cuenta_regresiva == "2":
                    cuenta_regresiva_sfx_1.play()            
                numero_cuenta_regresiva = "1"   
            elif tiempo_pasado_partida_actual == 5:
                if numero_cuenta_regresiva == "1":
                    cuenta_regresiva_sfx_2.play()
                numero_cuenta_regresiva = "DODGE !!!"

            cuenta_regresiva = fuente_cuenta_regresiva_y_game_over.render((numero_cuenta_regresiva), True, (170,170,170))
            pantalla.blit(cuenta_regresiva, ((1200 - cuenta_regresiva.get_width())/2, 300))

        # ------Impresion puntaje -------
        # score:     
        if tiempo_pasado_partida_actual >= 6:
            score = 2*(tiempo_pasado_partida_actual - 6) 
        impresion_score = fuente_puntaje.render( f"Score: {score}", True, (180,180,180))
        pantalla.blit(impresion_score, (8, 2))
        # High score:
        impresion_highscore = fuente_puntaje.render( f"High Score: {high_score}", True, (180,180,180))
        pantalla.blit(impresion_highscore, (8, 22))        


        # Enemigos:
        if bola_roja.activacion == True:  
            pygame.draw.circle(pantalla, bola_roja.color, (bola_roja.coord_x+bola_roja.radio,bola_roja.coord_y+bola_roja.radio), bola_roja.radio)
        
        if bola_violeta.activacion == True:
            pygame.draw.circle(pantalla, bola_violeta.color, (bola_violeta.coord_x+bola_violeta.radio,bola_violeta.coord_y+bola_violeta.radio), bola_violeta.radio)

        if bola_amarilla.activacion == True:  
            pygame.draw.circle(pantalla, bola_amarilla.color, (bola_amarilla.coord_x+bola_amarilla.radio,bola_amarilla.coord_y+bola_amarilla.radio), bola_amarilla.radio)  

        if bola_azul.activacion == True:
            pygame.draw.circle(pantalla, bola_azul.color, (bola_azul.coord_x+bola_azul.radio,bola_azul.coord_y+bola_azul.radio), bola_azul.radio)

        if bola_verde.activacion == True:  
            pygame.draw.circle(pantalla, bola_verde.color, (bola_verde.coord_x+bola_verde.radio,bola_verde.coord_y+bola_verde.radio), bola_verde.radio)
    
        if  bola_negra.activacion == True: 
            pygame.draw.circle(pantalla, bola_negra.color, (bola_negra.coord_x+bola_negra.radio,bola_negra.coord_y+bola_negra.radio), bola_negra.radio)

        # ------------ MOVIMIENTO ENEMIGOS: --------------

        # bola_roja:
        if bola_roja.activacion == True:  

            if bola_roja.coord_x < 1098:
                bola_roja.en_pantalla = True # Activo el rebote horizontal una vez que entra en pantalla
            if bola_roja.en_pantalla:
                if bola_roja.coord_x < 0 or bola_roja.coord_x > 1098:
                    bola_roja.speed_x *= -1

            if bola_roja.coord_y < 0 or bola_roja.coord_y > 598:
                bola_roja.speed_y *= -1

            bola_roja.coord_x += bola_roja.speed_x
            bola_roja.coord_y += bola_roja.speed_y 

        # bola_violeta:
        if bola_violeta.activacion == True:
            bola_violeta.coord_x += bola_violeta.speed_x
            bola_violeta.coord_y += 3.25*sin(bola_violeta.coord_x/100)

            if bola_violeta.coord_x > 1205:
                bola_violeta.coord_x = -140
                bola_violeta.coord_y = 245

        # bola_amarilla:
        if bola_amarilla.activacion == True:  

            if bola_amarilla.coord_x > 0:
                bola_amarilla.en_pantalla = True
            if bola_amarilla.en_pantalla:    
                if bola_amarilla.coord_x < 0 or bola_amarilla.coord_x > 1068:
                    bola_amarilla.speed_x *= -1

            if bola_amarilla.coord_y < 0 or bola_amarilla.coord_y > 568:
                bola_amarilla.speed_y *= -1

            bola_amarilla.coord_x += bola_amarilla.speed_x
            bola_amarilla.coord_y += bola_amarilla.speed_y

        # bola_azul:
        if bola_azul.activacion == True:

            if bola_azul.coord_x < 1078:
                bola_azul.en_pantalla = True
            if bola_azul.en_pantalla:    
                if bola_azul.coord_x < 0 or bola_azul.coord_x > 1078:
                    bola_azul.speed_x *= -1

            if bola_azul.coord_y < 0 or bola_azul.coord_y > 578:
                bola_azul.speed_y *= -1

            bola_azul.coord_x += bola_azul.speed_x
            bola_azul.coord_y += bola_azul.speed_y

        # bola_verde:
        if bola_verde.activacion == True: 

            if bola_verde.coord_x_inicial == -202:
                bola_verde.coord_x += bola_verde.speed_x
            elif bola_verde.coord_x_inicial == 1364:
                bola_verde.coord_x -= bola_verde.speed_x    
            
            bola_verde.coord_y += bola_verde.speed_y

            if bola_verde.coord_x > 3172 or bola_verde.coord_x < -2010:
                bola_verde.coord_x_inicial = random.choice((-202, 1364))
                bola_verde.coord_y_inicial = random.randrange(20, 680, 20)
                bola_verde.coord_x = bola_verde.coord_x_inicial
                bola_verde.coord_y = bola_verde.coord_y_inicial
                bola_verde.speed_x = random.uniform(2, 5.5)
                bola_verde.speed_y = random.choice((-0.8, 0.8))

        # bola_negra:
        if  bola_negra.activacion == True: 

            if bola_negra.coord_x < (bola_blanca.coord_x - 46.5):
                bola_negra.speed_x = 0.8
            elif bola_negra.coord_x > (bola_blanca.coord_x - 46.5):
                bola_negra.speed_x = -0.8    

            if bola_negra.coord_y < (bola_blanca.coord_y - 46.5):
                bola_negra.speed_y = 0.8
            elif bola_negra.coord_y > (bola_blanca.coord_y - 46.5):
                bola_negra.speed_y = -0.8        

            bola_negra.coord_x += bola_negra.speed_x
            bola_negra.coord_y += bola_negra.speed_y


        # ------ COLISIONES -------

        # Con bola_roja:
        if colision_con_bola_blanca(bola_roja.radio, bola_roja.coord_x, bola_roja.coord_y):  
            game_over = True   
        
        # Con bola_violeta:
        if colision_con_bola_blanca(bola_violeta.radio, bola_violeta.coord_x, bola_violeta.coord_y):  
            game_over = True

        # Con bola_amarilla:
        if colision_con_bola_blanca(bola_amarilla.radio, bola_amarilla.coord_x, bola_amarilla.coord_y):  
            game_over = True

        # Con bola_azul31:
        if colision_con_bola_blanca(bola_azul.radio, bola_azul.coord_x, bola_azul.coord_y): 
            game_over = True 

        # Con bola_verde:
        if colision_con_bola_blanca(bola_verde.radio, bola_verde.coord_x, bola_verde.coord_y):  
            game_over = True
        
        # Con el bola_negra:
        if colision_con_bola_blanca(bola_negra.radio, bola_negra.coord_x, bola_negra.coord_y):  
            game_over = True
                
        # ------------------------- GAME OVER -------------------------------

        if game_over == True:

            # Puntaje:
            if score > high_score:
                high_score = score
            score = 0    

            acumulador_tiempo_pasado_partidas_pasadas += tiempo_pasado_partida_actual
            
            colision_sfx.play()

            # Actualizo pantalla para que se actualize la posicion de los objetos en la pantalla:
            pygame.display.flip() 

            # Mensaje de game over:
            mensaje_game_over = fuente_cuenta_regresiva_y_game_over.render("YOU LOSE !!!", True, color_fuente)
            pantalla.blit(mensaje_game_over,((1200 - mensaje_game_over.get_width())/2, 300))
            pygame.display.flip()

            # Paro unos segundos el programa para que se vea el mensaje:
            pygame.time.delay(1500)

            # Fin de la partida:
            game_over = False

            break        
     
        # -------------------- Actualizo pantalla ---------------------------
        pygame.display.flip()

        clock.tick(120)