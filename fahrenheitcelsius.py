def celsius():
    C = ((f-32)/9)*5
    print(f'A temperatura é {f}°F em graus Celsius é {C:.2f}°C')

try:
    f = float(input('Digite a temperatura: '))
except:
    print('Valor digitado errado')
celsius()

