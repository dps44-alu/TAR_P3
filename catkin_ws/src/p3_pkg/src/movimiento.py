#!/usr/bin/env python3
import sys
import rospy
from geometry_msgs.msg import Twist
import math

rospy.set_param('/use_sim_time', True)
 #linea2 metros
def mov_0():
    rospy.init_node('movimiento', anonymous=True)
    pub = rospy.Publisher("/cmd_vel_mux/input/teleop", Twist, queue_size=10)

    rospy.sleep(2)

    vel_msg = Twist()
    vel_msg.linear.x = 0.2
    vel_msg.angular.z = 0.0  #no rotación

    distancia_objetivo = 2.0  #m
    tiempo_inicial = rospy.Time.now().to_sec()

    rate = rospy.Rate(10)  #10 Hz freq

    while not rospy.is_shutdown():
        tiempo_actual = rospy.Time.now().to_sec()
        distancia_recorrida = (tiempo_actual - tiempo_inicial) * vel_msg.linear.x
        pub.publish(vel_msg)
        if distancia_recorrida >= distancia_objetivo:
            break

       # pub.publish(vel_msg)
        rate.sleep()

    vel_msg.linear.x = 0.0
    pub.publish(vel_msg)
    rospy.loginfo("El TurtleBot ha recorrido 2 metros y se ha detenido.")


#triangulo eq 3 m
def mov_1():
    rospy.init_node('movimiento', anonymous=True)
    pub = rospy.Publisher("/cmd_vel_mux/input/teleop", Twist, queue_size=10)

    rospy.sleep(2)

    vel_msg = Twist()
    velocidad_lineal = 0.2  #vel lin
    velocidad_angular = 0.5  #vel ang
    rotacion_angulo = 120 * (3.14159265359 / 180)

    distancia_objetivo = 3.0
    rate=rospy.Rate(10)
    #triángulo equilátero
    for i in range(3):  # Realizamos 3 lados
        # Mover hacia adelante
        vel_msg.linear.x = velocidad_lineal
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)
        
        # Calcular el tiempo necesario para recorrer la distancia objetivo
        tiempo_de_movimiento = distancia_objetivo / velocidad_lineal
        
        # Avanzar durante el tiempo calculado para recorrer la distancia
        start_time = rospy.get_time()
        while rospy.get_time() - start_time < tiempo_de_movimiento:
            pub.publish(vel_msg)
            rate.sleep()  # Esperar el tiempo adecuado entre publicaciones
        
        # Detenerse
        vel_msg.linear.x = 0.0
        pub.publish(vel_msg)
        rospy.sleep(1)  # Pausa de 1 segundo antes de la rotación
  
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = velocidad_angular
        pub.publish(vel_msg)

        # Tiempo necesario para rotar 120 grados
        start_rotation = rospy.get_time()
        while rospy.get_time() - start_rotation < rotacion_angulo / velocidad_angular:
            pub.publish(vel_msg)  # Continuar rotando
            rate.sleep()  # Mantener la frecuencia

        # Detenerse después de la rotación
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)
        rospy.sleep(1)  # Pausa de 1 segundo antes de empezar el siguiente lado




    rospy.loginfo("El TurtleBot ha completado un triángulo equilátero de 3 metros de lado.")



def mov_2():
    rospy.init_node('movimiento', anonymous=True)
    pub = rospy.Publisher("/cmd_vel_mux/input/teleop", Twist, queue_size=10)

    rospy.sleep(2)

    vel_msg = Twist()
    velocidad_lineal = 0.2  #vel lin
    velocidad_angular = 1.0  #vel ang
    rotacion_angulo = 90 * (3.14159265359 / 180)  #rota90 en radianes

    distancia_objetivo = 1.0
    rate = rospy.Rate(10)
    for i in range(4):  #4lados posibles
        # delante
        vel_msg.linear.x = velocidad_lineal
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)
        tiempo_de_movimiento =  distancia_objetivo / velocidad_lineal
        start_time = rospy.get_time()
        while rospy.get_time() - start_time < tiempo_de_movimiento:
               pub.publish(vel_msg)
               rate.sleep()

        #rospy.sleep(distancia_objetivo / velocidad_lineal)
        # para
        vel_msg.linear.x = 0.0
        pub.publish(vel_msg)
        rospy.sleep(1)

        # rota90
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = velocidad_angular
        pub.publish(vel_msg)
       # rospy.sleep(rotacion_angulo / velocidad_angular)  # rota(t)

        # para
        tiempo_de_rotacion = rotacion_angulo / velocidad_angular
        start_rotation = rospy.get_time()
        while rospy.get_time() - start_rotation < tiempo_de_rotacion:
              pub.publish(vel_msg)
              rate.sleep()
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)
        rospy.sleep(1)

    rospy.loginfo("El TurtleBot ha completado un cuadrado de 1 metro de lado.")
#infinito
def mov_3():
    rospy.init_node('movimiento', anonymous=True)
    pub = rospy.Publisher("/cmd_vel_mux/input/teleop", Twist, queue_size=10)

    rospy.sleep(2)

    vel_msg = Twist()
    velocidad_lineal = 0.2  # Velocidad lineal en m/s
    velocidad_angular = 0.5  # Velocidad angular en radianes/s
    rotacion_angulo_120 = 120 * (3.14159265359 / 180)  # 120 grados en radianes

    distancia_recta = 0.5  # Distancia de 0.5 metros a recorrer
    distancia_diagonal = 0.71  # Distancia de 0.71 metros para los giros

    rate = rospy.Rate(10)  # Frecuencia de 10 Hz

    # Mover en forma de "infinito" (dos lazos para completar el "infinito")
    # 1er ciclo (recto -> gira derecha -> diagonal -> gira izquierda)
    for i in range(2):  # Dos lazos para formar el "infinito"
        # Mover hacia adelante 0.5 metros
        vel_msg.linear.x = velocidad_lineal
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)

        # Calcular el tiempo necesario para recorrer la distancia objetivo
        tiempo_de_movimiento = distancia_recta / velocidad_lineal
        start_time = rospy.get_time()

        # Avanzar durante el tiempo calculado para recorrer la distancia
        while rospy.get_time() - start_time < tiempo_de_movimiento:
            pub.publish(vel_msg)  # Continuar moviéndose
            rate.sleep()  # Mantener la frecuencia

        # Detenerse después de recorrer la distancia
        vel_msg.linear.x = 0.0
        pub.publish(vel_msg)
        rospy.sleep(1)  # Pausa de 1 segundo antes de la rotación

        # Girar 120 grados a la derecha
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = -velocidad_angular  # Giro hacia la derecha
        pub.publish(vel_msg)

        # Tiempo necesario para rotar 120 grados
        start_rotation_120 = rospy.get_time()
        while rospy.get_time() - start_rotation_120 < rotacion_angulo_120 / velocidad_angular:
            pub.publish(vel_msg)  # Continuar girando
            rate.sleep()  # Mantener la frecuencia

        # Detenerse después de la rotación
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)
        rospy.sleep(1)  # Pausa de 1 segundo antes de continuar

        # Mover hacia adelante 0.71 metros (diagonal)
        vel_msg.linear.x = velocidad_lineal
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)

        # Calcular el tiempo necesario para recorrer la distancia diagonal
        tiempo_de_movimiento = distancia_diagonal / velocidad_lineal
        start_time = rospy.get_time()

        # Avanzar durante el tiempo calculado para recorrer la distancia
        while rospy.get_time() - start_time < tiempo_de_movimiento:
            pub.publish(vel_msg)  # Continuar moviéndose
            rate.sleep()  # Mantener la frecuencia

        # Detenerse después de recorrer la distancia
        vel_msg.linear.x = 0.0
        pub.publish(vel_msg)
        rospy.sleep(1)  # Pausa de 1 segundo antes de la rotación

        # Girar 120 grados a la izquierda
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = velocidad_angular  # Giro hacia la izquierda
        pub.publish(vel_msg)

        # Tiempo necesario para rotar 120 grados
        start_rotation_120 = rospy.get_time()
        while rospy.get_time() - start_rotation_120 < rotacion_angulo_120 / velocidad_angular:
            pub.publish(vel_msg)  # Continuar girando
            rate.sleep()  # Mantener la frecuencia

        # Detenerse después de la rotación
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)
        rospy.sleep(1)  # Pausa de 1 segundo antes de continuar

        # Mover hacia adelante 0.5 metros (la segunda vez)
        vel_msg.linear.x = velocidad_lineal
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)

        # Calcular el tiempo necesario para recorrer la distancia objetivo
        tiempo_de_movimiento = distancia_recta / velocidad_lineal
        start_time = rospy.get_time()

        # Avanzar durante el tiempo calculado para recorrer la distancia
        while rospy.get_time() - start_time < tiempo_de_movimiento:
            pub.publish(vel_msg)  # Continuar moviéndose
            rate.sleep()  # Mantener la frecuencia

        # Detenerse después de recorrer la distancia
        vel_msg.linear.x = 0.0
        pub.publish(vel_msg)
        rospy.sleep(1)  # Pausa de 1 segundo antes de la rotación

        # Girar 120 grados a la izquierda (para completar el ciclo)
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = velocidad_angular  # Giro hacia la izquierda
        pub.publish(vel_msg)

        # Tiempo necesario para rotar 120 grados
        start_rotation_120 = rospy.get_time()
        while rospy.get_time() - start_rotation_120 < rotacion_angulo_120 / velocidad_angular:
            pub.publish(vel_msg)  # Continuar girando
            rate.sleep()  # Mantener la frecuencia

        # Detenerse después de la rotación
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)
        rospy.sleep(1)  # Pausa de 1 segundo antes de continuar

        # Mover hacia adelante 0.71 metros (la segunda diagonal)
        vel_msg.linear.x = velocidad_lineal
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)

        # Calcular el tiempo necesario para recorrer la distancia diagonal
        tiempo_de_movimiento = distancia_diagonal / velocidad_lineal
        start_time = rospy.get_time()

        # Avanzar durante el tiempo calculado para recorrer la distancia
        while rospy.get_time() - start_time < tiempo_de_movimiento:
            pub.publish(vel_msg)  # Continuar moviéndose
            rate.sleep()  # Mantener la frecuencia

        # Detenerse después de recorrer la distancia
        vel_msg.linear.x = 0.0
        pub.publish(vel_msg)
        rospy.sleep(1)  # Pausa de 1 segundo antes de completar

    rospy.loginfo("El TurtleBot ha completado el movimiento en forma de infinito de 0.5 metros y 0.71 metros de lado.")


def usage():
    return "%s [n]" % sys.argv[0]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)

    if n == 0:
        mov_0()
    elif n == 1:
        mov_1()
    elif n == 2:
        mov_2()
    elif n == 3:
        mov_3()
