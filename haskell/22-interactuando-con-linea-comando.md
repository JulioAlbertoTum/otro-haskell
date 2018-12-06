# Interactuando con la linea de comando y I/O perezoso

A menudo cuando las personas aprenden sobre I/O en Haskell asumimimos que I/O cambia a haskell. Ya que I/O es es cualquier cosa pero no puro. Pero hay otra forma de ver I/O como algo unico de haskell que es torpe en otros lenguajes. 

En otros lenguajes hablamos de I/O streams, pero que es un stream? Una buena forma de entender I/O streams es como una evaluacion perezosa de una lista de caracteres. STDIN treams son ingresadas por el usuario hacia un programa como  hasta que un eventual fin es alcanzado. Pero al final esto no siempre se conoce (en teoria nunca puede ocurrir). Esto es exactamente en como pensar sobre listas de haskell usando evaluacion perezosa.

I/O se usa en todos los lenguajes de programacion cuando leemos de grandes archivos. A menudo es inpractico o imposible, leer un gran archivo en memoria antes de operar sobre esta. Pero imagina que un gran archivo simplemente es  algun texto asignado a una variable y la variable fue una lista perezosa. Como aprendimos antes, la evaluacion perezosa nos permite operar sobre listas largas, No importa cuan larga sea la entrada, puedes manejar si tratas el problema como una lista larga.

En esta leccion, echaremos un vistazo a un problema simple y resolverlo de algunas formas. Queremos crear un programa que lee en una lista arbitraria de numeros ingresados por el usuario  y entonces adicionamos todo y adicionamos por ultimo retornamos el resultado al usuario. Aprenderemos como usar I/O tradicional y como usar evaluacion perezosa y una forma mas facil de razonar sobre la solucion.

## 22.1 Interactuando con el comando de linea la forma no perezosa.
