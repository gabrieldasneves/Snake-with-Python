import pygame as pg #importando a biblioteca que sera utilizada
from random import randint
# o pygame trabalha com RGB, ou seja, ele nao reconhece a cor branca
#para facilitar, vamos definir cores aqui
branco = (255,255,255) #tupla para a cor branca
roxo = (139,71,137)
verde = (0,255,127)
cinza = (143,143,143)
vermelho = (255,48,48) 
preto = (0,0,0)	



try: #verificando se a biblioteca ta iniciando
    pg.init() 
except:
    print("pygame.init() falhou")
    
    #_________________________________Variaveis de auxilio___________________________________________________
    
    
largura = 640 #definicoes para a tela do jogo
altura = 480 
tamanho = 10
relogio = pg.time.Clock() #relogio para controlar a quantidade de frames
    
     #__________________________________criando a tela do jogo_________________________________________________
    
back_ground = pg.display.set_mode((largura,altura)) #o parametro e dado como um par ordenado
pg.display.set_caption("Cobrinha") #colocando o titulo do jogo na janela
    
    
    #__________________________________funcao cobra__________________________________________________________

def cobra(coord_cobra): #funcao para criar a cobra
    for x in coord_cobra:     
        pg.draw.rect(back_ground, verde, [x[0],x[1],10,10]) #desenhando o retangulo inicial da cobrinha

    #__________________________________funcao maca___________________________________________________________

def maca(position_maca_x, position_maca_y):
    pg.draw.rect(back_ground, vermelho, [position_maca_x,position_maca_y,10,10]) #desenhando o retangulo da maca

def jogo():  #criando a funcao jogo, que sera o nosso jogo com o while 

    #_________________________________Variaveis de auxilio___________________________________________________

    sair = True #variavel para quebrar os loops quando necessario
    # coordenadas para criar a cobra
    position_x_axis = randint(0,(largura-tamanho)/10)*10
    position_y_axis = randint(0,(altura-tamanho)/10)*10
    
    velocidade_x=0 ##definindo velocidades iniciais da cobra
    velocidade_y=0
    
    # criando as coordenadas da maca
    position_maca_x = randint(0,(largura-tamanho)/10)*10
    position_maca_y = randint(0,(altura-tamanho)/10)*10
    
    coord_cobra = [] #nossa cobra, esta mais explicado la em baixo
    cont_cobra = 1    
    #___________________________________loop para rodar o jogo___________________________________________________________
    
    while(sair): 
        for event in pg.event.get(): #varrendo todos os eventos que estao acontecendo nesse momento
            if event.type == pg.QUIT: #pegando o evento de apertar no x para sair da tela
                sair = False
            if event.type == pg.KEYDOWN : # Pegando evento  pressionar tecla e desabilitando voltar no mesmo sentido
                if event.key == pg.K_LEFT and velocidade_x!=tamanho: # se o evento for pressionar tecla para esquerda
                    #position_x_axis = position_x_axis - 10  # a posicao  no eixo x diminui
                    velocidade_y=0
                    velocidade_x=-tamanho
            if event.type == pg.KEYDOWN: # Pegando evento  pressionar tecla
                if event.key == pg.K_RIGHT and velocidade_x!= -tamanho: # se o evento for pressionar tecla para direita
                    #position_x_axis = position_x_axis + 10  # a posicao  no eixo x aumenta
                    velocidade_y=0
                    velocidade_x=tamanho
            if event.type == pg.KEYDOWN: # Pegando evento  pressionar tecla
                if event.key == pg.K_UP and velocidade_y!=tamanho: # se o evento for pressionar tecla para cima
                    #position_y_axis = position_y_axis - 10  # a posicao  no eixo y aumenta
                    velocidade_x=0
                    velocidade_y=-tamanho
            if event.type == pg.KEYDOWN: # Pegando evento  pressionar tecla
                if event.key == pg.K_DOWN and velocidade_y!= -tamanho: # se o evento for pressionar tecla para baixo
                    #position_y_axis = position_y_axis + 10  # a posicao  no eixo y diminui
                    velocidade_x=0
                    velocidade_y=tamanho
        back_ground.fill(branco) #preenche a tela com um fundo de cor branca
        
        # aqui vamos fazer uma estrutura para facilitar a implementacao do crescimento da cobra
        cobra_cabeca = []
        cobra_cabeca.append(position_x_axis)
        cobra_cabeca.append(position_y_axis)        
        coord_cobra.append(cobra_cabeca)        
        cobra(coord_cobra) #funcao para gerar a cobra no jogo
        
        if len(coord_cobra) > cont_cobra:
            del coord_cobra[0]
            
        
        #agora vamos criar a regra do crescimento
        if position_x_axis == position_maca_x and position_y_axis == position_maca_y:
            #quando a cobra encontra a maca
            position_maca_x = randint(0,(largura-tamanho)/10)*10#cria-se uma nova maca aleatorimente
            position_maca_y = randint(0,(altura-tamanho)/10)*10
            cont_cobra += 1
        


        maca(position_maca_x, position_maca_y)
        position_x_axis+=velocidade_x
        position_y_axis+=velocidade_y
        pg.display.update()
        relogio.tick(15)
        
    #________________________________CONDICAO DE BORDA - atravessa aborda_______________________________________________________________    
    
    #    if position_x_axis > largura:
    #        position_x_axis = 0
    #    if position_x_axis < 0:
    #        position_x_axis = largura
    #    if position_y_axis > altura:
    #        position_y_axis = 0
    #    if position_y_axis < 0:
    #        position_y_axis = altura
    
    #________________________________CONDICAO DE BORDA - morre na borda_______________________________________________________________    
    
    
        if position_x_axis > largura:
            sair = False
        if position_x_axis < 0:
            sair = False
        if position_y_axis > altura:
            sair = False
        if position_y_axis < 0:
            sair = False
            
            
    #_________________________________________chamada de funcoes_____________________________________________________________________
            
jogo() #chamando o jogo para jogar            
pg.quit() #fechando a janela
