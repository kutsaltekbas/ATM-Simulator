import random as rnd
print("""
... [H]===========HOLYSOFT=========[-][o][x]
... |                                      |
... |     ATM işlem geçmişi görüntüleme    |
... |       programına hoşgeldiniz!        |
... |      Devam etmek için herhangi       |
... |          bir tuşa basın.             |
... |                                      |
... |======================================|
... """)
input()
bn = [[10, 175], [20, 150], [50, 125], [100, 100], [200, 75]] #banknotlar
tplm_para, cklck_para,i,y,e,yi,o, ytrlck_para,cek,bs,üye_no,py_üye_no,g = 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0 #değişkenler
c_iy,c_y,c_e,c_yi,c_o,y_iy,y_y,y_e,y_yi,y_o = 0,0,0,0,0,0,0,0,0,0#çekilecek ve yatırılacak banknot adetleri
giris = True # para yatıracak kişi koşuluna giriş değişkeni
saat1 = 0
saat2 = 8
dakika1 ,dakika2= 0,0
for a, b in (bn):
    tplm_para += a * b
while tplm_para>0:
    if giris == True: #para yatıracak kişi koşulu
        py_üye_no = rnd.randrange(üye_no, üye_no+10, 1) #para yatıracak üye no
        giris = False
    if py_üye_no == üye_no:
        ytrlck_para = rnd.randrange(100, 1601, 100) #yatırılacak paranın belirlenmesi ve banknotlara bölünmesi
        if 100<=ytrlck_para<=500:
            bn[2][1] += (ytrlck_para//2) // 50
            y_e += (ytrlck_para//2) // 50
            bn[1][1] += (ytrlck_para//2)//20
            y_yi += (ytrlck_para//2)//20
            bn[0][1] += ((ytrlck_para//2)%20)//10
            y_o += ((ytrlck_para//2)%20)//10
        elif 600<= ytrlck_para<=1600:
            bn[4][1] += ytrlck_para // 200
            y_iy += ytrlck_para // 200
            bn[3][1] += (ytrlck_para %200)//100
            y_y += (ytrlck_para %200)//100
    while True and üye_no != py_üye_no: #çekilecek paranın belirlenmesi ve banknotlara belirlenmesi
        i = rnd.randint(0, 2) * 200
        if i // 200 <= bn[4][1] and i >= 200:
            bn[4][1] -= i // 200
            bs += i // 200
            c_iy += i//200
        elif i // 200 > bn[4][1] and i >= 200:
            i = bn[4][1] * 200
            bn[4][1] -= i // 200
            bs += i // 200
            c_iy += i//200
        else:
            i = 0
        cklck_para += i
        if cklck_para >= 1600 or bs >= 15: break #maksimum çekilecek miktarın ve banknot sayısının kontrolü
        y = rnd.randint(0, 2) * 100
        if y // 100 <= bn[3][1] and y >= 100:
            bn[3][1] -= y // 100
            bs += y // 100
            c_y += y//100
        elif y // 100 > bn[3][1] and y >= 100:
            y = bn[3][1] * 100
            bn[3][1] -= y // 100
            bs += y // 100
            c_y += y // 100
        else:
            y = 0
        cklck_para += y
        if cklck_para >= 1600 or bs >= 15: break
        e = rnd.randint(0, 4) * 50
        if e // 50 <= bn[2][1] and e >= 50:
            bn[2][1] -= e // 50
            bs += e // 50
            c_e += e // 50
        elif e // 50 > bn[2][1] and e >= 50:
            e = bn[2][1] * 50
            bn[2][1] -= e // 50
            bs += e // 50
            c_e += e // 50
        else:
            e = 0
        cklck_para += e
        if cklck_para >= 1600 or bs >= 15: break
        yi = rnd.randint(0, 5) * 20
        if yi // 20 <= bn[1][1] and yi >= 20:
            bn[1][1] -= yi // 20
            bs += yi // 20
            c_yi += yi // 20
        elif yi // 20 > bn[1][1] and yi >= 20:
            yi = bn[1][1] * 20
            bn[1][1] -= yi // 20
            bs += yi // 20
            c_yi += yi // 20
        else:
            yi = 0
        cklck_para += yi
        if cklck_para >= 1600 or bs >= 15: break
        o = rnd.randint(0, 9) * 10
        if o // 10 <= bn[0][1] and o >= 10:
            bn[0][1] -= o // 10
            bs += o // 10
            c_o += o// 10
        elif o // 10 > bn[0][1] and o >= 10:
            o = bn[0][1] * 10
            bn[0][1] -= o // 10
            bs += o // 10
            c_o += o // 10
        else:
            o = 0
            break
        cklck_para += o
        if cklck_para >= 1600 or bs >= 15: break
    tplm_para += ytrlck_para
    g = ytrlck_para
    cek = cklck_para
    bs=0 #çekilen banknot sayısını sıfırlıyorum ki her seferinde maks 15 banknot çekilebilsin
    k_para = (tplm_para - cklck_para) + ytrlck_para #kalan para
    üye_no +=1
    if üye_no %10 == 0 and üye_no //10 >=1: #her 10 kişide bir yeni para yatıracak kişinin belirlenme koşulu
        giris = True
    dakika2 +=rnd.randint(1,10) #kendimce yaptığım basit saat
    if dakika2 >=10:
        dakika1 +=1
        dakika2 -=10
    if dakika1>=6:
        saat2+=1
        dakika1 =0
    if saat2>=10:
        saat2=0
        saat1+=1
    print("Çekilen banknot adetleri:\t200TL-->{}\t100TL-->{}\t50TL-->{}\t20TL-->{}\t10TL-->{}".format(c_iy,c_y,c_e,c_yi,c_o),"\n",
          "Yatırılan banknot adetleri:\t200TL-->{}\t100TL-->{}\t50TL-->{}\t20TL-->{}\t10TL-->{}".format(y_iy,y_y,y_e,y_yi,y_o),"\n",
          "Kalan banknot adetleri:\t\t200TL-->{}\t100TL-->{}\t50TL-->{}\t20TL-->{}\t10TL-->{}".format(bn[4][1],bn[3][1],bn[2][1],bn[1][1],bn[0][1]),
          "\n","Toplam para={}\tÇekilen para={}\tYatırılan para={}\tKalan para={}\tİşlem numarası={}\t"
          .format(tplm_para,cklck_para,ytrlck_para,k_para,üye_no),"\n","\t\tSaat = {}{}:{}{}".format(saat1,saat2,dakika1,dakika2),"\n","\n",sep="")
    tplm_para -= cklck_para
    cklck_para = 0
    ytrlck_para = 0
    c_iy,c_y,c_e,c_o,c_yi,y_iy,y_y,y_e,y_yi,y_o = 0,0,0,0,0,0,0,0,0,0
print("İşlem başarıyla gerçekleştirildi :)")
input()