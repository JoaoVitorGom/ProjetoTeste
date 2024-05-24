# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#nome = input("Digite seu nome:")
#print("Você digitou %s" % nome)
#print("Olá, %s!" % nome)
#x=int(input("Digite um número"))
#y=int(input("Digite outro número"))
#print(x+y)
#x=float(input("Digite um valor em metros"))
#print("O valor em milímetros é: %.2f"%(x*1000))
#x=int(input("Digite a quantidade de dias"))
#y=int(input("Digite a quantidade de horas"))
#z=int(input("Digite a quantidade de minutos"))
#w=int(input("Digite a quantidade de segundos"))
#print("O total convertido para segundos é: %d"%(x*86400+y*3600+z*60+w))
#x=int(input("Digite o valor da mercadoria"))
#y = float(input("Digite o valor percentual do desconto"))
#print("O valor da mercadoria sem desconto era: %d"%x)
#print("O valor da mercadoria com desconto é: %.2f"%(x-(x*y)/100))
#x=int(input("Qual a distância a ser percorrida durante a viagem?"))
#y=int(input("Qual a velocidade média durante a viagem?"))
#print("O tempo de viagem será de: %.2f horas"%(x/y))
#x=float(input("Digite uma temperatura em celsius"))
#y=(9*x)/5+32
#print("A temperatura %.2f em celsius convertida para Fahrenheit é: %.2f"%(x,y))
#x=int(input("Quantos km o carro percorreu?"))
#y=int(input("Por quantos dias o carro foi alugado?"))
#z=x*0.15+y*60
#print("O valor do aluguel do carro é: %.2f"%z)
#x=int(input("Quantos cigarros você fuma por dia?"))
#y=int(input("Há quantos anos você fuma?"))
#z=(x*y*365*10)/1440
#print("Você perdeu %.2f dias de vida"%z)
#x=int(input("Digite um valor"))
#y=int(input("Digite outro valor"))
#if x>y:
#    print("O maior valor é: %d"%x)
#x=int(input("Qual a velocidade do carro?"))
#if x>80:
#    y=(x-80)*5
#    print("Você foi multado. O valor da multa é: R$%d"%y)
#sal=float(input("Digite o salário para cáculo de imposto:"))
#base=sal;
#imp=0;
#if base>3000:
#    imp=imp+((base-3000)*0.35)
#    base=3000
#if base>1000:
#    imp=imp+((base-1000)*0.20)
#print("Salário: R$%.2f imposto a pagar: R$%.2f"%(sal,imp))
'''x=int(input("Digite um número"))
y=int(input("Digite um número"))
z=int(input("Digite um número"))
maior =x
if y > x and y > z:
    maior=y
if z>x and z>=y:
    maior=z
menor=x
if y<z and y<x:
    menor=y
if z<x and z<=y:
    menor=z
print("O menor número é: %d"%menor)
print("O maior número é: %d"%maior)'''
'''sal=float(input("Digite o valor do salário"))
p_aumento=0.15
if sal>1250:
    p_aumento=0.10
aumento=sal*p_aumento
print(f"Seu aumento será de:{aumento:.2f}")'''
'''ida=int(input("Digite a idade do seu carro"))
if ida<=3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")'''
'''dist=int(input("Digite a distância que será percorrida na viagem"))
if dist<=200:
    pasa=0.5
else:
    pasa=0.45
pasat=pasa*dist
print("O valor da passagem é:%.2f"%pasat)'''
'''x=int(input("Digite um número"))
y=int(input("Digite um número"))
op=int(input("Digite qual operação você deseja realizar\n"
             "1-adição\n"
             "2-Subtração\n"
             "3-Multiplicação\n"
             "4-Divisão"))
if op ==1:
    oper=x+y
elif op==2:
    oper=x-y
elif op==3:
    oper=x*y
elif op==4:
    oper=x/y
print("O valor da operação é: %.2f"%oper)'''
'''valca=int(input("Qual o valor da casa a comprar"))
sal=int(input("Qual o salário"))
tem=int(input("Em quantos anos será paga"))
men=valca/(tem*12)
if men>sal*0.3:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")'''
'''quant=float(input("Qual a quantidade de kWh consumida"))
tip=int(input("Qual o tipo de instalação\n"
              "1-Residencial\n"
              "2-Comercial\n"
              "3-Industrial"))
if tip==1:
    if quant<=500:
        print("O valor a pagar é: %.2f"%(quant*0.4))
    else:
        print("O valor a pagar é: %.2f" %(quant * 0.65))
elif tip==2:
    if quant <= 1000:
        print("O valor a pagar é: %.2f" %(quant * 0.55))
    else:
        print("O valor a pagar é: %.2f" %(quant * 0.60))
else:
    if quant <= 5000:
        print("O valor a pagar é: %.2f" %(quant * 0.55))
    else:
        print("O valor a pagar é: %.2f" %(quant * 0.60))'''
'''x=10
while x>=0:
    print("%d,"%x)
    if x==0:
        print("Fogo!")
    x-=1'''
'''fim=int(input("Digite o último número a imprimir"))
x=0
while x<=fim:
    if x%3==0:
        print(x)
    x+=1'''
'''n = int(input("Tabuada de:"))
x = int(input("Ditie o início da tabuada:"))
y = int(input("Digite o fim da tabuada"))
while x <= y:
  print("%dx%d = %d"%(n,x,n*x))
  x+=1'''
'''x=int(input("Digite um número"))
y=int(input("Digite outro número"))
z=0
while y>0:
    z=z+x
    if y==1:
        print(z)
    y-=1'''
'''x=int(input("Digite um número"))
y=int(input("Digite outro número"))
z=x
t=0
while z>=y:
    z=z-y
    t+=1
print("%d/%d = %d e resto %d"%(x,y,t,z))'''
'''pontos = 0
questão = 1
while questão <= 3:
 resposta = input("Resposta da questão %d: " % questão)
 if questão == 1 and (resposta == "b" or resposta=="B"):
  pontos = pontos + 1
 if questão == 2 and (resposta == "a" or resposta=="A"):
  pontos = pontos + 1
 if questão == 3 and (resposta == "d" or resposta=="D"):
  pontos = pontos + 1
 questão += 1
print("O aluno fez %d ponto(s)" % pontos)'''
'''n = 1
soma = 0
while n <= 10:
 x = int(input("Digite o %d número:"%n))
 soma = soma + x
 n = n + 1 
print("Soma: %d"%soma)'''
'''x = 1
soma = 0
while x <= 5:
 n = int(input("%d Digite o número:" % x))
 soma = soma + n
 x = x + 1
print("Média: %5.2f" % (soma/5)) '''
'''dep=float(input("Digite o depósito inicial"))
tax=float(input("Digite a taxa de juros"))
z = float(input("Qual o valor mensal a ser depositado?"))
x=1
y=dep
while x<=24:
    y=y+dep*tax+z
    print("O valor da poupança no mês %3d é: %6.2f"%(x,y))
    x+=1
print("O total ganho com juros foi: %.2f"%(y-dep))'''
'''div=float(input("Qual o valor da dívida:"))
jur=float(input("Qual o valor da taxa de juros:"))
pag=float(input("Qual será o valor pago mensalmente:"))
x=1
if div*jur>pag:
    print("A sua dívida nunca será paga")
else:
    saldo=div
    tjur=0
    tpag=0
    while saldo>pag:
        juro=saldo*jur
        saldo=saldo+juro-pag
        tjur+=juro
        tpag+=pag
        x+=1
    print("Você vai levar %d meses para pagar: R$%.2f com um total de juros: R$%.2f e ainda restarão: R$%.2f a pagar"%((x-1),tpag,tjur,saldo))
'''
'''s=0
y=0
m=0
while True:
  x=int(input("Digite um número inteiro ou digite 0 para sair"))
  if x==0:
      break
  else:
      s+=x
      y+=1
      m=s/y
print("A soma de todos os números digitados é: %d\n"
      "Foram digitados %d números\n"
      "A média dos números é %.2f"%(s,y,m))'''
'''tot=0
while True:
    x=int(input("Digite o código do produto\n"
                "1\n"
                "2\n"
                "3\n"
                "5\n"
                "9"))
    y=int(input("Digite a quantidade comprada"))
    if x==1:
        tot=tot+0.5*y
    elif x==2:
        tot = tot + 1 * y
    elif x==3:
        tot = tot + 4 * y
    elif x==5:
        tot = tot + 7 * y
    elif x==9:
        tot = tot + 8 * y
    else:
        print("Código Inválido")
    w=int(input("Digite 1 para continuar ou 0 para receber o total das compras"))
    if w==0:
        break
print("O total de compras é: R$%.2f"%tot)'''
'''val=float(input("Digite o valor desejado a pagar"))
ced=0
atual=100
apagar=val
while True :
    if atual<=apagar:
        apagar-=atual
        ced+=1
    else:
        if atual>=1:
          print("%d cédula(s) de R$%d" % (ced, atual))
        else:
          print("%d moeda(s) de R$%.2f" %(ced,atual))
        if apagar <0.01:
            break
        elif atual==100:
            atual=50
        elif atual == 50:
                 atual = 20
        elif atual == 20:
                 atual = 10
        elif atual == 10:
                 atual = 5
        elif atual == 5:
                 atual = 1
        elif atual == 1:
            atual=0.50
        elif atual == 0.50:
            atual=0.10
        elif atual == 0.10:
            atual=0.05
        elif atual == 0.05:
            atual=0.02
        elif atual == 0.02:
            atual=0.01
        ced = 0'''
'''tab=1
while tab<=10:
    num=1
    while num<=10:
        print("%d x %d = %d"%(num,tab,num*tab))
        num+=1
    tab+=1'''
'''while True:
 val=float(input("Digite o valor a pagar"))
 if val==0:
    break
 ced=0
 atual=50
 while True:
     if atual<=val:
      val-=atual
      ced+=1
     else:
      print("%d cédula(s) de R$%d" % (ced, atual))
      if val==0:
          break
      if atual==50:
         atual=20
      elif atual==20:
         atual=10
      elif atual ==10:
         atual =5
      elif atual ==5:
         atual=1
      ced=0'''
'''tab =1
while True:
    x=int(input("Escolha a operação que se deseja realizar\n"
                "1-Adição\n"
                "2-Subtração\n"
                "3-Multiplicação\n"
                "4-Divisão\n"
                "5-Sair"))
    if x==5:
        break
    while tab<=10:
        num=1
        while num<=10:
            if x==1:
              print("%d + %d = %d"%(num,tab,num+tab))
            elif x==2:
              print("%d - %d = %d" % (num, tab, num - tab))
            elif x==3:
              print("%d x %d = %d" % (num, tab, num*tab))
            else:
              print("%d / %d = %.2f" % (num, tab, num/tab))
            num+=1
        tab+=1
        num=1
    tab=1'''
'''z=int(input("Digite um número"))
y=3
if z<0:
    print("Digite números positivos")
else:
    print("2 é primo")
    while y<=z:
      x=3
      while x<y:
          if y%x==0:
              break
          x+=2
      if x==y:
          print(f"{y} é primo")

      y+=1'''
'''n=int(input("Digite um número para encontrar sua raiz quadrada"))
b=2
while abs(n-(b*b))>0.0001:
    p=(b+(n/b))/2
    b=p
print(f"A raiz quadrada de {n} é {b:3.2f}")'''
'''x=int(input("Digite um número"))
y=int(input("Digite um número"))
if x<y:
    print(f"O resto da divisão é {x}")
else:
    z=0
    while x>=y:
        x-=y
    z=y-x
    print(f"O resto da divisão é {z}")'''
'''x=input("Digite um número")
i=0
f=len(x)-1
while f>i and x[i]==x[f]:
    f-=1
    i+=1
if x[i]==x[f]:
    print(f"{x} é palíndromo")
else:
    print(f"{x} não é palíndromo")'''
'''n=[6,7,5,8,9]
sum=0
x=0
while x<=4:
    sum+=n[x]
    x+=1
print(f"A média das notas é: {sum/x}")'''
'''n=[0,0,0,0,0,0,0]
sum=0
x=0
while x<7:
    n[x]=float(input(f"Nota {x}"))
    sum+=n[x]
    x+=1
x=0
while x<7:
    print(f"Nota {x} = {n[x]}")
    x+=1
print(f"A média das notas é: {sum/x}")'''
'''n=[0,0,0,0,0]
x=0
while x<5:
    n[x]=float(input(f"Digite o {x+1} número"))
    x+=1
while True:
  x=int(input("Digite qual número vc quer que seja printado. Digite 0 para sair"))
  if x==0:
      break
  print(f"O número {x+1} é {n[x-1]}")'''
'''l=[]
while True:
    x=int(input("Digite um valor, 0 se quiser sair"))
    if x==0:
        break
    l.append(x)
x=0
while x < len(l):
    print(l[x])
    x+=1'''
'''pl=[]
sl=[]
while True:
    x=int(input("Digite os valores da primeira lista. Digite 0 se deseja ir para a segunda"))
    if x==0:
        break
    pl.append(x)
while True:
    x = int(input("Digite os valores da primeira lista. Digite 0 se deseja sair"))
    if x==0:
        break
    sl.append(x)
tl=pl[:]
tl.extend(sl)
print(tl)'''
'''pl=[1,2,3,4,5]
sl=[2,5,1,7,10,9]
pl.extend(sl)
tl=[]
x=0
while x<len(pl) :
    y = 0
    while y<len(tl) :
        if pl[x] == tl[y]:
            break
        y+=1
    if y == len(tl):
        tl.append(pl[x])
    x+=1
print(tl)'''
'''último = 10
fila = list(range(1,último+1))
fila2= list(range(1,último+2))
x = 0
while True:
    op=input(f"Existem {len(fila)} clientes na fila.\n"
                 f"Fila atual 1: {fila}\n"
                 f"Fila atual 2: {fila2}\n"
                 "1-Para adicionar um cliente na fila 1\n"
                 "2-Para realizar o atendimento fila 1\n"
                 "4-Para adicionar um cliente na fila 2\n"
                 "5-Para realizar o atendimento fila 2\n"
                 "3-Para sair")
    up=op[:]
    while  x<len(up):
     if up[x] == '2':
        if (len(fila)>0):
            att=fila.pop(0)
        else:
            print("Fila vazia! Ninguém para atender.")
     elif up[x] =='1':
        último+=1
        fila.append(último)
     elif up[x] == '5':
        if (len(fila2)>0):
            att=fila2.pop(0)
        else:
            print("Fila vazia! Ninguém para atender.")
     elif up[x] =='4':
        último+=1
        fila2.append(último)
     elif up[x] =='3':
        break
     else:
        print("Opção inválida, digite uma opção válida")
     x+=1
    break
print(fila)
print(fila2)'''
'''p=[]
x=0
z=input("Digite uma seqência de abre e fecha parênteses")
y=z[:]
while x<len(y):
    if y[x]=='(':
        p.append(1)
    elif y[x]==')':
        p.pop(-1)
    x+=1
if p==[]:
 print("Os parênteses foram abertos e fechados corretamente")
else:
 print("Os parênteses não foram abertos ou fechados corretamente")'''
'''ult=10
p=list(range(1,ult+1))
while True:
    z=input(f"A pilha atual tem {len(p)} pratos\n"
            f"A pilha atual é: {p}\n"
            f"1-Para adicionar um prato a pilha\n"
            f"2-Para remover um prato da pilha\n"
            f"3-Para sair")
    if z=='1':
        ult+=1
        p.append(ult)
    elif z=='2':
        if len(p)>0:
            p.pop(-1)
        else:
            print("Pilha vazia. Sem pratos para remover")
    elif z=='3':
        break
    else:
        print("Opção inválida. Digite 1,2 ou 3")
print(p)'''
'''l=[2,3,4,5]
p=int(input("Digite um valor para ser comparado aos valores da lista"))
x=0
while x<len(l):
     if l[x]==p:
      break
     x += 1
if x<len(l):
 print(f"O valor {p} foi encontrado")
else:
 print(f"O valor {p} não foi encontrado")'''
'''l=[5,3,4,2]
p=int(input("Digite um valor para ser comparado aos valores da lista"))
v=int(input("Digite outro valor para ser comparado aos valores da lista"))
x=0
achoup=False
achouv=True
y=0
while x<len(l):
     if l[x]==p:
         achoup=True
         y=1
     elif l[x]==v:
         achouv=True
         y=2
     x += 1
if achoup:
 print(f"O valor {p} foi encontrado")
else:
 print(f"O valor {p} não foi encontrado")
if achouv:
 print(f"O valor {v} foi encontrado")
else:
 print(f"O valor {v} não foi encontrado")
if y==2:
    print(f"O valor {p} foi encontrado primeiro")
elif y==1:
    print(f"O valor {v} foi encontrado primeiro")'''
'''l=[5,3,4,2]
p=int(input("Digite um valor para ser comparado aos valores da lista"))
v=int(input("Digite outro valor para ser comparado aos valores da lista"))
x=0
achoup=False
achouv=True
y=0
z=0
while x<len(l):
     if l[x]==p:
         achoup=True
         y=x
     elif l[x]==v:
         achouv=True
         z=x
     x += 1
if achoup:
 print(f"O valor {p} foi encontrado na posição {y}")
else:
 print(f"O valor {p} não foi encontrado")
if achouv:
 print(f"O valor {v} foi encontrado na posição {z}")
else:
 print(f"O valor {v} não foi encontrado")
if y<z:
    print(f"O valor {p} foi encontrado primeiro")
elif y>z:
    print(f"O valor {v} foi encontrado primeiro")'''
'''l=[1,2,3,4,5]
p=int(input("Diigite um valor para verificar se ele pertence a lista"))
for e in l:
    if e==p:
        print(f"O elemento {p} pertence a lista")
        break
else:
    print(f"O elemento {p} não pertence a lista")'''
'''L=[]
while True:
 n=int(input("Digite um número (0 sai):"))
 if n == 0:
  break
 L.append(n)
for e in L:
 print(e)'''
'''for t in range(3,33,3):
    print(t,end=" ")
print()'''
'''l=list(range(100,1100,50))
print(l)'''
'''L=[5,9,13]
for x, e in enumerate(L):
 print("[%d] %d" % (x,e))'''
'''l=[3,6,8,0,1]
max=l[0]
for e in l:
    if e> max:
        max=e
print(f"O maior valor é: {max}")'''
'''l=[3,6,8,0,1]
min=l[0]
for e in l:
    if e< min:
        min=e
print(f"O menor valor é: {min}")'''
'''T=[-10,-8,0,1,2,5,-2,-4]
max=T[0]
min=T[0]
med=0
for e in T:
    if e> max:
        max=e
    elif e<min:
        min=e
    med+=e
print(f"O menor valor é {min}, o maior valor é {max},a média de temperatura é {med/len(T)}")'''
'''V=[1,2,3,4,5,6,7,8,9,10]
P=[]
I=[]
for e in V:
    if e%2==0:
        P.append(e)
    else:
        I.append(e)
print(f"Os números pares {P}")
print(f"Os números ímpares {I}")'''
'''lugares_vagos=[10,2,1,3,0]
while True:
 sala=int(input("Sala (0 sai): "))
 if sala == 0:
  print("Fim")
  break
 if sala>len(lugares_vagos) or sala<1:
     print("Sala inválida")
 elif lugares_vagos[sala-1]==0:
  print("Desculpe, sala lotada!")
 else:
  lugares =int(input("Quantos lugares você deseja (%d vagos):"
   % lugares_vagos[sala-1]))
 if lugares > lugares_vagos[sala-1]:
  print("Esse número de lugares não está disponível.")
 elif lugares < 0:
  print("Número inválido")
 else:
  lugares_vagos[sala-1]-=lugares
  print("%d lugares vendidos" % lugares)
print("Utilização das salas")
for x,l in enumerate(lugares_vagos):
 print("Sala %d - %d lugar(es) vazio(s)" % (x+1, l))'''
'''L=[]
while True:
    c=input("Digite o próximo produto da lista. Digite fim para sair")
    if c=="fim":
        break
    L.append(c)
for x,e in enumerate(L):
    print(f"{x+1}-{e}")'''
'''L=["maçã","pera","uva"]
for p in L:
    for l in p:
        print(l)'''
'''p1=["Arroz",2,5.40]
p2=["Feijão",4,7.80]
p3=["Batata",10,1.50]
compras=[p1,p2,p3]
for e in compras:
      print(f"Produto: {e[0]}")
      print(f"Quantidade: {e[1]}")
      print(f"Preço: {e[2]}")'''
'''com=[]
while True:
    p=input("Digite qual o produto. Digite 0 para sair")
    if p=="0":
        break
    q=int(input("Digite a quantidade do produto"))
    pre=float(input("Digite o preço do produto"))
    com.append([p,q,pre])
soma=0
for e in com:
    print(f"Produto: {e[0]}")
    print(f"Quantidade: {e[1]}")
    print(f"Preço: {e[2]}")
    soma += e[1]*e[2]
print(f"O total das compras é R${soma}")'''
'''L=[7,4,3,12,8]
fim=5
while fim > 1:
 trocou=False
 x=0
 while x<(fim-1):
   if L[x] > L[x+1]:
    trocou=True
    temp=L[x]
    L[x]=L[x+1]
    L[x+1]=temp
   x+=1
 if not trocou:
  break
 fim-=1
for e in L:
  print(e)'''
'''L=[7,4,3,12,8]
fim=5
while fim > 1:
 trocou=False
 x=0
 while x<(fim-1):
   if L[x] < L[x+1]:
    trocou=True
    temp=L[x]
    L[x]=L[x+1]
    L[x+1]=temp
   x+=1
 if not trocou:
  break
 fim-=1
for e in L:
  print(e)'''
'''tabela = { "Alface": 0.45,
           "Batata": 1.20,
           "Tomate": 2.30,
           "Feijão": 1.50 }
print(tabela["Alface"])
print(tabela)
tabela["Tomate"]=2.00
print(tabela["Tomate"])
print("Manga"in tabela)
print("Alface" in tabela)'''
'''tabela = { "Alface": 0.45,
           "Batata": 1.20,
           "Tomate": 2.30,
           "Feijão": 1.50 }
print(tabela.keys())
print(tabela.values())'''
'''tabela = { "Alface": 0.45,
           "Batata": 1.20,
           "Tomate": 2.30,
           "Feijão": 1.50 }
while True:
    p=input("Digite o nome do produto. Digite 0 para sair")
    if p=="0":
        break
    if p in tabela:
        print(f"{p}:R${tabela[p]}")
    else:
        print("Esse produto não encontrado")'''
'''estoque={ "tomate": [ 1000, 2.30],
          "alface": [ 500, 0.45],
          "batata": [ 2001, 1.20],
          "feijão": [ 100, 1.50] }
venda = [ ["tomate", 5], ["batata", 10], ["alface",5] ]
total = 0
print("Vendas:\n")
for operação in venda:
 produto, quantidade = operação 
 preço = estoque[produto][1]
 custo = preço * quantidade
 print("%12s: %3d x %6.2f = %6.2f" %
 (produto, quantidade,preço,custo))
 estoque[produto][0] -= quantidade
 total+=custo
 print(" Custo total: %21.2f\n" % total)
 print("Estoque:\n")
for chave, dados in estoque.items():
 print("Descrição: ", chave)
 print("Quantidade: ", dados[0])
 print("Preço: %6.2f\n" % dados[1])'''
'''estoque={ "tomate": [ 1000, 2.30],
 "alface": [ 500, 0.45],
 "batata": [ 2001, 1.20],
 "feijão": [ 100, 1.50] }
total = 0
cust=0
while True:
    p=input("Digite o produto vendido.Digite 0 para sair")
    if p=="0":
        break
    else:
     if p in estoque:
         q=int(input("Digite a quantidade vendida do produto"))
         prec=estoque[p][1]
         if q>estoque[p][0]:
            print(f"A quantidade disponível é:{estoque[p][0]}")
         else:
            cust=prec*q
            estoque[p][0]-=q
            total+=cust
     else:
        print("Produto não encontrado")
    print(f"O {p} teve {q} unidades vendidas à um preço de R${prec} totalizando R${cust}")
print("Estoque\n")
for c,d in estoque.items():
    print(f"O produto {c}")
    print(f"Tem {d[0]} unidades")
    print(f"Custando R${d[1]}")'''
'''dic={}
f=input("Digite uma frase")
for e in f:
    if e in dic:
        dic[e]+=1
    else:
        dic[e]=1
print(dic)'''
'''frase = input("Digite uma frase para contar as letras:")
d = {}
for letra in frase:
    # Se letra não existir no dicionário, retorna 0
    # se existir, retorna o valor anterior
    d[letra] = d.get(letra, 0) + 1
print(d)
tupla=("a","b","c")'''
'''l=list("Alô Mundo")
print(l)
s="".join(l)
print(s)
print(s.startswith("Alô"))
print(s.startswith("alo"))
print(s.lower())
print(s.upper())
print("Alô" in s)
print("alô" in s)
print("Alô" not in s)'''
'''s="Primeira casa, segunda casa, terceira casa"
print(s.count("casa"))
print(s.count("segunda"))
print(s.count("a"))
print(s.find("casa"))
print(s.find("s"))
print(s.find("z"))
print(s.rfind("casa"))
print(s.rfind("a"))
print(s.find("a",10)) #começa a pesquisa a partir da posição 10
print(s.find("casa",0,30)) #começa a pesquisa em 0 e vai até 30
print(s.find("a",20,35)) #pesquisa de 20 até 35'''
'''s="Primeira casa, segunda casa, terceira casa"
p=0
while(p>-1):
    p=s.find("casa",p)
    if p>=0:
        print(f"Posição: {p}")
        p+=1'''
'''s=input("Digite uma string")
j=input("Digite outra string")
if j in s:
   p= s.find(j)
   print(f"{j} encontrado na posição {p} de {s.upper()}")
else:
    print(f"{j} não encontrado em {s.upper()}")'''
'''s=input("Digite uma string")
j=input("Digite outra string")
l=list(j)
ol=[]
x=0
while x< len(l):
    if l[x] in j:
        ol.append(l[x])
    x+=1
z="".join(ol)
print(z)'''
'''s=input("Digite uma string")
j=input("Digite outra string")
l=list(j)
m=list(s)
ol=[]
x=0
y=0
while x< len(l):
    if l[x] not in s:
        ol.append(l[x])
    x+=1
while y< len(m):
    if m[y] not in j:
        ol.append(m[y])
    y+=1
z="".join(ol)
print(z)'''
'''s=input("Digite uma string")
j=input("Digite outra string")
t=""
for l in s:
    if l not in j and l not in t:
        t+=l
for l in j:
    if l not in s and l not in t:
        t+=l
if t=="":
    print("Caracteres incomuns não encontrados")
else:
    print(f"Caracteres incomuns {t}")'''
'''s=input("Digite uma string")
t=""
for l in s:
    if l not in t:
     print(f"{l}:{s.count(l)}x")
    t += l'''
'''s=input("Digite uma string")
j=input("Digite outra string")
t=""
for l in s:
    if l not in j:
        t+=l
if t=="":
 print("Não há caracteres")
else:
    print(f"{t}")'''
'''s=input("Digite uma string")
j=input("Digite outra string")
m=input("Digite outra string")
if len(j)==len(m):
 t = ""
 for l in s:
    pos = j.find(l)
    if l not in j:
        t+=l
    else:
        t+=m[pos]
 if t=="":
  print("Não há caracteres")
 else:
    print(f"{t}")
else:
    print("A 2ª e a 3ª string devem ter o mesmo tamanho")'''
'''s="tigre"
print("X"+s.center(15)+"X")
print("X"+s.center(15,".")+"X")
print(s.ljust(20,"."))
print(s.rjust(20,"-"))'''
'''s="Uma casa, duas casas, três casas"
print(s.split(","))
print(s.split(" "))
print(s.split())
m="Uma linha\noutra linha\ne mais uma\n"
print(m.splitlines())'''
'''s="Um tigre, dois tigres, três tigres"
print(s.replace("tigre","gato"))
print(s.replace("","-"))
print(s.replace("tigre","gato",2))'''
'''t=' Olá   '
print(t.strip())
print(t.lstrip())
print(t.rstrip())'''
'''t="/././. Olá /././."
print(t.strip("/."))
print(t.lstrip("/."))
print(t.rstrip("/."))'''
'''s="125"
p=" Olá"
print(s.isalnum())
print(p.isalnum())
print(s.isalpha())
print(p.isalpha())
print(s.isdigit())
print(p.isdigit())
print("171".isdigit())
print("-5".isdigit())
print("2+3".isdigit())'''
'''s="ABC"
t="AbC"
u="abc"
print(s.isupper())
print(s.islower())
print(t.isupper())
print(u.islower())
print(u.isupper())'''
'''print("\n\t".isprintable())
print("\nAlô".isprintable())
print("Alô mundo".isprintable())'''
'''print("{0} {1}".format("Alô","Mundo"))
print("{0} x {1} R${2}".format(5,"maçã", "1.20"))
print("{0} {1} {0}".format("-","x"))
print("{1} {0}".format("primeiro", "segundo"))
print("{0:10} {1}".format("123", "456"))
print("X{0:10}X".format("123456789012345"))
print("X{0:<10}X".format("123"))
print("X{0:>10}X".format("123"))
print("X{0:^10}X".format("123"))
print("X{0:.<10}X".format("123"))
print("X{0:!>10}X".format("123"))
print("X{0:*^10}X".format("123"))
print("{0[0]} {0[1]}".format(["123", "456"]))
print("{0[nome]} {0[telefone]}".format({ "telefone": 572, "nome":"Maria"}))
print("{0:05}".format(5))
print("{0:*=7}".format(32))
print("{0:*^10}".format(123))
print("{0:*<10}".format(123))
print("{0:*>10}".format(123))
print("{0:10,}".format(7532))
print("{0:10.5f}".format(1500.31))
print("{0:10,.5f}".format(1500.31))
print("{0:+10} {1:10}".format(5,-6))
print("{:b}".format(5678))
print("{:c}".format(65))
print("{:o}".format(5678))
print("{:x}".format(5678))
print("{:X}".format(5678))'''
'''import locale
locale.setlocale(locale.LC_ALL,"pt_BR.utf-8")
'pt_BR.utf-8'
print("{:n}".format(5678))
print("{:8e}".format(3.141592653589793))
print("{:8E}".format(3.141592653589793))
print("{:8g}".format(3.141592653589793))
print("{:8G}".format(3.141592653589793))
print("{:.2%}".format(0.05))'''
'''palavra = input("Digite a palavra secreta:").lower().strip()
for x in range(100):
 print()
digitadas = []
acertos = []
erros = 0
while True:
 senha=""
 for letra in palavra:
  senha +=letra if letra in acertos else "."
 print(senha)
 if senha == palavra:
  print("Você acertou!")
  break
 tentativa = input("\nDigite uma letra:").lower().strip()
 if tentativa in digitadas:
  print("Você já tentou esta letra!")
  continue
 else:
  digitadas += tentativa
  if tentativa in palavra:
   acertos += tentativa
  else:
   erros += 1
   print("Você errou!")
   print("X==:==\nX : ")
   print("X O " if erros >= 1 else "X")
 linha2=""
 if erros == 2:
  linha2 = " | "
 elif erros == 3:
  linha2 = " \| "
 elif erros >= 4:
  linha2 = " \|/ "
 print("X%s" % linha2)
 linha3=""
 if erros == 5:
  linha3+=" / "
 elif erros>=6:
  linha3+=" / \ "
 print("X%s" % linha3)
 print("X\n===========")
 if erros == 6:
   print("Enforcado!")
   print(f"A palavra secreta era: {palavra}")
   break'''
'''palavras=["casa",
          "carro",
          "moto",
          "rua",
          "lago",
          "rio"]
num=int(input("Digite um índice"))
palavra = palavras[(num * 776) % len(palavras)]
digitadas = []
acertos = []
erros = 0
l=["X==:==\nX : ","X O "," | "," \| "," \|/ "," / "," / \ ","X\n==========="]
while True:
 senha=""
 for letra in palavra:
  senha +=letra if letra in acertos else "."
 print(senha)
 if senha == palavra:
  print("Você acertou!")
  break
 tentativa = input("\nDigite uma letra:").lower().strip()
 if tentativa in digitadas:
  print("Você já tentou esta letra!")
  continue
 else:
  digitadas += tentativa
  if tentativa in palavra:
   acertos += tentativa
  else:
   erros += 1
   print("Você errou!")
   print(l[0])
   print(l[1] if erros >= 1 else "X")
 linha2=""
 if erros == 2:
  linha2 = l[2]
 elif erros == 3:
  linha2 = l[3]
 elif erros >= 4:
  linha2 = l[4]
 print("X%s" % linha2)
 linha3=""
 if erros == 5:
  linha3+=l[5]
 elif erros>=6:
  linha3+=l[6]
 print("X%s" % linha3)
 print("X\n",l[7])
 if erros == 6:
   print("Enforcado!")
   print(f"A palavra secreta era: {palavra}")
   break'''
'''j1=[]
j2=[]
esc=[]
x=1
g=[["1","2","3"],
   ["4","5","6"],
   ["7","8","9"],
   ["1","4","7"],
   ["2","5","8"],
   ["3","6","9"],
   ["1","5","9"],
   ["3","7","5"]]
while True:
   print(f"Posições já escolhidas: {esc}")
   y=input(f"Jogador um faça sua {x}ª escolha")
   if y not in esc:
    esc+=y
    j1+=y
    if j1 in g:
        print("O jogador 1 ganhou!")
        break
   else:
       print("posição já escolhida. Você perdeu a vez")
   if len(esc)>=8:
       print("o jogo terminou empatado")
       break
   print(f"Posições já escolhidas: {esc}")
   z=input(f"Jogador dois faça sua {x}ª escolha")
   if z not in esc:
    esc.append(z)
    j2.append(z)
    if j2 in g:
        print("O jogador 2 ganhou!")
        break
   else:
       print("posição já escolhida. Você perdeu a vez")
   x+=1'''
'''def soma(a,b):
    print(a+b)
soma(2,9)
soma(10,3)'''
'''def soma(a,b):
    return(a+b)
print(soma(2,9))
print(soma(10,3))'''
'''def epar(x):
    return x%2==0
print(epar(2))
print(epar(3))'''
'''def epar(x):
    return x%2==0
def impar_par(x):
    if(epar(x)):
        return "par"
    else:
        return "ímpar"
print((impar_par(4)))
print((impar_par(5)))'''
'''def maior_num(a,b):
    if a>b:
        return a
    else:
        return b
print(maior_num(2,3))
print(maior_num(4,2))'''
'''def mult(a,b):
    return a%b==0
print(mult(4,5))
print(mult(8,4))'''
'''def A_quad(x):
    return x*x
print(A_quad(2))
print(A_quad(4))'''
'''def A_trian(a,b):
    return (a*b)/2
print(A_trian(4,5))
print(A_trian(9,5))'''
'''def pesquise(lista,valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return None
L=[10,20,25,30]
print(pesquise(L,25))
print(pesquise(L,27))'''
'''def med(lista):
    y=0
    for e in (lista):
        y+=e
    return y/len(L)
L=[10,20,25,30]
print(med(L))'''
'''def soma(L):
    tot=0
    for e in L:
        tot+=e
    return tot
def med(L):
    return soma(L)/len(L)
L=[10,20,25,30]
print(med(L))'''
'''def fatorial(n):
    fat=1
    while n>=1:
        fat*=n
        n-=1
    return fat
print(fatorial(5))'''
'''def pesq(valor,lista):
    if valor in lista:
        return lista.index(valor)
    return None
L=[1,23,4,5,6]
print(pesq(3,L))
print(pesq(1,L))'''
'''def soma(L):
 total=0
 for e in L:
  total+=e
 return total
L=[1,7,2,9,15]
print(soma(L))'''
'''EMPRESA="Unidos Venceremos Ltda"
def imprime_cabeçalho():
 print(EMPRESA)
 print("-" * len(EMPRESA))
print(imprime_cabeçalho())'''
'''a=5
def muda_e_imprime():
 a=7
 print("A dentro da função: %d" % a)
print("A antes de mudar: %d" % a)
muda_e_imprime()
print("A depois de mudar: %d" % a)'''
'''a=5
def muda_e_imprime():
 global a
 a=7
 print("A dentro da função: %d" % a)
print("a antes de mudar: %d" % a)
muda_e_imprime()
print("a depois de mudar: %d" % a)'''
'''def fatorial(n):
 if n==0 or n==1:
  return 1
 else:
  return n*fatorial(n-1)'''
'''def fatorial(n):
 print(f"Calculando o fatorial de {n}")
 if n==0 or n==1:
  print(f"Fatorial de {n} = 1")
  return 1
 else:
  fat=n*fatorial(n-1)
  print(f"Fatorial de {n} = {fat}")
 return fat
fatorial(4)'''
'''def fibonacci(n):
 if n<=1:
  return n
 else:
  return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))'''
'''def mdc(a,b):
 if b==0:
  return a
 if a>b:
  return mdc(b,a%b)
 else:
  print("O programa só funciona para a>b")
def mmc(a,b):
 return (abs(a*b)/mdc(a,b))
print(mmc(6,5))'''
'''def fibonacci(n):
 L = [0,1]
 x = 2
 if n<=1:
  return n
 else:
  while len(L)<=n:
   y=L[x-1]+L[x-2]
   L.append(y)
   x+=1
 return L[n]
print(fibonacci(7))'''
'''def faixa_int(pergunta, max,min):
 while True:
  v=int(input(pergunta))
  if v>max or v<min:
   print(f"Valor inválido. Digite um valor entre {min}-{max}")
  else:
   return v
print(faixa_int("Entre com um número",12,1))'''
'''def tam_string(string,max,min):
 string.strip()
 while True:
  if len(string) >max or len(string)<min:
   print(f"String Inválida. Digite uma String com comprimento entre {min}-{max}")
   break
  else:
   return string
print(tam_string("Uma noite estrelada",20,4))'''
'''def str_list(string,lista):
 if string in lista:
  return True
 else:
  return False
print(str_list("Uma",["Uma","Duas","Três"]))'''
'''def barra():
 ("*"*40)'''
'''def barra(n=40,caractere="*"):
 print(caractere*n)
barra(10,"@")
barra(12,"&")
barra()'''
'''def soma(a,b,imprime=False):
 s=a+b
 if imprime:
  print(s)
 return s
print(soma(2,3))
soma(2,3,True)'''
'''def retangulo(altura,largura,caractere="*"):
 linha=caractere*largura
 for i in range(altura):
  print(linha)
retangulo(2,3)
retangulo(largura=2,altura=3)'''
'''def soma(a, b):
 return a + b
def subtração(a, b):
 return a - b
def imprime(a, b, foper):
 print(foper(a, b))
imprime(5, 4, soma)
imprime(10, 1, subtração)'''
'''def impri_lista(L,impri,cond):
 for e in L:
  if cond(e):
   impri(e)
def impri_ele(e):
 print(f"Valor: {e}")
def épar(x):
 return x%2==0
def éimpar(x):
 return not épar(x)
L=[2,3,4,5,8,6,7]
impri_lista(L,impri_ele,épar)
impri_lista(L,impri_ele,éimpar)'''
'''def soma(a,b):
 print(a+b)
L=[1,2]
soma(*L)'''
'''def barra(n=10,c="*"):
 print(c*n)
L=[[5,"@"],[7,"&"],[4,"$"],[3,"#"],[8]]
for e in L:
 barra(*e)'''
'''def soma(*args):
 s=0
 for x in args:
  s+=x
 return print(s)
soma(1,2)
soma(2)
soma(1,4,5,3,3,6)'''
'''def imprime_maior(mensagem, *numeros):
 maior = None
 for e in numeros:
  if maior == None or maior < e:
   maior = e
 print(mensagem, maior)
imprime_maior("Maior:",5,4,3,1)
imprime_maior("Max:", *[1,7,9])'''
'''a=lambda x: x*2
print(a(3))'''
'''aumento=lambda a,b: (a*b/100)
print(aumento(100,5))'''
'''import entrada
L=[]
for x in range(10):
 L.append(entrada.val_int("Digite um número:", 20, 0))
print("Soma: %d" % (sum(L)))'''
'''import random
for x in range(10):
 print(random.randint(1,100))'''
'''import random
n=random.randint(1,10)
x=int(input("Digite um número de 1 a 10"))
if x==n:
 print("Você adivinhou o número")
else:
 print(f"Você errou, o número era {n}")'''
'''import random
n=random.randint(1,10)
tent=0
while tent<3:
 y=int(input("Digite um número de 1 a 10"))
 if y==n:
  print("Você adivinhou o número")
  break
 tent += 1
else:
  print("Você errou. Suas tentativas acabaram")'''
'''import random
for x in range(10):
 print(random.random())'''
'''import random
for x in range(10):
  print(random.uniform(15,25))'''
'''import random
print(random.sample(range(1,101), 6))'''
'''import random
a=list(range(1,11))
random.shuffle(a)
print(a)'''
'''import random
L=["uma","casa","carro","moto","livro"]
palavra =L[random.randint(0,len(L)-1)]
for x in range(100):
 print()
digitadas = []
acertos = []
erros = 0
while True:
 senha=""
 for letra in palavra:
  senha +=letra if letra in acertos else "."
 print(senha)
 if senha == palavra:
  print("Você acertou!")
  break
 tentativa = input("\nDigite uma letra:").lower().strip()
 if tentativa in digitadas:
  print("Você já tentou esta letra!")
  continue
 else:
  digitadas += tentativa
  if tentativa in palavra:
   acertos += tentativa
  else:
   erros += 1
   print("Você errou!")
 print("X==:==\nX : ")
 print("X O " if erros >= 1 else "X")
 linha2=""
 if erros == 2:
  linha2 = " | "
 elif erros == 3:
  linha2 = " \| "
 elif erros >= 4:
  linha2 = " \|/ "
 print("X%s" % linha2)
 linha3=""
 if erros == 5:
  linha3+=" / "
 elif erros>=6:
  linha3+=" / \ "
 print("X%s" % linha3)
 print("X\n===========")
 if erros == 6:
  print("Enforcado!")
  break'''
'''a=5
print(type(a))
b="Olá"
print(type(b))
c=print
print(type(c))'''
'''import types
def diz_o_tipo(a):
 tipo = type(a)
 if tipo == str:
  return("String")
 elif tipo == list:
  return("Lista")
 elif tipo == dict:
  return("Dicionário")
 elif tipo == int:
  return("Número inteiro")
 elif tipo == float:
  return("Número decimal")
 elif tipo == types.FunctionType:
  return("Função")
 elif tipo == types.BuiltinFunctionType:
  return("Função interna")
 else:
  return(str(tipo))
print(diz_o_tipo(10))
print(diz_o_tipo(10.5))
print(diz_o_tipo("Alô"))
print(diz_o_tipo([1,2,3]))
print(diz_o_tipo({"a":1, "b":50}))
print(diz_o_tipo(print))
print(diz_o_tipo(None))'''
'''L=[2,"Alô",["!"],{"a":1,"b":2}]
for e in L:
 print(type(e))'''
'''L=["a",["b","c","d","e"],"f"]
for e in L:
 if type(e)==str:
  print(e)
 else:
  for z in e:
   print(z)'''
'''ESPAÇOS_POR_NÍVEL = 4
def imprime_elementos(l, nivel=0):
    espacos = ' ' * ESPAÇOS_POR_NÍVEL * nivel
    if type(l) == list:
        print(espacos, "[")
        for e in l:
            imprime_elementos(e, nivel + 1)
        print(espacos, "]")
    else:
        print(espacos, l)
L = [1, [2, 3, 4, [5, 6, 7]]]

imprime_elementos(L)'''
'''def prime_num(n):
 y=1
 yield 2
 x=3
 z=3
 while y<n:
  if z%x==0:
   if x==z:
    yield z
    y += 1
   z+=2
   x=3
  elif x<z:
   x+=2
  else:
   z+=2
for primo in prime_num(10):
 print(primo)'''
'''def fibo_seq(n):
 y=2
 yield 0
 yield 1
 x=0
 z=1
 while y<n:
  w=x+z
  yield w
  x=z
  z=w
  y+=1
for fibo in fibo_seq(100):
 print(fibo)'''


'''def fibonacci(n):
 p = 0
 s = 1
 while n > 0:
  yield p
  p, s = s, s + p
  n -= 1
for f in fibonacci(10):
 print(f)'''
'''arquivo=open("números.txt","w")
for linha in range(1,101):
 arquivo.write("%d\n" % linha)
arquivo.close()'''
'''arquivo=open("números.txt","r")
for linha in arquivo.readlines(): 
 print(linha)
arquivo.close()'''
'''import sys
print("Número de parâmetros: %d" % len(sys.argv))
for primeiro,p in enumerate(sys.argv):
 print("Parâmetro %d = %s" % (primeiro,p))'''
'''import sys
# Verifica se o parâmetro foi passado
if len(sys.argv) !=2:  # Lembre-se que o nome do programa é o primeiro da lista
    arquivo=open("números.txt","r")
    for linha in arquivo.readlines():
        # Como a linha termina com ENTER,
        # retiramos o último caractere antes de imprimir
        print(linha[:-1])
else:
    nome = sys.argv[1]
    arquivo = open(nome, "r")
    for linha in arquivo.readlines():
        # Como a linha termina com ENTER,
        # retiramos o último caractere antes de imprimir
        print(linha[:-1])'''
'''ímpares=open("ímpares.txt","w")
pares=open("pares.txt","w")
for n in range(0,1000):
 if n % 2 == 0:
  pares.write("%d\n" % n)
 else:
  ímpares.write("%d\n" % n)
ímpares.close()
pares.close()'''
'''multiplos4=open("multiplos_4.txt","w")
pares=open("pares.txt")
for i in pares.readlines():
 if int(i)%4==0:
  multiplos4.write(i)
pares.close()
multiplos4.close()'''
'''def lê_número(arquivo):
    while True:
        número = arquivo.readline()
        # Verifica se conseguiu ler algo
        if número == "":
            return None
        # Ignora linhas em branco
        if número.strip() != "":
            return int(número)


def escreve_número(arquivo, n):
    arquivo.write(f"{n}\n")


pares = open("pares.txt", "r")
ímpares = open("ímpares.txt", "r")
pares_ímpares = open("pareseimpares.txt", "w")
npar = lê_número(pares)
nímpar = lê_número(ímpares)
while True:
    if npar is None and nímpar is None:  # Termina se ambos forem None
        break
    if npar is not None and (nímpar is None or npar <= nímpar):
        escreve_número(pares_ímpares, npar)
        npar = lê_número(pares)
    if nímpar is not None and (npar is None or nímpar <= npar):
        escreve_número(pares_ímpares, nímpar)
        nímpar = lê_número(ímpares)

pares_ímpares.close()
pares.close()
ímpares.close()'''
'''import sys

# Verifica se os parâmetros foram passados
if len(sys.argv) != 4:  # Lembre-se que o nome do programa é o primeiro da lista
    print("\nUso: e09-04.py primeiro segundo saída\n\n")
else:
    primeiro = open(sys.argv[1], "r")
    segundo = open(sys.argv[2], "r")
    saída = open(sys.argv[3], "w")

    # Funciona de forma similar ao readlines
    for l1 in primeiro:
        saída.write(l1)
    for l2 in segundo:
        saída.write(l2)

    primeiro.close()
    segundo.close()
    saída.close()'''
'''import sys
print("Número de parâmetros: %d" % len(sys.argv))
for n,p in enumerate(sys.argv):
 print("Parâmetro %d = %s" % (n,p))'''
'''import sys
if len(sys.argv) !=2:
    arquivo=open("números.txt","r")
    for linha in arquivo.readlines():
        print(linha[:-1])
else:
    nome=sys.argv[1]
    arquivo=open(nome,"r")
    for linha in arquivo.readlines():
        print(linha[:-1])'''
'''import sys
if len(sys.argv)!=4:
    print("Entre com todos os parâmetros na linha de comando")
else:
    nome=sys.argv[1]
    ini=int(sys.argv[2])
    fim=int(sys.argv[3])
    arquivo=open(nome,"r")
    for linha in arquivo.readlines()[ini-1:fim]:
        print(linha[:-1])
    arquivo.close()'''
'''impares=open("impar.txt","w")
pares=open("par.txt","w")
for i in range(1000):
    if i%2==0:
        pares.write(f"{i}\n")
    else:
        impares.write(f"{i}\n")
impares.close()
pares.close()'''
'''mult4=open("mult4.txt","w")
pares=open("par.txt")
for i in pares.readlines():
    if int(i)%4==0:
        mult4.write(f"{i}\n")
pares.close()
mult4.close()'''
'''pareimpar=open("pareimpar.txt","w")
impar=open("impar.txt")
par=open("par.txt")
for i in range(1000):
    if int(i) in impar:
         pareimpar.write(f"{i}\n")
    else:
       pareimpar.write(f"{i}\n")'''
'''def lê_número(arquivo):
    while True:
        número = arquivo.readline()
        # Verifica se conseguiu ler algo
        if número == "":
            return None
        # Ignora linhas em branco
        if número.strip() != "":
            return int(número)


def escreve_número(arquivo, n):
    arquivo.write(f"{n}\n")


pares = open("pares.txt", "r")
ímpares = open("ímpares.txt", "r")
pares_ímpares = open("pareseimpares.txt", "w")
npar = lê_número(pares)
nímpar = lê_número(ímpares)
while True:
    if npar is None and nímpar is None:  # Termina se ambos forem None
        break
    if npar is not None and (nímpar is None or npar <= nímpar):
        escreve_número(pares_ímpares, npar)
        npar = lê_número(pares)
    if nímpar is not None and (npar is None or nímpar <= npar):
        escreve_número(pares_ímpares, nímpar)
        nímpar = lê_número(ímpares)

pares_ímpares.close()
pares.close()
ímpares.close()'''
'''import sys
if len(sys.argv)!=4:
    print("Entre com todos os parâmetros")
else:
    primeiro = open(sys.argv[1], "r")
    segundo = open(sys.argv[2], "r")
    saída = open(sys.argv[3], "w")
    for i in primeiro:
        saída.write(f"{i}\n")
    for i in segundo:
        saída.write(f"{i}\n")
    primeiro.close()
    segundo.close()
    saída.close()'''
'''par=open("par.txt","r")
saída=open("paresinver.txt","w")
L=par.readlines()
L.reverse()
for i in L:
    saída.write(i)
par.close()
saída.close()'''
'''ent=open("entrada.txt","w")
ent.write("; não imprime\n")
ent.write("> imprime a direita\n")
ent.write("* imprime centralizada\n")
ent.write("linha normal\n")
ent.write("outra linha normal\n")
ent.write("=\n")
ent.write(".")
ent.close()'''
'''larg=79
entr=open("entrada.txt")
for linha in entr.readlines():
 if linha[0]==";":
  continue
 elif linha[0]==">":
  print(linha[1:].rjust(larg))
 elif linha[0]=="*":
  print(linha[1:].center(larg))
 else:
  print(linha)
entr.close()'''
larg=79
entr=open("entrada.txt")
for linha in entr.readlines():
    if linha[0]=="=":
       print("=*40\n")        
    elif linha[0]==".":
        y=input("pressione enter para parar de imprimir")
        while y!="":
            y = input("pressione enter para parar de imprimir")
    elif linha[0] == ">":
        print(linha[1:].rjust(larg))
    elif linha[0] == "*":
        print(linha[1:].center(larg))
    else:
        print(linha)
    entr.close()
'''saida=open("paginado.txt","w")
par=open("par.txt","r")
for linha in par.readlines():
    if len(linha)>76:
        print("\n")
    if linha>59:
        print()'''















