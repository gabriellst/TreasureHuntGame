import pygame

def framelist (nome, frames, digitos, formato):

    lista = [None]*frames
        
    for i in range(frames):
        
        n = "0"*digitos
        
        if i < 10:
            n = n[0:-1] + str(i)
            
        elif i >= 10 and i < 100:
            n = n[0:-2] + str(i)
            
        elif i >= 100 and i < 1000:
            n = n[0:-3] + str(i)
            
        lista[i] = nome + "_" + n + "." + formato
        
    return lista
        
def spritelist (destino, spritelist):
    lista = [None]*len(spritelist)
    
    for i in range(len(spritelist)):
        lista[i] = pygame.image.load(str(destino + spritelist[i]))
        
        
    return lista
    
