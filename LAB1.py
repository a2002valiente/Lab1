import numpy as np
import wfdb
import matplotlib.pyplot as plt



##########################################################################
########################### FUNCIONES ####################################

def powimpulso (noisedos): # Se crea una funcion para calcular la potencia del ruido impulso
    n = len (noisedos) # se crea una variable y se le asigna el tamaño de la varible ruido
    sumatoria = 0 # se nicializa una variable para realizar un sumatoria 
    
    for c in noisedos: # se crea un bucle que recorra cada valor de la variable ruido 
        sumatoria += (c)**2 #se eleva cada valor al cuadrado y se suman
        powdos = sumatoria/n # e resultado anterior se divide por el total de datos de nuestra variaable
        
        return powdos # indicamos que valor debe salir de la funcion 


##########################################################################


def powarte (artefacto): # Se crea una funcion para calcular la potencia del ruido artefacto
    n = len (artefacto) # se crea una variable y se le asigna el tamaño de la varible ruido
    sumatoria = 0# se nicializa una variable para realizar un sumatoria 
    
    for b in artefacto:# se crea un bucle que recorra cada valor de la variable ruido
        sumatoria += (b)**2 #se eleva cada valor al cuadrado y se suman
        powtres = sumatoria/n# e resultado anterior se divide por el total de datos de nuestra variaable
        
        return powtres# indicamos que valor debe salir de la funcion 



##########################################################################
# Se realiza el mismo pprocedimiento de las funciones anteriores 
def ruido_impulso(forma,prob):
    
    ruidoimp = np.random.rand(*forma)
    ruidoimp[ruidoimp > prob] = 255
    ruidoimp[ruidoimp < 1 - prob] = 0
    
    return ruidoimp 


##########################################################################
# Se realiza el mismo pprocedimiento de las funciones anteriores 
def potegau1 (rg1):
    n = len (rg1)
    sumatoria = 0
    
    for a in rg1:
        sumatoria += (a)**2
        poteuno = sumatoria/n
        
        return poteuno

##########################################################################
# Se realiza el mismo pprocedimiento de las funciones anteriores 
def potesignal (valores):
    n = len (valores)
    sumatoriacu = 0
    
    for u in valores:
        sumatoriacu += (u)**2
        potencia = sumatoriacu / n
        
        return potencia 


##########################################################################
##########################################################################

# Calculos estadisticos desde cero
#Formulas Media, Desviacion y Coeficiente de variacion 


def calculos (valores): #Creamos una funcion para establecer las formulas desde cero
    n = len (valores) #creamos la variable n y le damos el valor de la longitud total de las muestras
    sumatoria = 0 #inicializamos la variable sumatoria, la cual permiira almacenar la suma de cada elemento
    
    #1. Calculo de la media
    
    for i in range (n): # se crea un bucle para recorrer y almacenar cada elementos de n
        sumatoria += valores [i] #sumamos cada elemento a la suma total
        mu = sumatoria / n #dividimos toda la suma en el total de datos 
    
    #2. Calculo de la desviacion estandar
        
    suma_cuadrados_diferencia = 0 #inicializamos una variable para almacenar la formula x-mu**2
    for x in valores: # se crea un bucle para recorrer y almacenar cada elementos de n
        suma_cuadrados_diferencia += (x-mu)**2 #sumamos cada valor de nuestra variable 'valores'... 
        #restando la media a cada valor y elevando al cuadrado el resultado
        varianza = suma_cuadrados_diferencia / n # dividimos el resultado anterior por el numero
        #total de datos
        sigma = np.sqrt(varianza) # por ultimo aplicamos raiz cuadrada 
       
        
    #3. Calculo del coeficiente de variacion
        
    cv = sigma / mu #Creamo una nueva variable para dividir desviacion estandar entre la media
    cvpercent = np.abs (cv) * 100 #Aplicamos valor absoluto al resultado y multiplicamos por 100
    #para obtener el porcentaje del coeficiente de variacion
    
    return mu,sigma,cv, cvpercent   

#######################################################################
################################---CLASE ---##############################


#Cargar la informacion hay que cargar ambos archivos
signal = wfdb.rdrecord('01')
 
#Verificacion de la carga 
print (signal.n_sig)

#Visualizar valores de la señal
print (signal.p_signal)

#Comprobar valores que hay 
print (signal.sig_len)

#Almacenar los valores en una variable para poder manpularlos.
valores = signal.p_signal[:,0]

plt.figure (0)
plt.plot (valores,'green', label='Señal Obtenida') # graficar los datos con un color especifico 
#y su respectiva leyenda
plt.grid(True) #agregamos rejillas a la grafica 
plt.xlim(0, len(valores)) # limitamos los ejes para una mejor visualizacion
plt.ylim(-5, 5)
plt.xlabel ("Muestras") #nombramos los ejes
plt.ylabel ("Amplitud (mV)")
plt.title("Señales de ECG, con patologias cardiacas") #nombramos nuestra grafica 
plt.legend( loc='upper right') #ubicamos la leyenda en la parte superior derecha para
#mejorar la visualizacion 
plt.show

############################################################################
###############################----Prints----#####################################

mu, sigma, cv, cvpercent = calculos(valores) #se extrae los valores de la funcion calculos desde cero
print ("Datos Estadisticos Creados Desde Cero") # se imprime cada resultado 
print("\n")
print ("La media es:",mu)
print ("La desvicion estandar es:",sigma)
print ("El coeficiente de variacion es:",cvpercent)
print("\n")

############################################################################
##########################---- CALCULO FUNCIONES----########################


# Calculo media, desviacion estandar y coeficiente de variacion
#con las funciones de NumPy, aplicadas a la variables valores

media = np.mean (valores)
desviacion_estandar = np.std(valores)
coeficiente_varacion = np.abs ( desviacion_estandar / media ) *100

############################################################################
###############################----Prints----#####################################

#Se imprime cada valor de los calculos con funciones 
print ("Datos Estadisticos Con Funciones")
print("\n")
print ("La media es:",media)
print ("La desvicion estandar es:",desviacion_estandar)
print ("El coeficiente de variacion es:",coeficiente_varacion)
print("\n")

#Se imprimen el calculo de nuestra señal
print ("Calculos de potencias de ruidos, señal y SNR:")
print("\n")
potencia = potesignal(valores) #se extrae los valores de la funcion
print ("La potencia de la señal es:", potencia)
print("\n")


############################################################################
#########################--- HISOTGRAMA DESDE CERO ---########################## 


k = 1 + 3.322 * np.log(len(valores)) #Calcular intervalos con la ley de sturges
k_redondeado = int(np.round(k)) # redondear al numero entero mas cercano
#calcular valor maximo y minimo para calcular el rango 
valormax = np.max(valores) 
valormin = np.min(valores) 
rango = valormax - valormin #creamos la variale rango para hacer el respectivo calculo 
amplitud = rango / k_redondeado # se divide el rango con el numero de intervalos para obtener la amplitud
bins = np.linspace(valormin, valormax, k_redondeado + 1) # damos un valor inicial y final y aseguramos
#con el numero de intervalos + 1 que se tomen todos los valores incluso el final 


#Generamos grafica de histograma 
plt.figure (1)
counts, bins, patches = plt.hist(valores, bins=bins, edgecolor='black') # counts permite 
#regresar los valores a plt.hist y da dos arreglos, 1 la señal y el segundo los puntos medios 
bin_centers = (bins[:-1] + bins[1:]) / 2 # Obtener los puntos medios de cada bin
plt.plot(bin_centers, counts, '-o') #graficamos el poligono de frecuencia 
plt.hist(valores, bins=bins, edgecolor='black', label ='Datos histograma')
plt.grid (True)
plt.xlabel("Muestras")
plt.ylabel("Frecuencia")
plt.title("Histograma de la señal, obtenido desde cero")
plt.legend( loc='upper right')
plt.show() 




#########################--- HISOTGRAMA CON FUNCIONES ---########################## 
plt.figure (2)
plt.hist(valores,edgecolor='black', label = 'Datos') # se aplica la funcion de grafica de histograma de 
#Matplotlib directamente a la variable valores.
plt.xlabel ("Muestras")
plt.ylabel ("Frecuencia")
plt.title("Histograma de los datos, generado con funciones")
plt.grid (True)
plt.legend( loc='upper right')
plt.show()



########################################################################
#########################---RUIDOS---###################################

####-----------RUIDO GAUSSIANO-------------####

#Generacion del ruido 
fs = 43201 # se crea la variable representtiva de la frecuencia de muestreo ajustando la resolucion
#temporal en el total de datos de nuestra señal principal 
t = np.arange(0,1,1/ fs) #creamos un arreglo que inicia en 0, termina en 1 y va de a un paso
noiseuno = np.random.randn(len(t)) #generamos números aleatorios siguiendo una distribución normal estándar
#con una longitud del arreglo t 

plt.figure (3)
plt.plot(noiseuno,'red', label ='Ruido Gaussiano') #aplicamos color y leyenda a los datos
plt.grid (True) # generamos una rejilla 
plt.ylim (-5,5)# aplicamos limites a los ejes para mejor visualizacion
plt.xlabel ("Tiempo (s)")
plt.ylabel ("Amplitud del ruido")
plt.title("Grafica de Ruido Gaussiano")
plt.legend (loc = 'upper right')
plt.show

#Configuracion para extraer variables de potencias de las funciones e imprimir
ruido1 = noiseuno
rg1 = ruido1
poteuno = potegau1(rg1) # se extrae el valor de la potencia de nuestra funcion de calculo
print ("La potencia del ruido Gaussiano es:", poteuno)

#Calculo de los dos SNR de ruido gaussiano 
snr1y2 = 10 * np.log10 (potencia/poteuno) #creamos una variable que nos permita calcular el SNR
print ("SNR 1 / 2 es:",snr1y2,"dB")
print("\n")
#Suma de las graficas (señal y ruido)



# Sumamos las graficas para ver la contaminacion con ruido gaussiano 
plt.figure (4)
plt.grid (True)
plt.plot (noiseuno, 'red', label = 'Ruido Gaussiano')
plt.plot (valores,'green', label = ' Señal Limpia')
plt.xlim(0,len(valores)) #aplicamos limites a los ejes 
plt.ylim(-6,6)
plt.title("Señal contaminada con ruido Gaussiano")
plt.xlabel("Muestras")
plt.ylabel("Amplitud(mV)")
plt.legend(loc = 'upper right')
plt.show

#################################################################
#################################################################


####-----------RUIDO IMPULSO-------------####
#Generacion del ruido 

num_impulsos = 200 # se crea una variable que almacene el numero de implusos 
amplitud_imp = 0.5 # se elije la amplitud 


noisedos = np.ones(fs) # se crea una variable de '1' y se multiplica por 43201
#con el fin de obtener una variable del tamño de nuestra señal 
posicionimp = np.random.choice(fs,num_impulsos,replace = False) # se crea una funcion que 
#selecione numeros al azar, determinando cuántos números aleatorios queremos seleccionar. 
#de acuerdo a implusos y creamos una condicion para que no se puedan repetir 

noisedos [posicionimp] = amplitud_imp * np.random.randn(num_impulsos)# traemos a la variable 
#que contiene las posiciones de impulsos aleatoria y generamos ruido aleatorio
#multiplicado por la variable que define la amplitud de los impulsos.


plt.figure(5)
plt.grid (True)
plt.plot(noisedos,'purple', label ='Ruido impulso')
plt.xlim(0,len(valores))
plt.ylim (-6,6)
plt.xlabel ("Tiempo (s)")
plt.ylabel ("Amplitud de ruido")
plt.title("Grafica generacion del ruido Impluso")
plt.legend (loc = 'upper right')
plt.show

# sumamos la señal limpia con la señal de ruido impulso 
plt.figure(6)
plt.grid (True)
plt.plot (noisedos,'purple', label='Ruido impulso')
plt.plot (valores,'green', label ='Señal limpia')
plt.xlim(0,len(valores))
plt.ylim (-6,6)
plt.xlabel ("Muestra")
plt.ylabel ("Amplitud (mV)")
plt.title("Señal contaminada con ruido impulso")
plt.legend (loc ='upper right')
plt.show

powdos = powimpulso(noisedos)*(-1)# extraemos la variable de potencia del ruido de a funcion
print("La potencia del ruido de impulso es:",powdos)
snr3y4 = 10 * np.log10 (potencia/powdos) # cremos una variable que permita visualizar el calculo
#del SNR
print ("El SNR 3 / 4 es:",snr3y4,"dB")
print("\n")
#################################################################
#################################################################
 

####-----------RUIDO ARTEFACTO-------------####
#Generacion del ruido 

frecuartefac = 60 # se crea una varible que contenga la frecuencia del artefacto 
ampliartefac = 2.5 # esta variable almacena la amplitud del ruido 
t = np.arange (len(valores))/fs # se crea un arreglo de tiempo de la longitud total de valores y se 
#divide por la frecuencia de muestreo 
artefacto = ampliartefac *np.sin (2*np.pi*frecuartefac*t) # se genera una onda sinusoidal y se 
#multiplica y calcula cada elemento para definir la amplitud y frecuencia de nuesra onda 



plt.figure(7)
plt.grid (True)
plt.plot (artefacto, 'pink', label = 'Ruido artefacto')
plt.xlim (0, len(valores))
plt.ylim (-6,6)
plt.xlabel ("Tiempo (s) ")
plt.ylabel ("Amplitud")
plt.title("Grafica de generacion del ruido artefacto")
plt.legend(loc = 'upper right')
plt.show


plt.figure(8)
plt.grid (True)
plt.plot(artefacto,'pink', label = 'Ruido Artefacto') 
plt.plot(valores,'green', label = 'Señal Limpia')    
plt.xlim (0,len(valores))
plt.ylim(-6,6)
plt.xlabel ("Muestras")
plt.ylabel ("Amplitud (mV)")
plt.title("Señal contaminada con ruido artefacto")
plt.legend(loc = 'upper right')
plt.show  

powtres = powarte(artefacto) # se extrae la potencia de la funcion para los calculos
print ("La potencia del ruido artefacto es:", powtres)
snr5y6 = 10 * np.log10 (potencia / powtres) # se calcula el respectivo SNR 
print ("El SNR 5 / 6 es:", snr5y6,"dB")



