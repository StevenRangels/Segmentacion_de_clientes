# Segmentación de clientes.

En este repositorio identificamos la probabilidad de que un cliente sea clasificado como “PREFERENCIAL” en Colombia.

# Sistema de Segmentación de Clientes con Lógica Difusa.

Este sistema de segmentación de clientes en Python utiliza lógica difusa para determinar la probabilidad de que un cliente sea clasificado como "PREFERENCIAL" en Colombia.

## Descripción de contenido.  

1. El código fuente se encuentra en la carpeta "notebooks".

2. las imágenes dadas en simulación se encuentran en la carpeta"Imágenes".

## Descripción.

El sistema de segmentación de clientes utiliza lógica difusa para tomar decisiones basadas en dos variables de entrada: ahorro y salario. En función de estas variables, el sistema asigna una probabilidad de ser un cliente preferencial.

## Requisitos.

Asegúrate de tener Python y las bibliotecas necesarias instaladas. Puedes instalar las bibliotecas requeridas ejecutando en la terminal el siguiente comando: 

pip install numpy scikit-fuzzy matplotlib

Se recomienda simular el código en Visual Studio Code.

## Detalles del Código.

El código se divide en tres partes principales:

1. Definición de las Variables de Entrada y Salida.

Ahorro y salario son las variables de entrada que representan el ahorro y el salario del cliente y preferencial es la variable de salida que representa la probabilidad de ser un cliente preferencial.

2. Funciones de Membresía.

Las funciones de membresía definen cómo se relacionan las entradas y la salida, estas están diseñadas en ciertos niveles como "muy_bajo," "bajo," "medio," "medio_alto" y "alto" para proporcionar mayor precisión en la segmentación.

3. Reglas Difusas.

El sistema utiliza reglas difusas para tomar decisiones basadas en las variables de entrada. Las reglas se definen para diferentes combinaciones de niveles de ahorro y salario.

## Ejemplos de Casos.

El código incluye ejemplos de casos en el mismo script. Puedes modificar los valores de ahorro y salario en el código para probar diferentes casos.