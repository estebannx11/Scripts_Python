import colorama

colorama.init()
color_green = colorama.Fore.GREEN
color_blue = colorama.Fore.WHITE
banner = f'''
   _________     ___.                  .__         __________     ___.   .__  .__               
 /   _____/____ \_ |__   ___________  |__|_____   \______   \__ _\_ |__ |  | |__| ____ _____   
 \_____  \\__  \ | __ \_/ __ \_  __ \ |  \____ \   |     ___/  |  \ __ \|  | |  |/ ___\\__  \  
 /        \/ __ \| \_\ \  ___/|  | \/ |  |  |_> >  |    |   |  |  / \_\ \  |_|  \  \___ / __ \_
/_______  (____  /___  /\___  >__|    |__|   __/   |____|   |____/|___  /____/__|\___  >____  /
        \/     \/    \/     \/           |__|                         \/             \/     \/ 
         __________        .__                   .___       
 ___.__. \______   \_______|__|__  _______     __| _/____   
<   |  |  |     ___/\_  __ \  \  \/ /\__  \   / __ |\__  \  
 \___  |  |    |     |  | \/  |\   /  / __ \_/ /_/ | / __ \_
 / ____|  |____|     |__|  |__| \_/  (____  /\____ |(____  /
 \/                                       \/      \/     \/ 
        '''

dibujo_coloreado = color_green + banner + color_blue
print(dibujo_coloreado)

def programa():
    import socket 
    import urllib.request

    #capturar nombre del equipo
    hostname = socket.gethostname()

    #ip privada equipo
    ip_privada = socket.gethostbyname(hostname)

    print(f"=============================================")
    print("El nombre del equipo es: "+ hostname)
    print(f"=============================================")
    print("La ip del equipos es: "+ ip_privada)
    print(f"=============================================")

    ip_publica = urllib.request.urlopen('https://ident.me').read().decode('utf8')

    print(f"=============================================")
    print('La ip pública es:'+ ip_publica)
    print(f"=============================================")

    print('''
        ┌─────────────────────────────────────────────┐
        │       Gracias por usar el Programa          │
        ├─────────────────────────────────────────────┤
        │         Hasta la Proxima                    │
        ├─────────────────────────────────────────────┘
                                                    ''')
    
programa()