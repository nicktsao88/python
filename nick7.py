import nick6
print("歡迎使用計算機")
a=0
while a!=-1 :
    try :
        a=int(input("輸入 \n1是加法 \n2是減法 \n3是乘法 \n4是除法 \n5是平方 \n6是開方 \n-1離開"))
        if a==-1 :
            break
        c=float(input("輸入數字"))
        d=float(input("輸入數字"))
    except (TypeError,ValueError,NameError) :
        print("好玩嗎?")
        continue
    if(a==1) :
         nick6.add(c,d)
    elif(a==2) :
        nick6.remove(c,d)
    elif(a==3) :
        nick6.mulity(c,d)
    elif(a==4) :
        while(d==0) :
            d=float(input("想讓我當機沒門\n輸入數字"))
        nick6.dived(c,d)
    elif(a==5) :
        nick6.s(c,d)
    elif(a==6) :
        c=float(input("要開的數字"))
        d=int(input("你要開幾次方"))
        nick6.a(c,d)
    elif (a==-1) :
        print("ㄅㄅ")
    else :
        print("別玩我");






































































