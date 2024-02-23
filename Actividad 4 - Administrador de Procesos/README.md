# ADMINISTRADOR DE PROCESOS

## La administración de procesos
Este es un tema que nos lleva a analizar que clase de sistemas son los que 
utilizan estas terminologías, y nos remontamos a pensar en los sistemas distribuidos.
<br>

Según Andrew S. Tanenbaum, que es el autor en el que nos estamos basando para realizar la
presente actividad, dentro de un sistema distribuido, cuando hablamos de administración de
procesos, sabemos que debe existir un mecanismo de comunicación global entre los procesos,
de forma que cualquier proceso pueda comunicarse con cualquier otro.
<br>

La administración de procesos también debe ser la misma en todas partes. La forma en que se
crean destruye, inician y detienen los procesos, no debe variar de una máquina a otra.
<br>

En cuanto a los sistemas multiprocesador con tiempo compartido, tenemos que su característica
principal cuando nos referimos a la administración de procesos es que tiene una cola de
ejecución: una lista de todos los procesos en el sistema que no están bloqueados en forma
lógica y listos para su ejecución. La cola de ejecución es una estructura de datos contenida en
la memoria compartida.

![image](https://github.com/diegogovea/SSP-Sistemas-Operativos-DLGO/assets/87109033/a460e2af-f6cb-43de-9e57-05474485199f)

## Estados de un proceso

Los procesos pueden pasar por varios estados durante su ciclo de vida, como listo, en ejecución,
bloqueado y terminado. La comprensión de estos estados es crucial para la gestión eficiente de
los recursos del sistema.
<br>

Según Tanenbaum, menciona que los estados de procesos son los siguiente:
<br>

- En ejecución: En este estado, el proceso se encuentra activamente utilizando la capacidad de la CPU para llevar a cabo sus operaciones.
- Listo: El proceso está preparado para ejecutarse, pero momentáneamente cede la CPU a otro proceso, siguiendo la decisión del planificador de procesos. Este estado se produce cuando se determina que es el momento de que otro proceso utilice la CPU.
- Bloqueado: En este caso, el proceso no puede ejecutarse debido a la espera de la ocurrencia de un evento externo, como la llegada de datos de entrada específicos. El proceso permanece bloqueado hasta que se materializa el evento esperado.
- Desbloqueado: Aunque no constituye un estado separado, esta etapa se manifiesta cuando un proceso bloqueado se libera tras la ocurrencia del evento externo esperado. Una vez desbloqueado, el proceso puede trasladarse al estado listo, aguardando su oportunidad para ejecutarse.

## Llamadas al sistema para la administración de procesos
