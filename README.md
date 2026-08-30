# ProyectoFP
Repositorio de la clase Fundamentos de programación semestre agosto - diciembre 2026

# Sistema de Control de Inventario y Punto de Venta para Pequeños Negocios

## Contexto
En América Latina, las micro y pequeñas empresas (tiendas de abarrotes, cafeterías locales, papelerías) representan una parte fundamental de la economía local. Sin embargo, un gran porcentaje de estos establecimientos aún gestiona su inventario y registro de ventas de manera manual.

Los sistemas de Punto de Venta (POS) comerciales existentes en el mercado suelen ser costosos, requieren suscripciones mensuales o necesitan infraestructura especializada. Esto deja fuera a pequeños comercios y emprendedores que buscan digitalizarse sin realizar grandes inversiones iniciales.

## Problemática que atiende
La falta de un sistema accesible de control de ventas e inventario genera las siguientes dificultades en los negocios:
1. **Descontrol en el stock:** Pérdida de productos o desabasto por no detectar a tiempo cuándo se agota un artículo.
2. **Errores en el cobro:** Fallos en el cálculo manual del total o del cambio entregado al cliente.
3. **Falta de historial:** Imposibilidad de consultar ventas pasadas o saber qué productos generan más ingresos.

Este programa ofrece una solución automatizada, ligera y de bajo costo que corre en la terminal de Python. Permite registrar ventas, actualizar el inventario automáticamente y guardar un registro permanente de transacciones en archivos de texto, garantizando la persistencia de los datos.
Yo en lo especial decido agarrar esta idea como proyecto porque yo he trabajado en restaurantes y lugares que les faltan este tipo de avances tecnológicos y el recuento de inventario puede llegar a ser cansado y molesto, sin contar que puede llegar a tener errores humanos de conteo llegando a pérdidas de dinero o hasta el cierre del mismo establecimiento, con este código busco encontrar una alternativa accesible que automatice esas tareas repetitivas y optimice el tiempo de los trabajadores evitando renuncias y mejorando la calidad laboral.

## Algoritmo y Pseudocódigo

```text
Inicio del Programa

1. Cargar el inventario desde el archivo "inventario.txt"
   - Si no existe, inicializar con una lista predefinida de productos y cantidades.

2. Repetir (Ciclo Principal del Menú):
   Mostrar Menú:
     1. Ver Inventario Disponible
     2. Realizar una Venta (Punto de Venta)
     3. Agregar / Modificar Producto en Inventario
     4. Consultar Historial de Ventas (Leer Archivo)
     5. Salir

   Leer opcion

   Según opcion:
     Opción 1:
       Desplegar la lista/matriz de productos [ID, Nombre, Precio, Stock]

     Opción 2:
       Crear lista vacía "carrito"
       Repetir:
         Pedir ID del producto y Cantidad deseada
         Si el producto existe Y Cantidad <= Stock:
           Agregar producto a "carrito"
           Restar Cantidad del Stock disponible
         Sino:
           Mostrar mensaje de error (Stock insuficiente o ID no válido)
         Preguntar si desea agregar otro producto
       Hasta que el usuario decida no agregar más

       Si "carrito" tiene productos:
         Calcular Subtotal, IVA (16%) y Total
         Mostrar ticket en pantalla
         Solicitar Pago y calcular Cambio
         Guardar el ticket generado en "ventas.txt" (Modo Append)

     Opción 3:
       Solicitar ID, Nombre, Precio y Stock
       Si el producto ya existe:
         Sumar el nuevo stock al existente
       Sino:
         Agregar el nuevo producto a la lista de inventario

     Opción 4:
       Abrir y leer el archivo "ventas.txt"
       Mostrar todo el historial de ventas registradas en la terminal

     Opción 5:
       Guardar el estado actual del inventario en "inventario.txt"
       Mostrar mensaje de salida
       Terminar programa

Fin del Programa
