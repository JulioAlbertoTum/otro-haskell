# Comentarios

El uso de comentarios permite compensar la incapacidad  para expresarnos en el codigo. Los comentarios son siempre fallos. Se usan porque no sabemos como expresarlos son ellos perro su uso no es motivo de celebracion.

Los programadores deben ser lo bastante disciplinados como para mantener los comentarios actualizados, relevantes y precisos. Sin embargo es mejor arreglar el codigo para no necesitar comentario alguno.

El codigo es la unica fuente de informacion precisa 

## Los comentarios no compensan el codigo incorrecto

El codigo claro y expresivo sin comentarios es muy superior al codigo 
enrevesado y complejo con multitud de comentarios. Asi que es mejor solucionar los problemas del codigo.

## Explicarse en el codigo

El codigo es el mejor (o deberia serlo) vehiculo de expresion. En muchos casos basta con una funcion que diga lo mismo que el comentario que pensaba escribir.

## Comentarios de calidad

Algunos comentarios son necesarios y beneficiosos.Sin embargo recuerde que el mejor comentario es el que no se tiene que escribir.

### Comentarios legales

Algunos estandares obligan a poner comentarios por motivos legales. Ej Derechos de autor.
Evite los comentarios contratos o tomos legales. Es mejor hacer referencias a una licencia estandar u otro documento.

### Comentarios informativos

Brindan informacion basica, pero es mejor usar el nombre de una funcion para transmitir la informacion siempre que sea posible. 

### Explicar la intencion

A veces un comentario proporciona la intencion de una decision. 

### Clarificacion

Por lo general, conviene buscar la forma de que el argumento o el valor devuelto sean claros por si mismos, pero cuando forma parte de una biblioteca estandar o de codigo que no se puede alterar, un comentario aclarativo puede ser util.

Sin embargo se corre el riesgo que el comentario aclarativo sea incorrecto.

### Advertir de las consecuencias

En ocasiones es necesario advertir a otros programadores de determinadas consecuencias.

Comandos como @Ignore de java nos facilitan este trabajo.

### Comentarios TODO 

Son notas en forma de comentarios. ES decir son tareas que el programador piensa de deberia haber hecho pero que no es asi. No abuse de estas notas y trate de eliminarlas si es posible

### Amplificacion

Se trata de amplificar la importancia de algo que pareceria irrelevante.

### Javadoc en API publicas

En API's publicas debe crear javadoc de calidadd, sin embargo estos pueden llegar a ser tan ambiguos, amplios y descorteses  como cualquier otro tipo de documentos.

## Comentarios incorrectos

Suelen ser excusas de codigos pobres o justificaciones de decisiones insuficientes.

### Balbucear

Aniadir un comentario sin razon o porque el proceso lo requiere es un error.

### Comentarios redundantes

Es el tipo de comentario que no es mas informativo que el codigo. Son el tipo de comentarios que ensucian y oscurecen el codigo.

### Comentarios confusos

Es del tipo que hace una afirmacion que no es del todo precisa. 

### Comentarios obligatorios

No todas las funciones deben tener un javadoc o que todas las variablels deben tener un comentario. Estos encusian el codigo y generan confusion y desorganizacion.

### Comentarios periodicos

En ocasiones se aniade un comentario al inicio de un modulo cada vez que se edita. Estos acumulan una especie de registro de todos los cambios realizados.

En la actualidad los sistemas de control de versiones han reemplazado a estos.

### Comentario sobrantes

Sono del tipo que sobran. Restan importancia a lo evidente y no ofrecen informacion nueva.

Dese a la tarea de limpiar el codigo.

### Comentarios sobrantes espeluznantes.

Otro problemas creado por los javadoc.

### No usar comentarios si se puede usar una funcion o una variable

-- 

### Marcadores de posicion

son del tipo 

////// Acciones /////////////////////////

Esta hilera resulta molesta, uselas cuando sea estrictamente necesarias, siempre que el beneficio sea significativo.

### Comentarios de llave de cierre

Suele tener sentido en funciones extensas con estructuras anidadas, sin embargo es mejor usar funciones pequenas y asi evitar estos comentarios.

### Asignaciones y menciones
```
/*  Aniadido por Rick */
```
Los sistemas de control de versiones tambien solucionan este problema, por lo que no es necesario plagar le codigo con pequenas menciones.

### Codigo comentado 

Evite el codigo comentado. !No lo haga!

Por lo general los programadores evitan borrarlo, y se va acumulando.

### Comentarios HTML

El html en comentarios es una aberracion. Dificulta la lectura de los comentarios.

### Informacion no local

Un comentario debe tener informacion del codigo que lo rodea. Evite poner informacion bgloblar dle sistema en  el contexto de un comentario local.

### Demasiada informacion 

No incluya en sus comentarios descripciones extensas y detalladas.

### Conexiones no Evidentes

La conexion entre un comentario y el codigo que describe debe ser evidente. 

### Encabezados de funcion

las funciones breves apenas requieren explicacion. Un nombre bien elegido nos ahorra el problema.

### Javadocs en codigo no publico

javadocs no es util para codigo no dirigido a consumo publico.






















































































































































