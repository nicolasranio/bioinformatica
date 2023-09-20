
# El juego de la vida 

**Objetivo**: Comprender la traduccion del arn mensajero en una cadena de polipeptidos, mediante un juego que sume puntos por cada coincidencia que sea correcta.

**Definicion**: El juego consiste en una pantalla con dos secciones bien definidas. En la parte inferior se mostrara una cadena de ARNm (inicialmente con dos nucleotidos mas señales de start y stop) y en la parte superior diferentes tarjetas con aminoacidos (donde estan las respuestas correctas y otras de relleno) y un cronometro inicializado en 60 segundos. 

Cuando comienza el juego, el jugador debe poner su nombre. Una vez que comienza la partida (boton start), se muestra la cadena ARNm y comienza el contador. El jugador debe clickear la traduccion del nucleotido ARN en orden, por cada acierto suma 10 puntos, y si falla se restan 5 puntos (cambia la tarjeta a color verde si esta ok o rojo si es fallida, emitiendo un sonido). Luego de cada click, se agrega el amino traducido en una nueva cadena de resultados (polipeptido), únicamente si el resultado es correcto. Cuando se completo una cadena (con errores y aciertos), se genera una nueva con un nucleotido adicional. El juego termina cuando el timer llega a 0 o los puntos son 0.

Los resultados se guardan en un archivo y se muestran al final. Si el jugador ya existe en el registro y los puntos que cosecho superan los que ya tenia, se reemplazan por los puntos nuevos (siempre priorizando la partida con la mayor cantidad de puntos). Al terminar la partida se muestra un resumen de cada jugador con los puntos que cosecho.

Etapa 1 → pantalla de inicio con boton start tipo popup. Cuando le das a start se muestran tarjetas en la parte superior, ARNm con 4 nucleotidos en la parte inferior y el cronometro corriendo.

Etapa 2→ permite seleccionar las tarjetas y suma/resta puntos. El juego termina cuando el contador llega a 0 o los puntos son 0.

Etapa 3 → Pedir nombre al inicio del juego y mostrar pantalla con resultados al final.

  

## Instalacion

El juego fue desarrollando el framework online de Pilas Engine (https://pilas-engine.com.ar), el cual genera un build que se incluye en este repositorio. Tambien se incluye el archivo ```proyecto.pilas```, el cual se puede importar en el entorno online de pilas para poder ver/editar el codigo.

Para correr el proyecto en un ambiente local, situarse en la carpeta proyecto y ejecutar

para instalar dependencias:

  ```bash
  npm install
  ```

para ejecutar en un navegador local:

  ```bash
  npm start
  ```

  Previamente revisa que tengas alguna version de nodejs corriendo con el comando

  ```bash
  node --version
  ```

