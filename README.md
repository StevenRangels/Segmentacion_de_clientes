# Segmentación de clientes.

En este repositorio identificamos la probabilidad de que un cliente sea clasificado como “PREFERENCIAL” en Colombia.

## EL problema planteado es el siguiente:

Eres un ingeniero/a de un banco con presencia en varios países. Tu tarea es implementar en Python un sistema de segmentación de clientes. Debes identificar la probabilidad de que un cliente sea clasificado como “PREFERENCIAL” en Colombia. 

1. Variables de entrada: 
- Cantidad de dinero ahorrado en el banco. 
- El salario que gana el cliente. 

2. Variable de salida: 
- Probabilidad de ser un cliente preferencial.

### Diseñe un controlador difuso que cumpla los siguientes ejemplos:

1. Adriana debe tener una probabilidad de al menos 90% de ser preferencial, tiene $500 Millones ahorrados y un salario de $15 Millones al mes. 
2. Nelson debe tener una probabilidad alrededor de 60% de ser preferencial, tiene $30 millones ahorrados y un salario de $9 millones al mes. 
3. Federico no debe sobrepasar una probabilidad de 20% de ser preferencial, tiene $40 millones ahorrados y un salario de $1.160.000 al mes. 
4. Verónica debe estar alrededor de un 5% de ser preferencial, no tiene dinero ahorrado en el banco y su salario es de $1.500.000 al mes.

# Sistema de Segmentación de Clientes con Lógica Difusa.

Este sistema de segmentación de clientes en Python utiliza lógica difusa para determinar la probabilidad de que un cliente sea clasificado como "PREFERENCIAL" en Colombia.

## Descripción de contenido.  

1. El código fuente se encuentra en la carpeta "notebooks".

2. las imágenes dadas en simulación se encuentran en la carpeta"Images".

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
