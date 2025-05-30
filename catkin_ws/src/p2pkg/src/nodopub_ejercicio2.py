#!/usr/bin/env python3

import rospy
from p2pkg.msg import MiMensaje
from random import random
from datetime import datetime

def nodo_pub_ejercicio2(numero):
    pub = rospy.Publisher('/topic_ejercicio2', MiMensaje, queue_size=10)
    rospy.init_node('nodopub_ejercicio2', anonymous=True)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        posicion = MiMensaje().posicion
        posicion.position.x = random()
        posicion.position.y = random()
        posicion.position.z = random()
        posicion.orientation.x = random()
        posicion.orientation.y = random()
        posicion.orientation.z = random()
        posicion.orientation.w = random()

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        mensaje = MiMensaje()
        mensaje.numero = numero
        mensaje.posicion = posicion
        mensaje.fecha = fecha

        #logeo valores
        rospy.loginfo(f"Fecha: {mensaje.fecha}, Numero: {mensaje.numero}, "
                       f"Posicion: ({mensaje.posicion.position.x}, {mensaje.posicion.position.y}), "
                       f"Orientation w: {mensaje.posicion.orientation.w}")
        pub.publish(mensaje)
        rate.sleep()

if __name__ == '__main__':
    try:
        numero = int(input("Introduce un numero para el campo numero: "))
        nodo_pub_ejercicio2(numero)
    except rospy.ROSInterruptException:
        pass
