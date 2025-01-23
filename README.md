# Práctica 1:  Aprendiendo las bases de ROS

ROS es una colección de software de código abierto destinados al desarrollo de robots, que ofrece características parecidas a las de un sistema operativo en un conjunto de ordenadores diverso. La meta principal de ROS es respaldar el reaprovechamiento de código en la investigación y el desarrollo de robótica como un instrumento autónomo del lenguaje y la plataforma. Actualmente, ROS solo se puede ejecutar en plataformas que utilizan Unix. En este ejercicio de laboratorio, abordaremos algunas nociones fundamentales de ROS e interactuaremos con un sistema ROS en operación.

## Instalación
Para la realización de esta práctica y las sucesivas, se han generado varios `Dockerfile` que serán los encargados de generar las imágenes de ROS para poder trabajar con ellas. Esto nos va a permitir generar contenedores de `Docker` con dichas imágenes, de forma que, podamos tener todas las dependencias y librerias contenezidas dentro de nuestro sistema operativo (Ubuntu 24.04 LTS), evitando así incompatibilidades con otras aplicaciones. 

Para poder trabajar con los contenedores de `Docker` y ROS es necesario antes de comenzar, es necesario realizar los pasos que se encuentran en el documento [Instalacion.md](Instalacion.md) dentro de este repositorio. Este documento contiene la guía de instalación con las heramientas necesarias para poder ejecutar las prácticas de la asignatura.

Para comenzar con la instalación de ROS dentro de un contenedor `Docker` se requiere de abrir una terminal dentro de la carpeta que contenga esta práctica y ejecutar los siguientes comandos:

1. Crear y construir la imágen de ROS Noetic a través del `Dockerfile`:
```bash
docker build -t ros_noetic:latest.
```
Este comando comenzará la instalación de ROS en su Distro Noetic

2. Una vez instalado ROS ya podemos ejecutar el contenedor y conectarnos a él de la siguiente manera:
```bash
sudo chmod u+x run.sh # Solo la primera vez para dar los permisos necesarios
./run.sh 
```
Ya estaremos dentro del contenedor y podremos empezar a trabajar con ROS.

3. Para conectarnos al contenedor desde nuevas terminales, ejecutar:
```bash
sudo chmod u+x connect_ros.sh # Solo la primera vez para dar los permisos necesarios
./connect_ros.sh
```

## Parte 1: Primeros Pasos con ROS

### Creación del espacio de Trabajo en ROS
Cuando se trabaja con el código fuente de ROS, a menudo es útil hacerlo en un `workspace` (Espacio de trabajo). Para crear un espacio de trabajo ROS lo único que tenemos que hacer es navegar hasta el directorio en el que queramos crear el espacio de trabajo y ejecutar los comando que aparecen a
continuación. Se recomienda crearlo en la carpeta raíz de nuestro espacio de trabajo en el contenedor de `Docker` y con el nombre `catkin_ws`.
```bash
mkdir -p catkin_ws/src
cd catkin_ws/
catkin_make
```
El comando [catkin_make](https://wiki.ros.org/catkin/commands/catkin_make) es una herramienta práctica para trabajar con [espacios de trabajo catkin](https://wiki.ros.org/catkin/workspaces). Ejecutándolo la primera vez en su espacio de trabajo, creará un enlace *CMakeLists.txt* en su carpeta `src`.

Además, si miras en tu directorio actual ahora deberías tener una carpeta 'build' y 'devel'. Dentro de la carpeta 'devel' puedes ver que ahora hay varios archivos setup.*sh. Cualquiera de estos archivos se superpondrá a este espacio de trabajo en la parte superior de su entorno. Para más información consulte la documentación general de catkin: catkin. Antes de continuar genere su nuevo archivo setup.*sh:

```bash
source devel/setup.bash
```

Para asegurarse de que su espacio de trabajo es superpuesto correctamente por el script de instalación, asegúrese de que la variable de entorno ROS_PACKAGE_PATH incluye el directorio en el que se encuentra.

```bash
echo $ROS_PACKAGE_PATH
```
La salida deberia ser la siguiente:
```
/workspace/catkin_ws/src:/opt/ros/noetic/share
```



### Ejemplo de un entorno de ROS
En esta primera parte nos vamos a servir de los tutoriales básicos que trae la instalación de ROS para entender su funcionamiento básico de `nodos` y `topics`. 
Para ello, vamos a seguir las siguientes instrucciones dentro del contenedor de `Docker` generado anteriormente:
- Terminal 1:
```bash
roscore #Lanzar el nodo master que gestiona la comunicación de ROS
```

- Terminal 2:
En esta terminal lanza el nodo `/talker`. Observa el mensaje que está publicando dicho nodo. A continuación, observa la  lista de nodos que existen en el entorno y estudia el entorno de ROS creado.
```bash
rosrun rospy_tutorials talker
```

Revisa la siguiente documentación ([ROS Nodes](https://wiki.ros.org/ROS/Tutorials/UnderstandingNodes), [ROS Topics](https://wiki.ros.org/ROS/Tutorials/UnderstandingTopics)) y responde a las siguientes preguntas:
> Pregunta 1: ¿Qué podemos saber de este nodo? (Suscriptores, topics)
>
> Pregunta 2: ¿Qué podemos saber sobre el topic que publica el nodo que acabamos de lanzar?

- Terminal 3:
El siguiente paso es crear un suscriptor al topic que está publicando en nodo `/talker` (`/chatter`). Para ello lanzaremos otro nodo, el nodo `/listener`.
```bash
rosrun rospy_tutorials listener
```
> Pregunta 3: ¿Qué podemos saber sobre este nuevo nodo?
>
> Pregunta 4: ¿Qué ha sucedido ahora en el topic /chatter?

Dentro de ROS existen multitud de herramientas ya  implementadas para ayudarnos a conocer mejor el entorno en el que se está trabajando. Entre ellas se encuentra la herramienta [rqt](http://wiki.ros.org/rqt). Dentro de `rqt` tenemos una herramienta que nos permite ver la interconexión entre los diferentes nodos, `rqt_graph`, que para lanzarla solo tenemos que escribir en una nueva Terminal lo siguiente:

- Terminal 4: 
```bash
rqt_graph
```
Esto nos muestra un gráfico donde aparecen los nodos y los topics que están actualmente en el
entorno de ROS

> Pregunta 5: ¿Qué podemos saber a partir de este gráfico?

### Creando un Servicio en ROS
A continuación, se va a crear un servicio que nos va a sumar dos enteros. Para ello copia la carpeta `servicio_suma` en `~/catkin_ws/src`. A continuación, ejecuta catkin_make desde la terminal, dentro de la carpeta `~/catkin_ws`. De esta forma ya habremos creado el servicio que nos va a permitir sumar dos enteros. Ahora lanza el `rosmaster` y ejecuta los siguientes comandos en otra Terminal:
```bash
rossrv list
rossrv show servicio_suma/AddTwoInts
rosrun servicio_suma add_two_ints_server.py
rosrun servicio_suma add_two_ints_client.py 3 7
```

> Pregunta 6: ¿Qué puedes comentar acerca de este servicio?

### Ejercicios
1. Publica desde la terminal un mensaje, con la cadena de caracteres que desees, al topic `/chatter` y para que este sea leído por el nodo `/listener`. Escribe los comandos que has tenido que ejecutar para que esto suceda. Ten en cuenta que el nodo ROS master no está lanzado todavía.

2. Cambia el servicio `servicio_suma` para que haga la suma de tres enteros. Describe que has tenido que hacer y los archivos que has tenido que modificar.