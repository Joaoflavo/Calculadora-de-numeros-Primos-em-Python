print('Calculadora para descobrir números primos')
print('Programa Desenvolvido por João Flavo 12-10-2020 J°@°2@2@ 05:30 AM')
print('Digite um valor um valor, é descubra, todos os números primos de zero a cem:')
a = int(input('Digite o valor à ser calculado:'))
for num in range(a+1):
    div = 0
    for x in range (1, num+1):
         resto = num % x
         if resto ==0:
             div +=1
             if div ==2:
                print(num)
