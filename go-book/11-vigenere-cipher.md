El cifrado viginere  es una variante del cifrado cesar del siglo 16. Para este reto  escribiras un programa que decifre un texto usando una clave.

Antes de describir el cifrado vigenere, permitenos reformular el cifrado cesar, con el que ya hemos trabajado. Con el cifrado Cesar, un mensaje en texto plano es cifrado para cambiar cada letra  por tres. La direccion es inversa para decifrar el mensaje resultante.

Asignar cada Letra del ingles un valor numerico, donde A=0, B=1, hasta llegar a al Z=25. Con esto en mente, un cambio por 3 puede ser representado por la letra D (D = 3).

Para descifrar el texto en la tabla 11.1, comenzando con la letra L y cambiando esta por D. Porque L=11 y D=3, el resultado de 11-3 es 8, o la letra I. Si tienes la necesidad de decifrar la letra A, no deberias perder X, como se vio en la leccion 9.

El cifrado cesar y ROT13  son susceptibles a algo llamado analisis de frecuencia. letras que ocurren frecuentemente en el lenguaje ingles, tal como E, que ocurrira frecuentemente en el cifrado de texto tambien. Aplicando patrones en el texto cifrado, el codigo puede ser crackeado.

Para frustrar a los crackers de codigo, El cifrado vignere cambia cada letra basada en la repeticion de una palabra clave, en lugar de un valor constante como 3 a 13. La palabra clave hasta el fin del mensaje, como se muestra para la palabra clave GOLANG en la tabla.

Ahora que conoces el cifrado Vigenere es, como notaras Viginere con la clave D es equivalente al cifrado Cesar. Al igual, ROT13 tiene un clave de N (N = 13). Claves largas son necesarias para conseguir cualquier beneficio.

Escribe un programa para decifrar el texto cifrado mostrado en la tabla. Para mantener esto simple, todos los caracteres son letras en ingles mayusculas para ambos el texto y la clave:
```go
cipherText := "CSOITEUIWUIZNSROCNKFD"
keyword := "GOLANG"
```
- La funcion *strings.Repeat*  puede llegar a ser muy practica. Intenta, pero esto tambien completa el ejercicio  sin importar ningun otro paquete que no sea fmt para imprimir el mensaje decifrado.
- Intenta este ejercicio usando *range* en un bucle y sin este. recuerda que range de la palabra clave divide un string en runes, mientras que un index como keyword[0] tiene resultados en un byte.

*TIP* Puedes realizar solo operaciones sobre valores sobre valores del mismo tipo, pero puedes  convertir un tipo en otro [string, byte, rune].

- Para envolver alrededor de los limites del alfabeto, El ejercicio del cifrado cesar usa una comparacion. Resuelve este ejercicio sin  usar la sentencia *if* usando modulos (%).

*TIP* Llamamos modulos al resto de dividir dos numeros. Por ejemplo 27 % 26 es 1 , guardando los numeros en un rango de 0-25. Se cuidadoso con los numeros negativos, aunque -3 % 26 es todavia -3.

Despues de completar el ejercicio, echa un vistazo a la solucion en el apendice. Como hago la comparacion? usa el boton Share del Playground Go y postea el link a tu solucion en el foro del libro.

Texto cifrado no tiene otra dificultad que decifrar el texto. Solo adiciona letras de la palabra clave a las letras de un texto plano en lugar de sustraerlo.

Para enviar mensajes cifrados, escribe un programa que cifre el texto plano usando una clave:
```go
plainText := "your message goes here"
keyword := "GOLANG
``` 
Bonus: en lugar de escribir tu mensaje en texto plano en mayusculas sin espacios, usan las funciones *strings.Replace* y *strings.ToUpper* para remover espacios y  poner cadenas en mayuscula antes de tu cifrado.

Una vez que cifras un mensaje en texto plano, verifica tu trabajo decifrando el texto cifrado con la misma clave.

Usa la clave *GOLANG* para cifrar un mensaje y postea este en los foros de Get Programming with Go.

*NOTA* El cifrado Vigenere es bueno y divertido, pero no se usa en secretos importantes. Hay formas mas seguras de enviar mensajes en el siglo 21.


