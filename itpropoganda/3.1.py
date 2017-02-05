# -*- coding: utf-8 -*-
borcht = 2.75 # на 100
pelmeni = 2.19 # 100
kompot = 1.24 # 50
porciy_borcht = 100//borcht
print(porciy_borcht) #36
sdacha_borcht = 100%borcht
sdacha_borcht = round(sdacha_borcht, 2)
print(sdacha_borcht) # 1 c борща орфициану

porciy_pelmeni = 100//pelmeni
print(porciy_pelmeni) #45
sdacha_pelmeni = 100%pelmeni
sdacha_pelmeni = round(sdacha_pelmeni, 2) # округлили до 2 сотых
print(sdacha_pelmeni) # 1,45 c пельмень орфициану

porciy_kompot = 100//kompot
print(porciy_kompot) #80
sdacha_kompot = 100%kompot
sdacha_kompot = round(sdacha_kompot, 2)
print(sdacha_kompot) # 0,8 c пельмень орфициану

total = sdacha_kompot + sdacha_pelmeni + sdacha_borcht
print(total)