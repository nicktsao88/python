a=0
while a<3 :
    a=int(input("輸入 1為華氏 2為攝氏 3跳出 "))
    if a==1 :
            F=float(input("輸入華氏溫度"))
            C=(F-32)*5/9
            print("攝氏為",C)

    if a==2 :
            C=float(input("輸入攝氏溫度"))
            F=9*C/5+32
            print("現在華氏為",F)
    
    if a== 3:
            print("ㄅㄅ")

    if a>3 or a<=0:
            print("不要亂玩")


