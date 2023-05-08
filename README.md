# Técnicas de simulación en computadoras - Ciclo 01-23

## Rama 'JS'

En esta rama se creo un pequeño programa modular de consola en NodeJS que permite el cálculo de las K y las B locales, dadas una lista de nodos y un par K y Q globales.

### LISTAS DE NODOS

El archivo `createNodes.py` es un archivo escrito en Python que sirve para generar un arreglo de objetos de JS, que tienen la siguiente forma:

```js
{
    x: 'value-x',
    y: 'value-y'
}
```

Al ejecutarlo, solicitara al usuario el número de nodos que existen en el mallado. Luego, solicitara el número de la lista de nodos que se va a crear.  
La ruta por defecto donde los archivos se guardan es `bin/data/nodeList-###.js` donde **###** es el número de archivo establecido por el usuario. Si se colocan 2 archivos con el mismo número, se reemplazará todo el contenido en el archivo anterior con el contenido del nuevo.

Cabe destacar que el archivo `bin/main.js` tendrá que ser modificado para determinar la lista de nodos globales que se quiera usar. El cambio se hace en la primera línea de código:

```js
// Archivo bin/main.js - línea 1
import nodeList from "./data/nodeList-ex1.js";
```

### MODO DE USO

Para utilizar el programa, se debe localizar en el directorio raiz. Primero, asegurarse de instalar los paquetes necesarios ejecutando el siguiente comando

```bash
npm install
```

Luego de haberlos instalado, correr el comando de la siguiente manera:

```
node . -k <> -q <>
```

Donde:

```
    -k, --global-k  The global k given  [number]
    -q, --global-q  The global q given  [number]
```

> Nota: Las opciones k y q son requeridas para el funcionamiento del programa

Seguido de esto, el programa preguntara por las referencias globales de los 3 nodos locales. Para esto se hace uso de la tabla de conectividades, y se ingresan los valores en orden. El programa luego responde con las K y B locales de los nodos globales establecidos por el usuario.

Finalmente, se le pregunta al usuario si quiere volver a calcular las K y B locales de otro elemento. Si la respuesta es `y`, el proceso se reinicia. De lo contrario, el programa se cierra.

### EJEMPLO

#### Posible tabla de conectividades del archivo `bin/data/nodeList-ex1.js`

|     |  1  |  2  |  3  |
| :-: | :-: | :-: | :-: |
|  1  |  1  |  2  |  4  |
|  2  |  2  |  3  |  4  |
|  3  |  4  |  3  |  5  |
|  4  |  6  |  1  |  4  |

Para el elemento tres:

```
Wich global is the local 1? 4
Wich global is the local 2? 3
Wich global is the local 3? 5
```

Respuesta del programa:

```js
// K global es 2
// Q global es 12

LOCAL K:
[
  [ '2.07', '0.43', '-2.50' ],
  [ '0.43', '0.57', '-1.00' ],
  [ '-2.50', '-1.00', '3.50' ]
]

LOCAL B:
[ [ '14.00' ], [ '14.00' ], [ '14.00' ] ]

```
Posibles opciones:
```
//Cierran el programa
Again? n
Again? No
Again? Si
Again? Yes
Again? asdfgh

//Repite el proceso
Again? y
```
