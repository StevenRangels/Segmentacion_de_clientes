import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Variables de entrada.
ahorro = ctrl.Antecedent(np.arange(0, 500000001, 100000), 'ahorro')
salario = ctrl.Antecedent(np.arange(0, 15000001, 10000), 'salario')

# Variable de salida.
preferencial = ctrl.Consequent(np.arange(0, 101, 1), 'preferencial')

# Funciones de membresía.
ahorro['muy_bajo'] = fuzz.trimf(ahorro.universe, [0, 0, 10000000])
ahorro['bajo'] = fuzz.trimf(ahorro.universe, [8000000, 20000000, 33000000])
ahorro['medio'] = fuzz.trimf(ahorro.universe, [31000000, 115000000, 200000000])
ahorro['medio_alto'] = fuzz.trimf(ahorro.universe, [180000000, 280000000, 380000000])
ahorro['alto'] = fuzz.trimf(ahorro.universe, [350000000, 500000000, 500000000])

salario['muy_bajo'] = fuzz.trimf(salario.universe, [0, 0, 1200000])
salario['bajo'] = fuzz.trimf(salario.universe, [1000000, 2250000, 3500000])
salario['medio'] = fuzz.trimf(salario.universe, [3200000, 5100000, 7500000])
salario['medio_alto'] = fuzz.trimf(salario.universe, [7000000, 8500000 , 10000000])
salario['alto'] = fuzz.trimf(salario.universe, [8700000, 15000000, 15000000])

preferencial['muy_bajo'] = fuzz.trimf(preferencial.universe, [0, 0, 13])
preferencial['bajo'] = fuzz.trimf(preferencial.universe, [9, 19, 30])
preferencial['medio'] = fuzz.trimf(preferencial.universe, [25, 40, 55])
preferencial['medio_alto'] = fuzz.trimf(preferencial.universe, [38, 58, 75])
preferencial['alto'] = fuzz.trimf(preferencial.universe, [72, 100, 100])

# Reglas difusas.
regla1 = ctrl.Rule(ahorro['muy_bajo'] & salario['muy_bajo'], preferencial['muy_bajo'])
regla2 = ctrl.Rule(ahorro['muy_bajo'] & salario['bajo'], preferencial['muy_bajo'])
regla3 = ctrl.Rule(ahorro['muy_bajo'] & salario['medio'], preferencial['bajo'])
regla4 = ctrl.Rule(ahorro['muy_bajo'] & salario['medio_alto'], preferencial['medio'])
regla5 = ctrl.Rule(ahorro['muy_bajo'] & salario['alto'], preferencial['medio_alto'])

regla6 = ctrl.Rule(ahorro['bajo'] & salario['muy_bajo'], preferencial['bajo'])
regla7 = ctrl.Rule(ahorro['bajo'] & salario['bajo'], preferencial['bajo'])
regla8 = ctrl.Rule(ahorro['bajo'] & salario['medio'], preferencial['medio'])
regla9 = ctrl.Rule(ahorro['bajo'] & salario['medio_alto'], preferencial['medio_alto'])
regla10 = ctrl.Rule(ahorro['bajo'] & salario['alto'], preferencial['alto'])

regla11 = ctrl.Rule(ahorro['medio'] & salario['muy_bajo'], preferencial['bajo'])
regla12 = ctrl.Rule(ahorro['medio'] & salario['bajo'], preferencial['bajo'])
regla13 = ctrl.Rule(ahorro['medio'] & salario['medio'], preferencial['medio'])
regla14 = ctrl.Rule(ahorro['medio'] & salario['medio_alto'], preferencial['medio_alto'])
regla15 = ctrl.Rule(ahorro['medio'] & salario['alto'], preferencial['alto'])

regla16 = ctrl.Rule(ahorro['medio_alto'] & salario['muy_bajo'], preferencial['medio_alto'])
regla17 = ctrl.Rule(ahorro['medio_alto'] & salario['bajo'], preferencial['medio_alto'])
regla18 = ctrl.Rule(ahorro['medio_alto'] & salario['medio'], preferencial['alto'])
regla19 = ctrl.Rule(ahorro['medio_alto'] & salario['medio_alto'], preferencial['alto'])
regla20 = ctrl.Rule(ahorro['medio_alto'] & salario['alto'], preferencial['alto'])

regla21 = ctrl.Rule(ahorro['alto'] & salario['muy_bajo'], preferencial['alto'])
regla22 = ctrl.Rule(ahorro['alto'] & salario['bajo'], preferencial['alto'])
regla23 = ctrl.Rule(ahorro['alto'] & salario['medio'], preferencial['alto'])
regla24 = ctrl.Rule(ahorro['alto'] & salario['medio_alto'], preferencial['alto'])
regla25 = ctrl.Rule(ahorro['alto'] & salario['alto'], preferencial['alto'])

# Sistema de control.
cliente_ctrl = ctrl.ControlSystem(
    [    
    regla1,
    regla2, 
    regla3, 
    regla4, 
    regla5, 
    regla6, 
    regla7, 
    regla8, 
    regla9, 
    regla10,
    regla11,
    regla12, 
    regla13,
    regla14, 
    regla15,
    regla16, 
    regla17, 
    regla18, 
    regla19,
    regla20, 
    regla21, 
    regla22, 
    regla23, 
    regla24, 
    regla25
    ]
    )

cliente = ctrl.ControlSystemSimulation(cliente_ctrl)

# Caso 1: Adriana.
cliente.input['ahorro'] = 500000000
cliente.input['salario'] = 15000000
cliente.compute()
print(f'Probabilidad de ser preferencial para Adriana: {cliente.output["preferencial"]:.2f}%')

# Caso 2: Nelson.
cliente.input['ahorro'] = 30000000
cliente.input['salario'] = 9000000
cliente.compute()
print(f'Probabilidad de ser preferencial para Nelson: {cliente.output["preferencial"]:.2f}%')

# Caso 3: Federico.
cliente.input['ahorro'] = 40000000
cliente.input['salario'] = 1160000
cliente.compute()
print(f'Probabilidad de ser preferencial para Federico: {cliente.output["preferencial"]:.2f}%')

# Caso 4: Verónica.
cliente.input['ahorro'] = 0
cliente.input['salario'] = 1500000
cliente.compute()
print(f'Probabilidad de ser preferencial para Verónica: {cliente.output["preferencial"]:.2f}%')

# Visualización de las funciones de membresía.
ahorro.view()
salario.view()
preferencial.view()
plt.show()