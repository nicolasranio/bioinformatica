1. ¿Podrías buscar un ejemplo de macromoléculas que almacenen información sobre la ‘identidad’ de un organismo dado?

    Un ejemplo es el ADN, que contiene toda la información genética necesaria para determinar las características y la identidad de un organismo.
    Esta informacion esta almacenada en forma de código genético el cual está compuesto por una secuencia de nucleótidos que contienen la información genética 

2. Proponé una forma de expresar la información contenida en la estructura primaria de las proteínas usando tipos de datos de los lenguajes de programación que conocés.

    Para el caso de la estructura primaria, donde unicamente importa el orden de los aminoacidos en la cadena, es suficiente con una estructura tipo lista,
    (por ejemplo un string) donde esten concatenados los aminoacidos que forman parte de la secuencia. 
    Ej: para la secuencia Metionina - Prolina - Serina - Leucina - Valina - Histidina - Alanina - Arginina - Treonina - Glicina - Lisina - Cisteína,
    una representacion podria ser 'MPSLVHARTGKC' donde cada aminoacido esta representado por su código de 1 letra

3. En qué tipo de datos podrías expresar la información de la estructura terciaria proteica?

    Para la estructura terciaria, es necesario ubicar el aminoacido de la secuencia en el espacio. Por ejemplo se podria representar 
    como una matriz tridimensional (en python se podria usar alguna herramienta que facilite su construccion, como numpy), donde cada amino de la secuencia de la proteina tenga asociada una coordenada.
    Ej: tomando como ejemplo la secuencia del desafio anterior, M = [1, 8, 3], P = [6, 2, 1] representan las coordenadas (x,y,z) 
    de la Metionina y la Prolina respectivamente. 


