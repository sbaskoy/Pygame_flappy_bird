# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:42:33 2019

@author: Salim
"""
from scipy import mat
import numpy  as np
import csv

import math
import random
class aktivayon_fonksiyonu:
    def sigmaid(x):
        s1=1/(1+math.exp(-x))        
        return s1
class Matrix:
    def __init__(self,satır,sütün):
        self.satır=satır
        self.sütün=sütün        
    def oluştur(self):
        matrix=[]
        for i in range(self.satır):
            matrix+=[[0] *self.sütün]
        
        return matrix 
    
   
"""Eger ara katman agırlıklarını siz vermek isterseniz dizi şeklinde
girdi verebilirsizniz dizinin tüm elemanlarını 0 yaparsanız
kendi random ahırlık verir  
"""   
class Yapay_Sinir_Ağı():
        def __init__(self,inputs=[],gizli_katman=[],çıkış_katmanı=[]):
            self.inputs=inputs
            self.gizli_katman=gizli_katman
            self.çıkış_katmanı=çıkış_katmanı            
            self.ara_agırlık=self.katman_agırlık_oluştur()[0]
            self.cıkış_agırlık=self.katman_agırlık_oluştur()[1]
            self.yaz=self.dosyaya_yazdır()
        def katman_agırlık_oluştur(self):            
            sayı=0
            ara_agırlık=[]
            cıkış_agırlık=[]
            for i in self.gizli_katman:            
                if(i==0):
                    sayı=sayı+1
                    if(sayı==len(self.gizli_katman)):
                        for i in range(len(self.inputs)*len(self.gizli_katman)):
                            a=random.random()
                            ara_agırlık.append(a)  
                  
            for i in range(len(self.gizli_katman)*len(self.çıkış_katmanı)):
                a=random.random()
                cıkış_agırlık.append(a)
            return ara_agırlık,cıkış_agırlık   
        """Yanlış Düzelt"""
        def ara_katman_cıkışları(self):           
                matris=Matrix(len(self.gizli_katman),len(self.inputs)).oluştur()
                cıkışlar=[]
                d=0
                for i in range(len(self.inputs)):
                    for j in range(len(self.gizli_katman)):
                        matris[j][i]=self.ara_agırlık[d]
                        d=d+1      
                for i in range(len(self.gizli_katman)):
                    t=0
                    for j in range(len(self.inputs)):
                        t+=matris[i][j]*self.inputs[j]
                    b=aktivayon_fonksiyonu.sigmaid(t)
                    cıkışlar.append(b)
                return cıkışlar    
        def cıkış_katman(self):
            matris=Matrix(len(self.cıkış_agırlık),len(self.ara_katman_cıkışları())).oluştur()
            sonuc=[]
            d=0
            for i in range(len(self.ara_katman_cıkışları())):                               
                for j in range(len(self.çıkış_katmanı)):
                    matris[j][i]=self.cıkış_agırlık[d]
                    d+=1
            for i in range(len(self.çıkış_katmanı)):
                t=0
                for j in range(len(self.ara_katman_cıkışları())):
                    t+=matris[i][j]*self.ara_katman_cıkışları()[j]
                b=aktivayon_fonksiyonu.sigmaid(t)
                sonuc.append(b)
            return sonuc
        """Buraya Kadar Gerekli İşlemler Yapılıp Sonuç Elde Ediliyor """
        """Geri Beslemeli Yapay Sinir Ağı """
        def hata(self):
            hata=self.çıkış_katmanı[0]-self.cıkış_katman()[0]
            return hata
        def agırlık_farkı(self):
            ögrenme_katsayısı=0.2
            momentum_katsayısı=0.6
            delta=[]
            d=0
            Em=self.hata()*(1-self.cıkış_katman()[0])*self.cıkış_katman()[0]
            for i in self.cıkış_agırlık:
                d=i*Em*ögrenme_katsayısı+momentum_katsayısı*d
                delta.append(d)
            return delta,Em
        def ara_katman_yeni_agırlıklar(self):
            yeni=[]
            for i in range(len(self.cıkış_agırlık)):
                yeni.append(self.cıkış_agırlık[i]+self.agırlık_farkı()[i])
            return yeni
        def ara_katman_deltaları(self):
            ara_katman_delta=[]
            d=0
            cıkışlar=self.ara_katman_cıkışları()
            for i in range(len(cıkışlar)):
                d=0
                d=cıkışlar[i]*(1+cıkışlar[i])*self.agırlık_farkı()[1]*self.cıkış_agırlık[i]
                ara_katman_delta.append(d)
            return ara_katman_delta
        def giriş_agırlık_farkı(self):
            giriş=self.inputs
            deltalar=self.ara_katman_deltaları()
            ög_katsayısı=0.2
            fark=[]
            for i in giriş:
                for j in deltalar:
                    d=0
                    d=ög_katsayısı*i*j
                    fark.append(d) 
            return fark
        def giriş_yeni_agırlıklar(self):
            giriş=self.ara_agırlık
            fark=self.giriş_agırlık_farkı()
            sonuc=[]
            for i in range(len(giriş)):
                    d=giriş[i]+fark[i]
                    sonuc.append(d)
            return sonuc 
        def dosyaya_yazdır(self):
            with open("dosya.csv","a",newline="") as dosya:
                yazıcı=csv.writer(dosya)
                yazıcı.writerow([self.ara_agırlık])
                yazıcı.writerow([self.cıkış_katman()])
                yazıcı.writerow([self.giriş_yeni_agırlıklar()])
             
            
ali=Yapay_Sinir_Ağı([0,0,0],[0,0,0],[0])
print(ali.cıkış_katman)
                