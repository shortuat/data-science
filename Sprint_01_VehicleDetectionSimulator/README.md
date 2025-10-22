# Sprint 1 - Simulador básico de flujo vehicular

## Objetivo
Desarrollar un script en Python que simule el comportamiento básico de un cruce vial inteligente, donde los semáforos cambian su estado según la cantidad de vehículos detectados en cada dirección.

## Descripción funcional
El programa debe simular el comportamiento de una intersección (Norte - Sur y Oriente - Occidente), donde los semáforos cambian su estado en cada ciclo de simulación en base a la **mayor cantidad de vehículos** y al **límite máximo de tiempo de espera** de cada semáforo. Luego de cada ciclo, el sistema actualiza el flujo de vehículos, generando un archivo csv con el ciclo de simulación, el nombre de la vías, el número de vehículos en cada una de las vía, los estados de los semáforos y los tiempos de espera.

## Entradas esperadas
Define los parámetros que el simulador necesitará, por ejemplo:
- Nombre de vías.
- Número inicial aleatorio de vehículos por vía.
- Número de ciclos de simulación.
- Número de ciclos máximos de espera para el estado rojo y verde del semáforo.

## Salidas esperadas
Indica los resultados que el programa debe generar:
- Ciclo de simulación.
- Nombre de la vía.
- Número de vehículos.
- Estado de cada vía (verde, rojo).
- Tiempo de espera de vía.
- Registro (log) de los ciclos.

## Reglas de funcionamiento
Las reglas concretas que guiarán la simulación son:
- La vía con mayor flujo obtiene el verde en el siguiente ciclo.
- Cada ciclo libera un número fijo de vehículos por vía.

## Ejemplo de salida esperada

=== Simulación de Intersección Inteligente ===
Ciclos simulados: 5

--- Ciclo 1 ---
Vía: Norte - Sur | Vehículos: 12 | Estado: verde | Espera: 0
Vía: Sur - Norte | Vehículos: 9 | Estado: rojo | Espera: 0

--- Ciclo 2 ---
Vía: Norte - Sur | Vehículos: 9 | Estado: rojo | Espera: 1
Vía: Sur - Norte | Vehículos: 11 | Estado: verde | Espera: 0

--- Ciclo 3 ---
Vía: Norte - Sur | Vehículos: 15 | Estado: verde | Espera: 0
Vía: Sur - Norte | Vehículos: 8 | Estado: rojo | Espera: 1

=== Resumen ===
Vehículos totales procesados: 23
Duración total de simulación: 5 ciclos

---------------------------------------------

## Estructura de archivos

sprint_1/
│
├── data/
│   ├── raw/                    # Datos de entrada originales (sin procesar)
│   │   └── entradas.csv
│   ├── processed/              # Datos generados o transformados
│   │   └── resultados.csv
│
├── notebooks/                  # Exploración y análisis interactivo (Jupyter)
│   ├── 01_exploracion_inicial.ipynb
│   ├── 02_visualizacion_resultados.ipynb
│
├── reports/                    # Resultados finales del sprint
│   ├── figures/                # Gráficos exportados
│   └── informe_sprint1.md      # Resumen del Sprint o documentación técnica
│
├── scripts/                    # Scripts auxiliares (automatizaciones, limpieza, etc.)
│   ├── generar_datos_iniciales.py
│   ├── graficar_resultados.py
│
├── src/                        # Código fuente del simulador (núcleo lógico)
│   ├── __init__.py
│   ├── modelos.py
│   ├── controlador.py
│   ├── io_csv.py
│   └── simulador.py
│
├── tests/                      # Pruebas unitarias y validación de módulos
│   ├── test_simulador.py
│
├── main.py                     # Punto de entrada principal
│
├── requirements.txt            # Dependencias del entorno (numpy, pandas, etc.)
│
└── README.md                   # Descripción general del proyecto

👤 **Autor:** Santiago Hortua  
🌍 **Enfoque:** Ciencia de Datos aplicada a movilidad y sostenibilidad energética.
