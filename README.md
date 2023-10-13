# MNIXEL
Este es un programa que permite dibujar numeros del mismo tipo que MNISt y irlos guardando en el computador, inicialmente creado para facilitar y hacer mucho mas rapida la creacion de una minibase de datos.
## Modo de uso
El programa te va mostrando numeros para que vayas dibujando, siempre te mostrara todos los numeros del 0 al 9 aleatorimente sin repetir hasta que completes los 10 (un grupo de 10 es llamado paquete). Una vez completes un paquetee el programa los guardara en una archivo MNIST.npz en la ruta del .exe, que es un archivo de numpy que puedes cargar facilmente en cualquier codigo de python con: 
```python
datos_cargados = np.load('MNIST.npz')
mi_X = datos_cargados['X']
mi_y = datos_cargados['y']
```

Si sigues creando paquetes, estos se guardarn en el mismo archivo.

:warning: **¡Advertencia!** Si vuelves a ejecutar el programa, los nuevos numeros remplazaran a los numeros anteriores, asegurate de guardar tus archivos antes de volver a ejecutarlo.


## Capturas
![Captura](https://github.com/Konat23/MNIXEL/assets/68023761/e739e9eb-d7eb-4f0a-bcba-1a0091ef2c5d)

![image](https://github.com/Konat23/MNIXEL/assets/68023761/e9fd1c57-bbba-4c28-a327-b56e9ca4fd0d)

## How to install
### Windows
The last version is avalible as .exe in github. Go to [Release](https://github.com/Konat23/MNIXEL/releases) and download and run the Mnixel.exe

### Source code
An anaconda envoriment is available. 
1. Clone or download this repository
2. Instalar anaconda y ejecutar anaconda prompt
3. Ir a la ruta del repositorio ```.../MNIXEL>```
4. Create your anaconda enviroment: ```conda env create -f entorno.yml```

