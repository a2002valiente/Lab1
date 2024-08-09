---
title: "README"
author: "Sebastian Ochoa, Andrea Valiente"
date: "2024-08-09"
output: html_document
editor_options: 
  markdown: 
    wrap: 72
---

***LABORATORIO 1: Análisis estadístico de la señal***

------------------------------------------------------------------------

```         
                                                                                                                  Sebastian Ochoa 
                                                                                                                  Andrea Valiente 
                                                                                                                        UMNG 
```

------------------------------------------------------------------------

> **Objetivo:** En esta practica se busca identificar los datos
> estadísticos que describen una señal biomédica, para obtenerlos a
> partir de algoritmos de programación y mostrarlos.

------------------------------------------------------------------------

**Descripción:** Se escogio una ECG, ***(Brno University of Technology
ECG Signal Database with Annotations of P Wave (BUT PDB))*** es una base
de datos de señales de ECG con picos de onda P marcados creada por el
equipo de cardiología del Departamento de Ingeniería Biomédica de Brno
University of Technology. La base de datos consta de 50 grabaciones de
señales de ECG de 2 derivaciones de 2 minutos de duración con diversos
tipos de patología. Los ECG se seleccionaron de tres bases de datos de
señales de ECG existentes: la base de datos de arritmias MIT-BIH, la
base de datos de arritmias supraventriculares MIT-BIH y la base de datos
de FA de larga duración para calcular los datos estadísticos que la
describen para ello nos piden lo siguiente :

-   Media de la señal
-   Desviación estándar
-   Coeficiente de variación
-   Histogramas
-   Función de probabilidad

Ademas se pide contaminar esta señal con los siguentes ruidos :
Guassiano, impulso y de artefacto para calcular la potencia y el SNR de
cada una de ellas siendo asi posible visualizar cada una y unidas estos
ruidos con la señal original

***Instrucciones***

1.  Para el desarrollo de la guia se descargo la señal ECG anteriormente
    mencionada de la pagina ***Physionet*** verificando que tuviera los
    archivos .dat y .hea procediendo a su descarga ,dejando estos 3
    archivos en una carpeta sola siendo mas facil su busqueda .

2.  Utlizamos una interfaz grafica en nuestro caso es ***Anaconda
    navigator*** donde se uso***spyder*** en lenguaje de phyton,cargando
    la señal adquirida obteniendo la matriz de datos volviendola una
    variable que se llama **valores** que posteriormente se graficaria
    para poder visualizar la señal.

-   Se importan las librerias correspondientes.

-   Se añade la señal adquirida mediante el codigo mostrado.

-   Se da un nombre a la variable de la señal.

-   Se grafican los datos

    ````         
       ```           
     import numpy as np
     import wfdb
     import matplotlib.pyplot as plt
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
     plt.legend( loc='upper right') #ubicamos la leyenda en la parte superior derecha para mejorar la visualizacion 
     plt.show
    ````

    \`\`\`

![Señal ECG con patologia cardiacas](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20014130.png){width="400"}

3.Calculamos los datos estadisticos de dos maneras diferentes cuando fue
posible desde cero y haciendo uso de las funciones predefinidas de
python ,los datos que obtuvimos fueron los siguientes:

-   Creamos una funcion *Calculos* para crear las formulas desde cero

    ```         
     def calculos (valores): #Creamos una funcion para establecer las formulas desde cero
     n = len (valores) #creamos la variable n y le damos el valor de la longitud total de las        muestras
     sumatoria = 0 #inicializamos la variable sumatoria, la cual permiira almacenar la suma de       cada elemento
    ```

------------------------------------------------------------------------

***DESDE CERO***

------------------------------------------------------------------------

> **Media**
>
> > Se encuentra al sumar todos los números en el conjunto de datos y
> > luego al dividir entre el número de valores en el conjunto.

```         
    for i in range (n): # se crea un bucle para recorrer y almacenar cada elementos de n
        sumatoria += valores [i] #sumamos cada elemento a la suma total
        mu = sumatoria / n #dividimos toda la suma en el total de datos 
```

> **Desviación estandar**
>
> > Es una medida de extensión o variabilidad en la estadística
> > descriptiva. Se utiliza para calcular la variación o dispersión en
> > la que los puntos de datos individuales difieren de la media

```         
  suma_cuadrados_diferencia = 0 #inicializamos una variable para almacenar la formula x-mu**2
  for x in valores: # se crea un bucle para recorrer y almacenar cada elementos de n
  suma_cuadrados_diferencia += (x-mu)**2 #sumamos cada valor de nuestra variable 'valores'...     restando la media a cada valor y elevando al cuadrado el resultado
  varianza = suma_cuadrados_diferencia / n # dividimos el resultado anterior por el numer total   de datos
  sigma = np.sqrt(varianza) # por ultimo aplicamos raiz cuadrada 
```

> **Coeficiente de variación**
>
> > Es una medida de dispersión que permite el análisis de las
> > desviaciones de los datos con respecto a la media y al mismo tiempo
> > las dispersiones que tienen los datos dispersos entre sí

```         
        cv = sigma / mu #Creamo una nueva variable para dividir desviacion estandar entre la media
        cvpercent = np.abs (cv) * 100 #Aplicamos valor absoluto al resultado y multiplicamos por 100
        #para obtener el porcentaje del coeficiente de variacion

        return mu,sigma,cv, cvpercent   
```

-   Ahora utilizamos la función Print para que se muestren los
    resultados

    ```         
      mu, sigma, cv, cvpercent = calculos(valores) #se extrae los valores de la funcion calculos desde cero
     print ("Datos Estadisticos Creados Desde Cero") # se imprime cada resultado 
     print("\n")
     print ("La media es:",mu)
     print ("La desvicion estandar es:",sigma)
     print ("El coeficiente de variacion es:",cvpercent)
     print("\n")
    ```

-   Valores obtenidos con el código

![Valores obtenidos](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20015434.png)

------------------------------------------------------------------------

> **Histograma con calculos**
>
> > Es un gráfico que usa barras para simbolizar cómo se distribuye un
> > conjunto de datos.

```         
        k = 1 + 3.322 * np.log(len(valores)) #Calcular intervalos con la ley de sturges
        k_redondeado = int(np.round(k)) # redondear al numero entero mas cercano
        #calcular valor maximo y minimo para calcular el rango 
        valormax = np.max(valores) 
        valormin = np.min(valores) 
        rango = valormax - valormin #creamos la variale rango para hacer el respectivo calculo 
        amplitud = rango / k_redondeado # se divide el rango con el numero de intervalos para obtener la amplitud
        bins = np.linspace(valormin, valormax, k_redondeado + 1) # damos un valor inicial y final y aseguramos
        #con el numero de intervalos + 1 que se tomen todos los valores incluso el final 
```

-   Grafico del histograma

![Histograma creado desde cero](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20020059.png)

***Calculos realizados con funciones***

> Mediante las funciones predefinidas de phyton se obtuvieron los
> calculos de la media , desviación estandar y el coeficiente de
> variación, histograma y asi mismo se grafica para ser visualizado su
> valor

```         
    # Calculo media, desviacion estandar y coeficiente de variacion
    #con las funciones de NumPy, aplicadas a la variables valores
    media = np.mean (valores)
    desviacion_estandar = np.std(valores)
    coeficiente_varacion = np.abs ( desviacion_estandar / media ) *100
    
    #Se imprime cada valor de los calculos con funciones 
    print ("Datos Estadisticos Con Funciones")
    print("\n")
    print ("La media es:",media)
    print ("La desvicion estandar es:",desviacion_estandar)
    print ("El coeficiente de variacion es:",coeficiente_varacion)
    print("\n")
```

![Histograma con funciones](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20020906.png)
![Resultado calculos con funciones](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20020918.png)

4.Para la contaminación la señal ECG se utilizaron 3 tipos de ruidos el
Gaussiano,de imulso ,de artefacto y asi generar una funcion que
encuentre la **potencia** de la señal ECG como de los ruidos para hallar
el **SNR** que es una medida que compara la potencia de una señal
deseada con la potencia del ruido de fondo. Se expresa generalmente en
decibelios (dB) y se utiliza para evaluar la calidad de una señal de
transmisión,si el SNR es positivo quiere decir que la señal es mas
grande que el ruido (mayor información) y es negativo el ruido es mas
grande que la señal (menor informacíon) .\* De cada rudio mencionado
anteriormente .Ademas se visualizaran cada tipo de ruido y la suma con
la señal adquirida.

-   Utilizando las funciones obtenemos la potencia de la señal ECG y
    extraemos el valor calculado de la potencia para poder utlizarlo en
    otros calculos e imprimirlo.

    ```         
          def potesignal (valores):
           n = len (valores)
           sumatoriacu = 0
           for u in valores:
          sumatoriacu += (u)**2
           potencia = sumatoriacu / n
          return potencia 
    ```

    ```         
     #Se imprimen el calculo de nuestra señal
     print ("Calculos de potencias de ruidos, señal y SNR:")
     print("\n")
     potencia = potesignal(valores) #se extrae los valores de la funcion
     print ("La potencia de la señal es:", potencia)
     print("\n")
    ```

![Resultado de la poencia de la señal:](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20021724.png)

**RUIDO GAUSSIANO**

-   se refiere a un tipo de ruido aleatorio cuyas muestras son
    independientes entre sí y siguen una distribución normal

    ```         
     fs = 43201
     t = np.arange(0,1,1/ fs)
     noiseuno = np.random.randn(len(t))
     plt.figure (3)
     plt.plot(noiseuno)
     plt.xlabel ("dB")
     plt.ylabel ("Amplitud")
     plt.title("Ruido Gaussiano")
     plt.legend ("Gaussiano")
     plt.show
    ```

-   Acontinuación se muestra la grafica del ruido Gaussiano

![Grafica del ruido Gaussiano:](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20021909.png)

-   Medimos la potencia del ruido Gaussiano y a la señal ECG para
    encontrar el SNR positivo y negativo

    ```         
          def potegau1 (rg1):
          n = len (rg1)
          sumatoria = 0
          for a in rg1:
          sumatoria += (a)**2
          poteuno = sumatoria/n
          return poteuno
    ```

-   Se utliza las siguientes formulas para poder hallar la medida de
    estos y posteriormente graficar las sumas de las dos señales

    ```         
    #Configuracion para extraer variables de potencias de las funciones
    e imprimir
    ruido1 = noiseuno
    rg1 = ruido1
    poteuno = potegau1(rg1)
    print ("La potencia del ruido Gaussiano es:", poteuno)

    #Calculo de los dos SNR de ruido gaussiano
    snr = 10 \* np.log10(potencia/poteuno) 
    print ("SNR1 es:",snr)

    #Suma de las graficas (señal y ruido)
    plt.figure (4)
    plt.grid(True) 
    plt.plot (noiseuno, 'red', label = 'Ruido Gaussiano')
    plt.plot (valores,'green', label = ' Señal Limpia')
    plt.xlim(0,len(valores)) #aplicamos limites a los ejes
    plt.ylim(-6,6) 
    plt.title("Señal contaminada con ruido Gaussiano")
    plt.xlabel("Muestras") 
    plt.ylabel("Amplitud(mV)") 
    plt.legend(loc ='upper right') 
    plt.show
    ```

-   Obteniendo asi el valor de estas medidas y ademas la suma de las dos
    graficas. A continucion se mostrara el resultado de la potencia de
    ruido y las graficas resultados de los SNR tanto para el postivo
    como el negativo.

![Resultado de la potencia del ruido Gaussiano y SNR 1:](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20022727.png)

![Grafica señal contaminada con ruido Gaussiano y SNR negativo:](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20022739.png)

![Resultado de la potencia del ruido Gaussiano y SNR 2:](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20023451.png)

![Grafica señal contaminada con ruido Gaussiano y SNR positivo:](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20023459.png)

Para las señales de ruido Gaussiano cuando el ruido es menor que la
señal en amplitud obtenemos un SNR positivo, en cambio cuando el ruido
es mayor que la señal el SNR tiende a ser negativo como se visualiza en
las imagenes.

**RUIDO DE IMPULSO**

-   Se caracteriza por un sonido muy alto que ocurre de forma súbita, se
    presenta con un aumento brusco durante un breve periodo, lo que lo
    diferencia de otros tipos de ruido.

    ```         
          num_impulsos = 200
          amplitud_imp = 2
          noisedos = np.ones(fs)
          posicionimp = np.random.choice(fs,num_impulsos,replace = False)
          noisedos [posicionimp] = amplitud_imp * np.random.randn(num_impulsos)
          plt.figure(5)
          plt.plot(noisedos)
          plt.xlabel ("dB")
          plt.ylabel ("Amplitud")
          plt.title("Ruido Impluso")
          plt.legend ("Impulso")
          plt.show
    ```

-   Acontinuación se muestra la grafica del ruido de impulso

![Grafica del ruido impulso:](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20023800.png)

-   Medimos la potencia del ruido de potencia y a la señal ECG para
    encontrar el SNR positivo y negativo

    ```         
    def powimpulso (noisedos):
        n = len (noisedos)
        sumatoria = 0

        for c in noisedos:
          sumatoria += (c)**2
          powdos = sumatoria/n

          return powdos
    ```

-   Se utliza las siguientes formulas para poder hallar la medida de
    estos y posteriormente graficar las sumas de las dos señales

    ```         
          powdos = powimpulso(noisedos)
          print("La potencia del ruido de impulso es:",powdos)
          snr2 = 10 * np.log10 (potencia/powdos)
          print ("El SNR2 es:",snr2)
          plt.figure(6)
          plt.plot (noisedos)
          plt.plot (valores)
          plt.xlabel ("dB")
          plt.ylabel ("Amplitud")
          plt.title("Señal contaminada con ruido impulso")
          plt.legend ("Impulso")
          plt.show
    ```

-   Obteniendo asi el valor de estas medidas y ademas la suma de las dos
    graficas, a continuacion se muestran los resultados y graficas del
    SNR negativo y postivo.

![Resultado de la potencia del ruido impluso y SNR3](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20024233.png)

![Grafica señal contaminada con ruido impulso y SNR negativo](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20024241.png)

![Resultado de la potencia del ruido impluso y SNR4](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20025532.png)\
![Grafica señal contaminada con ruido impulso y SNR positivo](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20025423.png)

Se noto que la señal del ruido de impulso cuando se incrementa su
amplitud y es mayor que la amplitud de la señal limpia o visceversa el
SNR tiende a ser negativo. Esto se puede deber a la funcion utlizada en
el arreglo incial el cual tiene como objetivo obtener una variable del
tamaño total de la señal pura. se utilizo la funcion np.ones la cual
convierte los 43201 valores en 1.

**RUIDO DE ARTEFACTO**

-   Efecto sonoro accidental o no deseado, resultante de la edición o la
    manipulación de un registro sonoro

    ```         
          frecuartefac = 60
          ampliartefac = 2.5
          t = np.arange (len(valores))/fs
          artefacto = ampliartefac *np.sin (2*np.pi*frecuartefac*t)
          plt.figure(7)
          plt.plot (artefacto)
          plt.xlabel ("dB")
          plt.ylabel ("Amplitud")
          plt.title("Ruido artefacto")
          plt.show
    ```

-   Acontinuación se muestra la grafica del ruido de artefacto

![Grafica del ruido artefacto](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20025808.png)

-   Medimos la potencia del ruido de artefacato y a la señal ECG para
    encontrar el SNR positivo y negativo

    ```         
          def powarte (artefacto):
           n = len (artefacto)
          sumatoria = 0
          for b in artefacto:
           sumatoria += (b)**2
          powtres = sumatoria/n
          return powtres
    ```

-   Se utliza las siguientes formulas para poder hallar la medida de
    estos y posteriormente graficar las sumas de las dos señales

    ```         
          powtres = powarte(artefacto)
          print ("La potencia del ruido artefacto es:", powtres)
          snr3 = 10 * np.log10 (potencia / powtres)
          print ("El SNR3 es:", snr3)
          plt.figure(8)
          plt.plot(artefacto) 
          plt.plot(valores)    
          plt.show  
    ```

-   Obteniendo asi el valor de estas medidas y ademas la suma de las dos
    graficas.

![Grafica de la señal contaminada con ruido artefacto y SNR negativo](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20030206.png)
![Grafica de la señal contaminada con ruido artefacto y SNR positivo](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20030313.png)
![SNR infinito:](C:/Users/seeba/Pictures/Screenshots/Captura%20de%20pantalla%202024-08-09%20030426.png)

Se pudo observar que al disminuir el valor de la amplitud de la señal
del ruido artefacto al momento de graficarla y sumarla a la señal ECG.
Se logra evidencia que el rudo es menor a la señal por tanto deberia
tener un SNR posiivo. Sin embargo, al ser una señal sinusoidal con una
longitud extensa y amplitudes bajas. los valores ubicados en cada
espacio determinado son demasiado pequeños y al momento de sacar la
potencias van a tender a cero. por lo que al momento de extraer la
fucion de la potencia y evaluarla junto con la potencia de la señal en
la variable que calcula el SNR. Termina siendo un decimal divido cero
por lo que el SNR tanto con una amplitud mayor a la señal o menor tiende
a infinito.

\`\`\`
