#!/usr/bin/env python3

import rospy
from p2pkg.msg import MiMensaje

def callback(data):
    rospy.loginfo(f"Recibido -> Fecha: {data.fecha}, Numero: {data.numero}, "
                   f"Posicion: ({data.posicion.position.x}, {data.posicion.position.y}), "
                   f"Orientation w: {data.posicion.orientation.w}")

def nodo_sub_ejercicio2():
    rospy.init_node('nodosub_ejercicio2', anonymous=True)
    rospy.Subscriber('/topic_ejercicio2', MiMensaje, callback)
    rospy.spin()

if __name__ == '__main__':
    nodo_sub_ejercicio2()
