def calcula_area():
    area = PI * r **2
    print(f'A área do círculo é {area}')
    
    
def calcula_perimetro():
    perímetro = PI * 2 * r
    print(f'O perímetro é {perímetro}')
    
r = float(input('Raio: '))
PI = 3.14
calcula_area()
calcula_perimetro()