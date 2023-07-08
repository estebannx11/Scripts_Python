user_ = 'admin'
passw_ = '123'

print('''
        ┌─────────────────────────────────────────────┐
        │             Bienvenido                      │
        ├─────────────────────────────────────────────┤
        │         Por favor ingrese los datos         │
        ├─────────────────────────────────────────────┘
''')

def comprobaruseandpassw():
    user = input('Ingrese su usuario: ')
    passw = input('Igrese la contraseña: ')

    if user==user_ and passw==passw_:
        print('Bienvenido al programa!!! (:')
    else:
        print('Usuario o Contraseña Invalidos ):')
comprobaruseandpassw()