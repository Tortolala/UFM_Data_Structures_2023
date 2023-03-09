# Parcial #1 - Estructuras de Datos

Fecha: Marzo 02, 2023  
Duración: 1h 20m

## Instrucciones

Utilizando como base las clases *Linked List* y *Stack* que se encuentran en el Gist, realizar las siguientes modificaciones:

1) **Reverse Inplace:** este método debe incluirse en la clase Linked List, su funcionalidad consiste en invertir el orden de la lista simplemente ligada a través de modificaciones en los punteros. Este método no requiere ningún retorno específico, ya que modifica la instancia original de la lista.

Para implementarlo, debe basarse en el siguiente pseudocódigo: 

> REVERSE_IN_PLACE():
>
>
> IF START == NIL:  
> &nbsp;&nbsp;&nbsp;&nbsp;EMPTY LIST  
> 
> SET CURRENT_NODE = START  
> SET PREV_NODE = NIL  
> SET NEXT_NODE = NIL  
> 
> WHILE CURRENT_NODE != NIL:  
>&nbsp;&nbsp;&nbsp;&nbsp;SET NEXT_NODE = CURRENT_NODE.NEXT  
>&nbsp;&nbsp;&nbsp;&nbsp;SET CURRENT_NODE.NEXT = PREV_NODE  
>&nbsp;&nbsp;&nbsp;&nbsp;SET PREV_NODE = CURRENT_NODE  
>&nbsp;&nbsp;&nbsp;&nbsp;SET CURRENT_NODE = NEXT_NODE 
>  
>SET START = PREV_NODE

2) **Reverse with Stack:** esta función debe realizarse fuera de la clase Linked List. Su funcionalidad consiste en apoyarse de una instancia de la clase Stack para invertir el orden de la lista simplemente ligada. Esta función debe retornar una nueva lista, independiente a la lista ligada original, con el orden de sus elementos invertido.


## Testing

Para evaluar el funcionamiento de su código, deberá realizar lo siguiente en el archivo `test.py`:

1) Crear una instancia de Linked List y agregar 10 elementos en ella.
2) Imprimir la lista original.
2) Utilizar la función **Reverse with Stack** para crear una nueva lista invertida a partir de la lista original.
3) Utilizar el método **Reverse Inplace** para invertir la lista original.
4) Imprimir ambas listas resultantes para evaluar que sean iguales.
