#!/usr/bin/env python3
import sys
import rospy
from geometry_msgs.msg import Twist
import math

def mov():
    rospy.init_node('movimiento', anonymous=True)
    pub = rospy.Publisher("/cmd_vel_mux/input/teleop", Twist, queue_size=10)
    
    # Esperar a que el nodo esté listo
    rospy.sleep(2)
    vel_msg = Twist()
    
    # Parámetros de movimiento
    velocidad_lineal = 0.2  # Velocidad lineal (en m/s)
    velocidad_angular = 0.5  # Velocidad angular (en radianes/s)
    rotacion_angulo = math.pi / 2  # Rotación de 90 grados (en radianes)
    distancia_1 = 1.5  # Primera distancia a recorrer (1.5 metros)
    distancia_2 = 1.35  # Segunda distancia a recorrer (1.35 metros)
    
    rate = rospy.Rate(10)  # Frecuencia de publicación, 10 Hz
    
    try:
        # Movimiento 1: Avanzar 1.5 metros
        vel_msg.linear.x = velocidad_lineal
        vel_msg.angular.z = 0.0
        inicio_tiempo = rospy.get_time()
        while (rospy.get_time() - inicio_tiempo) < (distancia_1 / velocidad_lineal) and not rospy.is_shutdown():
            pub.publish(vel_msg)
            rate.sleep()
            
        # Detenerse
        vel_msg.linear.x = 0.0
        pub.publish(vel_msg)
        rate.sleep()
        rospy.loginfo("Primer movimiento completado: 1.5 metros adelante")
        
        # Movimiento 2: Girar 90 grados EN SENTIDO CONTRARIO (negativo)
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = -velocidad_angular  # Velocidad angular negativa para giro opuesto
        inicio_tiempo = rospy.get_time()
        while (rospy.get_time() - inicio_tiempo) < (rotacion_angulo / velocidad_angular) and not rospy.is_shutdown():
            pub.publish(vel_msg)
            rate.sleep()
            
        # Detenerse
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)
        rate.sleep()
        rospy.loginfo("Giro de 90 grados en sentido contrario completado")
        
        # Movimiento 3: Avanzar 1.35 metros
        vel_msg.linear.x = velocidad_lineal
        vel_msg.angular.z = 0.0
        inicio_tiempo = rospy.get_time()
        while (rospy.get_time() - inicio_tiempo) < (distancia_2 / velocidad_lineal) and not rospy.is_shutdown():
            pub.publish(vel_msg)
            rate.sleep()
            
        # Detenerse final
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)
        rospy.loginfo("Movimiento completado: 1.35 metros adelante")
        rospy.loginfo("Robot detenido en posición final")
        
    except rospy.ROSInterruptException:
        # Detener el robot si hay interrupción
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)
        rospy.loginfo("Movimiento interrumpido")

if __name__ == '__main__':
    try:
        mov()
    except rospy.ROSInterruptException:
        pass
