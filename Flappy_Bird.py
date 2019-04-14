# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 07:17:56 2019

@author: Salim
"""

import pygame
import random
import neuralnetwork
import time
pygame.init()

oyun_alanı_genişlik=700
oyun_alanı_yükseklik=500
siyah=(0,0,0)
beyaz=(255,255,255)
mavi=(0,0,225)
red=(255,0,0)

oyun_alanı=pygame.display.set_mode((oyun_alanı_genişlik,oyun_alanı_yükseklik))
pygame.display.set_caption("Flappy Bird")
oyun_alanı.fill(siyah)
saat=pygame.time.Clock()

def Boru_oluştur():
     boru1 = Kare(None);
     boru1_height= oyun_alanı_yükseklik - boru1.yükseklik - boşluk;
     boru2 = Kare(boru1_height);
     return boru1,boru2



class Kuş:
    def __init__(self,y_kord):
        self.x_kord=100
        self.y_kord=y_kord
        self.r=10
        self.gravity=0
        self.ivme=0.1
    def çiz(self):
        pygame.draw.circle(oyun_alanı,beyaz,(self.x_kord,round(self.y_kord)),self.r)
    def güncelle(self):
        self.gravity+=self.ivme
        self.gravity=min(4,self.gravity)
        self.y_kord+=self.gravity
        
        

boşluk=100
min_boru_boyutu=40
class Kare:
    def __init__(self,height):
        self.x_kord=700
        self.y_kord=self.kareY(height)
        self.genişlik=50
        self.yükseklik=self.kareH(height)
        
    def kareY(self,height):
        if height!=None:
            return oyun_alanı_yükseklik-height
        else:
            return 0
    def kareH(self,height):
        if height!=None:
            return height
        else:
           return min_boru_boyutu+random.random()*(oyun_alanı_yükseklik-boşluk-min_boru_boyutu*2)
       
    def çiz(self):
        pygame.draw.rect(oyun_alanı,beyaz,[self.x_kord,self.y_kord,self.genişlik,self.yükseklik])

def yanma():
    font=pygame.font.Font("freesansbold.ttf",115)
    yazı=font.render("Yandınız",True,beyaz)
    kare=yazı.get_rect()
    kare.center=(oyun_alanı_genişlik/2,oyun_alanı_yükseklik/2)
    oyun_alanı.blit(yazı,kare)
    pygame.display.update()
    time.sleep(2)
    Oyun()
    
     
def Oyun():
    kuş_y_kord=100
    kuş=Kuş(kuş_y_kord)
    borular=list(Boru_oluştur())
    sayıcı=0
    
    while True:
        sayıcı+=1
        
        if sayıcı%100==0:
            boru=Boru_oluştur()
            borular+=boru
        
        oyun_alanı.fill(siyah)
        kuş.çiz()
        for i in borular:
            i.x_kord-=5
            i.çiz()
            if i.x_kord<0:
                borular.remove(i)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:         
                pygame.quit()       
            if event.type==pygame.KEYDOWN:           
                if event.key==32 :
                    kuş.ivme=-2                        
            if event.type==pygame.KEYUP:
                kuş.ivme=1
                
        
        
        kuş.güncelle()
        """beyin=neuralnetwork.Yapay_Sinir_Ağı([kuş.y_kord/oyun_alanı_yükseklik,kuş.x_kord/oyun_alanı_genişlik,0.001,],[0,0,0],[0])
        if beyin.cıkış_katman()[0]<0.5:
            print(beyin.cıkış_katman()[0])
            kuş.ivme=-2
        else:
            kuş.ivme=-1
            print(beyin.cıkış_katman()[0])
        """
        if kuş.y_kord+kuş.r>oyun_alanı_yükseklik:
            kuş.y_kord=0-kuş.y_kord
        for i in borular:
            if   i.x_kord<kuş.x_kord<i.x_kord+i.genişlik and i.y_kord+i.yükseklik>kuş.y_kord>i.y_kord:
                yanma()
        
        
        
        pygame.display.flip()
        saat.tick(60)
      
Oyun()





