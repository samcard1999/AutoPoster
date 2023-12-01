from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import os
import time
 
 
LOGIN_URL = 'https://www.facebook.com/login.php'
service = Service(executable_path=GeckoDriverManager().install())


def init(mail, passw, browser='Chrome'):
        # Store credentials for login
        global driver 
        global email 
        email = mail
        global password 
        password = passw
        if browser == 'Chrome':
            # Use chrome
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
            # Set it to Firefox
            driver = webdriver.Firefox(service=service)
            driver.get(LOGIN_URL)
            time.sleep(1) # Wait for some time to load
 
 
 
def login():
        email_element = driver.find_element(By.ID,'email')
        email_element.send_keys(email) # Give keyboard input
 
        password_element = driver.find_element(By.ID,'pass')
        password_element.send_keys(password) # Give password as input too
 
        login_button = driver.find_element(By.NAME,'login') 
        login_button.click() # Send mouse click
 
        time.sleep(2) # Wait for 2 seconds for the page to show up

def CargarMensaje():
    print("Cargando mensaje")
    # Mensaje
    archivo = open("mensaje.txt", 'r', encoding="utf8")
    msj = archivo.read()
    archivo.close()
    return msj

def CargarGrupos():
    print("Cargando listado de grupos")
    # Lista de grupos
    archivo = open("grupos.txt", 'r')
    lg = []
    for grupo in archivo.readlines():
        lg.append(grupo)
    archivo.close()
    return lg

def CargarImagen():
    usi = int(input('''
        Ingrese una opcion
        0. No usar imagen
        1. Usar imagen
    '''))
    while (usi != 1 and usi != 0):
        print("Opcion incorrecta, vuelva a intentar")
        usi = int(input('''
            Ingrese una opcion
            0. No usar imagen
            1. Usar imagen
        '''))
    return usi

def CargarDireImagen(op):
    if (op == 1):
        print("Cargando direccion de la imagen")
        # Imagen
        imagen = os.path.join(os.getcwd(), "imagen.jpg")
    else:
        imagen = ""
    return imagen
 
 
if __name__ == '__main__':
    # Enter your login credentials here
    fb_login = init(mail='+5358511936', passw='Sam99yo69', browser='Firefox')
    login()
    print("Iniciando Programa")
usar_imagen = CargarImagen()
print("Configurando navegador")

mensaje = CargarMensaje()
lista_grupos = CargarGrupos()
imagen = CargarDireImagen(usar_imagen)

#Recorrido de grupos
i = 1
cantidad_lograda = 0
for grupo in lista_grupos:
    try:
        print("Entrando al grup " + str(i) + ". Link: " + grupo)
        driver.get(grupo)
        

        print("Realizando posteo")

        #Ubicar la caja de posteo
        p = driver.find_element(By.XPATH("xpath=//div[@id='mount_0_0_t6']/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/div/div/form/div/div/div/div/div/div/div/div/div[2]/div/i"))
        driver.find_element(By.XPATH("//div[contains(@class,'x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x6s0dn4 x1lq5wgf xgqcy7u x30kzoy x9jhf4c x78zum5 x1r8uery x1iyjqo2 xs83m0k xl56j7k x1pshirs x1y1aw1k x1sxyh0 xwib8y2 xurb0ha')]")).send_keys("\n")
        p.click()
        print("Enviando mensaje")          
        #Enviando mensaje
        p.click()
        time.sleep(3)
    except Exception as inst:

        print(type(inst)) 
        print ('FALSE')
