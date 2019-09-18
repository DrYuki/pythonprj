# 算武器升级要不要放幸运石
import numpy as np

star = 5 # 星钻5
moon = 20 # 月光宝石
price = {"star": 5,"moon":20}
weaponlist= {8:{"rate": 0.69, "price": price["moon"]*9,"sliver":50000}}
weaponlist.update ({7:{"rate": 0.80, "price": price["moon"]*6,"sliver":40000}})
weaponlist.update ({9:{"rate": 0.60, "price": price["moon"]*12,"sliver":60000}})
weaponlist.update ({10:{"rate": 0.50, "price": price["moon"]*16,"sliver":40000}})
weaponlist.update ({11:{"rate": 0.40, "price": price["moon"]*18,"sliver":40000}})
weaponlist.update ({12:{"rate": 0.20, "price": price["moon"]*21,"sliver":40000}})
weaponlist.update ({13:{"rate": 0.20, "price": price["moon"]*6,"sliver":40000}})
weaponlist.update ({14:{"rate": 0.12, "price": price["moon"]*6,"sliver":40000}})
weaponlist.update ({15:{"rate": 0.10, "price": price["moon"]*6,"sliver":40000}})


nothing = {"name": "none", "rate": 0, "price":0}
luck = {"name": "luck", "rate": 0.05, "price":60}
luck_sup = {"name": "luck_sup", "rate": 0.15, "price": 350}

weapon = weaponlist[10]

luckdit = {0: nothing, 1: luck, 2: luck_sup}
showlist ={}

totallist = []
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            ratetotal = weapon["rate"] +luckdit[i]["rate"]+luckdit[j]["rate"]+luckdit[k]["rate"]
            if(ratetotal<=1.15):
                p1 = weapon["price"] + luckdit[i]["price"]+luckdit[j]["price"]+luckdit[k]["price"]
                total_price = 1/ratetotal*p1
                show = {total_price: [ratetotal, luckdit[i]["name"], luckdit[j]["name"], luckdit[k]["name"]]}
                showlist.update(show)

s = sorted(showlist.items(), key=lambda x:x[0])
s = dict(s)

for key in s:
    print(key, s[key])