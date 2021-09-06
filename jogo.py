import pygame 
import random 
from moviepy.editor import *
from functions      import *

pygame.init      ()
pygame.mixer.init()

#Configs
tela = pygame.display.set_mode((  1280, 720))
pygame.display.set_caption("Caça ao Tesouro")
clock = pygame.time.Clock()

#Assets
menuintro            = VideoFileClip("assets/background/menuintro.mp4" )
menu                  = pygame.image.load("assets/background/menu.png" )
tabintro              = VideoFileClip("assets/background/tabintro.mp4" )
tab                   = pygame.image.load("assets/background/tab.png"  )
circulo_frames        = framelist ("circulo", 16, 5, "png")
tesouro_frames        = framelist("tesouro", 120, 5, "png")
kraken_frames         = framelist("kraken", 120, 5, "png")
x_frames              = framelist("x", 18, 5, "png")
jogador1_vez_frames   = framelist("1", 73, 5, "png")
jogador2_vez_frames   = framelist("2", 72, 5, "png")
frames_0_pont         = framelist("0", 108, 5, "png")
frames_0              = framelist("0", 60, 5, "png")
frames_1              = framelist("1", 60, 5, "png")
frames_2              = framelist("2", 60, 5, "png")
frames_3              = framelist("3", 60, 5, "png")
frames_4              = framelist("4", 60, 5, "png")
frames_50             = framelist("50", 108, 5, "png")
frames_100            = framelist("100", 108, 5, "png")
frames_150            = framelist("150", 108, 5, "png")
frames_200            = framelist("200", 108, 5, "png")
frames_250            = framelist("250", 108, 5, "png")
frames_300            = framelist("300", 108, 5, "png")
frames_350            = framelist("350", 108, 5, "png")
frames_400            = framelist("400", 108, 5, "png")
frames_450            = framelist("450", 108, 5, "png")
frames_500            = framelist("500", 108, 5, "png")
frames_550            = framelist("550", 108, 5, "png")
frames_600            = framelist("600", 108, 5, "png")
frames_jogador1venceu = framelist("1", 150, 5, "png")
frames_jogador2venceu = framelist("2", 150, 5, "png")
frames_selecvenceu    = framelist("selecvenceu", 20, 5, "png")
spritecirculo         = spritelist("assets/selecao/circulo/", circulo_frames) 
spritex               = spritelist("assets/selecao/x/", x_frames)
spritetesouro         = spritelist("assets/bau/tesouro/", tesouro_frames)
spritekraken          = spritelist("assets/bau/kraken/", kraken_frames)
spritejogador1        = spritelist("assets/vez/1/", jogador1_vez_frames)
spritejogador2        = spritelist("assets/vez/2/", jogador2_vez_frames)
sprite0pont           = spritelist("assets/numeros/0/pontuacao/", frames_0_pont)
sprite0               = spritelist("assets/numeros/0/individual/", frames_0)
sprite1               = spritelist("assets/numeros/1/", frames_1)
sprite2               = spritelist("assets/numeros/2/", frames_2)
sprite3               = spritelist("assets/numeros/3/", frames_3)
sprite4               = spritelist("assets/numeros/4/", frames_4)
sprite50              = spritelist("assets/numeros/50/", frames_50)
sprite100             = spritelist("assets/numeros/100/", frames_100)
sprite150             = spritelist("assets/numeros/150/", frames_150)
sprite200             = spritelist("assets/numeros/200/", frames_200)
sprite250             = spritelist("assets/numeros/250/", frames_250)
sprite300             = spritelist("assets/numeros/300/", frames_300)
sprite350             = spritelist("assets/numeros/350/", frames_350)
sprite400             = spritelist("assets/numeros/400/", frames_400)
sprite450             = spritelist("assets/numeros/450/", frames_450)
sprite500             = spritelist("assets/numeros/500/", frames_500)
sprite550             = spritelist("assets/numeros/550/", frames_550)
sprite600             = spritelist("assets/numeros/600/", frames_600)
spritejogador1venceu  = spritelist("assets/venceu/1/", frames_jogador1venceu)
spritejogador2venceu  = spritelist("assets/venceu/2/", frames_jogador2venceu)
spriteselecvenceu    = spritelist("assets/selecao/venceu/", frames_selecvenceu)

dict_num = {"0": sprite0, "1": sprite1, "2": sprite2, "3": sprite3,"4": sprite4}
dict_pont = {"0": sprite0pont, "50": sprite50, "100": sprite100, "150": sprite150, "200": sprite200, "250": sprite250, "300": sprite300, "350": sprite350, "400": sprite400, "450": sprite450, "500": sprite500, "550": sprite550, "600": sprite600}


def desenho():
    
    global circulocount
    global cont_tabintro
    global xcount
    global celula_x
    global celula_y
    global tesourocount
    global numcount
    global krakencount
    global tesouro_clicado
    global kraken_clicado
    global numero_clicado
    global celula_clicada_x
    global celula_clicada_y
    global click_bloqueado
    global jogador2count
    global jogador1count
    global jogador1
    global jogador2
    global pontcount1
    global pontcount2
    global pontuacao1_trocou 
    global pontuacao2_trocou
    global vez_jogador
    global selecvenceucount
    global venceucount
    global selec_possivel
    global jogar_novamente_selecionado 
    global jogar_novamente 

    if no_menu == True:
        tela.blit(menu, (0, 0))
        
        if jogar_selecionado == True:
            tela.blit(spritecirculo[circulocount], (0, 0))
            if circulocount + 1 >= len(spritecirculo):
                circulocount = len(spritecirculo) - 1
            else:
                circulocount += 1
        else:
            circulocount= 0
        
    else:
        if cont_tabintro == 0:
            tabintro.preview(30) 
            pygame.mixer.music.load("assets/musica/resto_musica_tabuleiro.ogg")
            pygame.mixer.music.play(-1)
            
        tela.blit(tab, (0,0))
        
        if pontuacao1_trocou == True:
            pontcount1 = 0
            pontuacao1_trocou = False
            
        if pontuacao2_trocou == True:
            pontcount2 = 0
            pontuacao2_trocou = False
        
        tela.blit((dict_pont[f"{pont[0]}"])[pontcount1], ((966, 295)))
        if pontcount1 >= 108 - 1:
            pontcount1 = 108 - 1
        else:
            pontcount1 += 1
            
        tela.blit((dict_pont[f"{pont[1]}"])[pontcount2], ((966, 520)))
        if pontcount2 >= 108 - 1:
            pontcount2 = 108 - 1
        else:
            pontcount2 += 1
        
        if cel_selecionada == True and tab_selecionado == True:
            tela.blit(spritex[xcount], ((61+(lado_celula+6)*celula_x, 46+(lado_celula+6)*celula_y)))
            if xcount + 1 >= len(spritex):
                xcount = len(spritex) - 1
            else:
                xcount +=1
        else:
            xcount = 0
            
        if tesouro_clicado == True:
            
            tupla = tesouros_abertos[f"{tesouros_abertos_n}"]
            
            tela.blit(spritetesouro[tesourocount], ((61+(lado_celula+6)*tupla[0], 3+(lado_celula+6)*tupla[1])))
            
            if tesourocount == len(spritetesouro) - 1:
                click_bloqueado = False
                tesouro_clicado = False
                tesouros_abertos_concluidos[f"{tesouros_abertos_n}"] = (tupla[0], tupla[1])
            else:
                tesourocount += 1
                
        else:
            tesourocount = 0
            
        if kraken_clicado == True:
            
            tupla = krakens_abertos[f"{krakens_abertos_n}"]
            
            tela.blit(spritekraken[krakencount], ((61+(lado_celula+6)*tupla[0], 3+(lado_celula+6)*tupla[1])))
            
            if krakencount == len(spritekraken) - 1:
                click_bloqueado = False
                kraken_clicado = False
                krakens_abertos_concluidos[f"{krakens_abertos_n}"] = (tupla[0], tupla[1])
                
            else:
                krakencount += 1
        else:
            krakencount = 0
            
        if numero_clicado == True:
            antetupla = numeros_abertos[f"{numeros_abertos_n}"]
            tupla = antetupla[1]
            tela.blit((dict_num[antetupla[0]])[numcount], ((61+(lado_celula+6)*tupla[0], 46+(lado_celula+6)*tupla[1])))
            
            if numcount == 60 - 1:
                click_bloqueado = False
                numero_clicado = False
                numeros_abertos_concluidos[f"{numeros_abertos_n}"] = (antetupla[0], antetupla[1])
            
            else:
                numcount += 1
        else:
            numcount = 0
            
        for i in tesouros_abertos_concluidos:
            tupla = tesouros_abertos_concluidos[i]
            tela.blit(spritetesouro[-1], ((61+(lado_celula+6)*tupla[0], 3+(lado_celula+6)*tupla[1])))
            
        for i in krakens_abertos_concluidos:
            tupla = krakens_abertos_concluidos[i]
            tela.blit(spritekraken[-1], ((61+(lado_celula+6)*tupla[0], 3+(lado_celula+6)*tupla[1])))
            
        for i in numeros_abertos_concluidos:
            antetupla = numeros_abertos_concluidos[i]
            tupla = antetupla[1]
            tela.blit((dict_num[antetupla[0]])[-1], ((61+(lado_celula+6)*tupla[0], 46+(lado_celula+6)*tupla[1])))
          
        if num_cel_abertas < 16: 
            if vez_jogador % 2 == 0 and click_bloqueado == False:
                tela.blit(spritejogador1[jogador1count], (0, 0))
                if jogador1count + 1 >= len(spritejogador1):
                    jogador1count = len(spritejogador1) - 1
                else:
                    jogador1count += 1
                    
            else:
                jogador1count = 0
                
            if vez_jogador %2 != 0 and click_bloqueado == False:
                tela.blit(spritejogador2[jogador2count], (0, 0))
                if jogador2count >= len(spritejogador2) - 1:
                    jogador2count = len(spritejogador2) - 1
                else:
                    jogador2count += 1
                    
            else:
                jogador2count = 0
            
        if fimdejogo == True:
            
            if pont[0] > pont[1]:
                tela.blit(spritejogador1venceu[venceucount], (0, 0))
                if venceucount >= len(spritejogador1venceu) - 1:
                    venceucount = len(spritejogador1venceu) - 1
                else:
                    venceucount += 1
                    
            else:
                tela.blit(spritejogador2venceu[venceucount], (0, 0))
                if venceucount >= len(spritejogador2venceu) - 1:
                    venceucount = len(spritejogador2venceu) - 1
                else:
                    venceucount += 1
                    
            if venceucount >= 71:
                selec_possivel = True
                    
            if jogar_novamente_selecionado == True and selec_possivel == True:
                tela.blit(spriteselecvenceu[selecvenceucount], (0, 0))
                if selecvenceucount >= len(spriteselecvenceu) - 1:
                    selecvenceucount = len(spriteselecvenceu) - 1
                          
                else:
                    selecvenceucount += 1
            else:
                selecvenceucount = 0
    
        else:
            venceucount = 0

        cont_tabintro = 1
        
    pygame.display.update()
    
jogar_novamente = True

while jogar_novamente:
    
    #Booleans
    no_menu           = True
    jogar_selecionado = False
    jogo_cancelado    = False
    fimdejogo         = False
    cel_selecionada   = False
    tab_selecionado   = False
    tesouro_clicado   = False
    kraken_clicado    = False
    numero_clicado    = False
    click_bloqueado   = False
    jogador1          = True
    jogador2          = False
    pontuacao1_trocou = True
    pontuacao2_trocou = True
    selec_possivel    = False
    jogar_novamente_selecionado = False
    jogar_novamente   = False
    
    #Dict de blits
    tesouros_abertos, tesouros_abertos_concluidos, tesouros_abertos_n = {}, {}, 0
    krakens_abertos, krakens_abertos_concluidos, krakens_abertos_n    = {}, {}, 0
    numeros_abertos, numeros_abertos_concluidos, numeros_abertos_n    = {}, {}, 0
    cont_tabintro    = 0
    numcount         = 0
    jogador1count    = 0
    jogador2count    = 0
    circulocount     = 0
    xcount           = 0
    tesourocount     = 0
    krakencount      = 0
    pontcount1       = 0
    pontcount2       = 0
    venceucount      = 0
    selecvenceucount = 0
    
    #Matrizes
    lado_celula  = 153
    num_linhas   = 4
    num_buracos  = 0
    num_tesouros = 0
    origem_tab   = (61,46)
    cont_celula  = [[None for i in range(num_linhas)] for j in range(num_linhas)]
    
            
    #Alocação de espaço para uma matriz 
    #Marca com 'X' 3 células (Baú vazio)
    while num_buracos < 3:
        i = random.randint(0, num_linhas - 1)
        j = random.randint(0, num_linhas - 1)
    
        if  cont_celula[i][j] == None:   #Checagem para ver se a célula está vazia 
            cont_celula[i][j] = 'X'
            num_buracos += 1
            
    #Marca com 'Y' 6 células (Baú tesouro)
    while num_tesouros < 6:
        i = random.randint(0, num_linhas - 1)
        j = random.randint(0, num_linhas - 1)
        
        if  cont_celula[i][j] == None:
            cont_celula[i][j] = 'Y'
            num_tesouros += 1
            
            
    #Verificação do número de 'Y' ao redor 
    for i in range(0, num_linhas):
        for j in range(0, num_linhas):
            
            if cont_celula[i][j] != 'Y' and cont_celula[i][j] != 'X':
                nb_tesouros_ao_redor = 0
                
                #Acima  #Avalia juntamente os limites do meu tabuleiro 
                if (i - 1) >= 0 and cont_celula[i - 1][j] == 'Y':
                    nb_tesouros_ao_redor += 1
                    
                #Esquerda
                if (j - 1) >= 0 and cont_celula[i][j - 1] == 'Y':
                    nb_tesouros_ao_redor += 1
                    
                    
                #Abaixo #Avaliação do limite muda
                if (i + 1) < num_linhas and cont_celula[i + 1][j] == 'Y':
                    nb_tesouros_ao_redor += 1
                
                #Direita
                if (j + 1) < num_linhas and cont_celula[i][j + 1] == 'Y':
                    nb_tesouros_ao_redor += 1
                    
                cont_celula[i][j] = str(nb_tesouros_ao_redor)
        
    
    cel_revelada = [[False for i in range(num_linhas)] for j in range(num_linhas)]
    
    num_cel_abertas = 0
    
    pont = [0,0]
    
    vez_jogador = 2
    
    menuintro.preview(30)
    pygame.mixer.music.load("assets/musica/resto_musica_menu.ogg")
    pygame.mixer.music.play(-1)
    
    #mainloop
    while not jogo_cancelado:
    
        clock.tick(30) 
        coords = pygame.mouse.get_pos()
    
        for evento in pygame.event.get():
            
            if evento.type == pygame.QUIT:
                jogo_cancelado = True
                break
            
            click = False
            
            if no_menu == True:
                
                mouse_x = coords[0]
                mouse_y = coords[1]
                
                if mouse_x > 70 and mouse_x < 320 and mouse_y > 404 and mouse_y < 568:
                    jogar_selecionado = True
                    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                        no_menu = False
                else:
                    jogar_selecionado = False
                
            else:
                mouse_x = coords[0] - 61
                mouse_y = coords[1] - 46
                
                #Localização das células
                celula_x = (mouse_x // 159)
                celula_y = (mouse_y // 159)
                
                if mouse_x > 0 and mouse_x < 627 and mouse_y > 0 and mouse_y < 630:
                    tab_selecionado = True
                else:
                    tab_selecionado = False
                    
                if tab_selecionado == True:
                    if cel_revelada[celula_x][celula_y] == False:
                        cel_selecionada = True
                    else:
                        cel_selecionada = False
                        
                if mouse_x > 397 and mouse_x < 768 and mouse_y > 483 and mouse_y < 595 and fimdejogo == True:
                    jogar_novamente_selecionado = True
                else:
                    jogar_novamente_selecionado = False
            
                #Evento que muda a tela mediante os cliques com o mouse
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and click_bloqueado == False:
                    
                    if jogar_novamente_selecionado == True:
                        jogar_novamente = True
                        break
                    
                    #Verificação do clique fora do tabuleiro 
                    if celula_x > (num_linhas - 1) or celula_x < 0 or celula_y > (num_linhas - 1) or celula_y < 0 :
                        continue            
                            
                    #Verificação se a célula foi clicada pela 1a vez:
                    if not cel_revelada[celula_x][celula_y]:
                        click = True
                        num_cel_abertas += 1
                        cel_revelada[celula_x][celula_y] = True
                        
                        #Atualizando as pontuações
                        if vez_jogador % 2 == 0:
                            if cont_celula[celula_x][celula_y] == 'Y':
                                pont[0] += 100
                                pontuacao1_trocou = True
                            
                            elif cont_celula[celula_x][celula_y] == 'X':
                                if (pont[0] - 50) < 0:
                                    pont[0] = 0
                                    pontuacao1_trocou = True
                                
                                else:
                                    pont[0] -= 50
                                    pontuacao1_trocou = True
                            
                            vez_jogador += 1
                            
                        else:
                            if cont_celula[celula_x][celula_y] == 'Y':
                                pont[1] += 100
                                pontuacao2_trocou = True
                            
                            elif cont_celula[celula_x][celula_y] == 'X':
                                if (pont[1] - 50) < 0:
                                    pont[1] = 0
                                    pontuacao2_trocou = True
                                
                                else:
                                    pont[1] -= 50
                                    pontuacao2_trocou = True
                            
                            vez_jogador += 1
                    
                    #Colocando desenhos e números na tela:  
                    if click == True and click_bloqueado == False:
                        i, j = celula_x, celula_y
                        
                        if cont_celula[i][j] == 'Y':
                            tesouros_abertos_n += 1
                            click_bloqueado = True
                            tesouro_clicado = True
                            tesouros_abertos[f"{tesouros_abertos_n}"] = (celula_x, celula_y)
                            
                        elif cont_celula[i][j] == 'X':
                            krakens_abertos_n += 1
                            click_bloqueado = True
                            kraken_clicado = True
                            krakens_abertos[f"{krakens_abertos_n}"] = (celula_x, celula_y)
                            
                        #If para escrever na tela a contagem de baús ao redor
                        elif cont_celula[i][j] != 'X' and cont_celula != 'Y':
                           numeros_abertos_n += 1
                           click_bloqueado = True
                           numero_clicado = True
                           numeros_abertos[f"{numeros_abertos_n}"] = ((cont_celula[i][j], (celula_x, celula_y)))
                            
        if num_cel_abertas == 16:
            fimdejogo = True
            
        if jogar_novamente == True:
            break
                            
        desenho()
    
    if jogo_cancelado == True: 
        jogar_novamente = False
        break
        
    if jogar_novamente == True:
        continue
    
pygame.quit()
 
 
