def celsius():
    C = ((f-32)/9)*5
    print(C)

try:
    f = float(input('Digite a temperatura: '))
except:
    print('Valor digitado não errado')
celsius()
