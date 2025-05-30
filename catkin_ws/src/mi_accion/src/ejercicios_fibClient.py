#!/usr/bin/env python3
import rospy
import actionlib
from std_msgs.msg import String
import mi_accion.msg

def ejercicios_fibonacci_client(orden):
    # Crea el cliente de acción
    client = actionlib.SimpleActionClient('ej_fibonacci', mi_accion.msg.FibonacciAction)
    # Espera a que el servidor de acción esté disponible
    client.wait_for_server()

    # Crea un objetivo con el orden de la secuencia
    goal = mi_accion.msg.FibonacciGoal(orden=orden)
    # Envía el objetivo al servidor
    client.send_goal(goal)

    # Publica "en proceso" en el topic /estado_accion mientras se espera la acción
    pub = rospy.Publisher('/estado_accion', String, queue_size=10)
    while not client.wait_for_result(rospy.Duration(1)):
        pub.publish("En proceso...")

    # Una vez que la acción ha terminado, obtiene el resultado
    result = client.get_result()
    return result

if __name__ == '__main__':
    try:
        rospy.init_node('ej_fibonacci_client')

        orden = rospy.get_param('~orden', 10)

        result = ejercicios_fibonacci_client(orden)

        rospy.loginfo("Secuencia de Fibonacci: %s", result.secuencia_final)

    except rospy.ROSInterruptException:
        pass
