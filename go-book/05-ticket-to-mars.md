05-ticket-to-mars.md
Bienvenido al primer desafio. Es tiempo de tomar todo lo cubierto en la unidad 1  y escribir un programa tu mismo. Tu desafio es escribir un generador de tickets en el play ground de Go este hara uso de variables constantes, constantes, switch, if, y for. ESte debe tambien dibujar con los paquetes fmt y math/rand  par mostrar  texto alineado y generador de numeros aleatorios.

Cuando planificamos  un viaje a marte, este debe ser manejado con un ticket de las multiples lineas en un lugar. Existen websites que agregan precios de tickets para aerolineas, pero no existe hasta ahora para lineas espacielas.

Este no es un problema para ti, aunque. Puedes usar Go para ensenar a tu computadora a resolver problemas como este.

Para comenzar a construir un prototipo que genera 10 tickes aleatorios y los muestre en un formato tabular con un bonito encabezado como sigue.

```go
Spaceline                  Days  Trip  type Price
=================================================
Virgin Galactic              23  Round-trip $ 96
Virgin Galactic              39  One-way    $ 37
SpaceX                       31  One-way    $ 41
Space Adventures             22 Round-trip  $ 100
Space Adventures             22 One-way     $ 50
Virgin Galactic              30 Round-trip  $ 84
Virgin Galactic              24 Round-trip  $ 94
Space Adventures             27 One-way     $ 44
Space Adventures             28 Round-trip  $ 86
SpaceX                       41 Round-trip  $ 72
```
La tabla deberia tener 4 columnas:
- El spaceline de la compania que provee el servicio.
- La duracion en dias  para el viaje a marte (un-forma).
- Si el precio cubre el viaje de retorno.
- El precio en millones de dolares.

Para cada ticket, se selecciona aleatoriamente uno de las siguientes spacelines: Space Adventures, SpaceX, o Virgin Galactic.

Usa October 13, 2020 como la fecha de inicio de todos los tickets. Marte esta a 62,100,000 km de distancia a la vez

Escoge aleatoriamente la velocidad de la nave entre 16 a 30 km/s. Esto determinara la duracion del viaje a marte y tambien el precio del ticket. Haz que los viajes mas rapidos sean mas caros, en el rango de precios desde $36 millones a $50 millones. Dobla el precio para viajes redondos.

