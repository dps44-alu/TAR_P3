#! /usr/bin/env python3
import rospy
import actionlib
import mi_accion.msg

def fibonacci_client():
    # Crea el cliente de acción
    client = actionlib.SimpleActionClient('fibonacci', mi_accion.msg.FibonacciAction)
    # Espera a que el servidor de la acción esté disponible
    client.wait_for_server()
    # Crea el objetivo con el valor de orden 20
    goal = mi_accion.msg.FibonacciGoal(orden=20)
    # Envía el objetivo al servidor
    client.send_goal(goal)
    # Espera hasta que el servidor termine
    client.wait_for_result()
    # Devuelve el resultado de la acción
    return client.get_result()  # FibonacciResult

if __name__ == '__main__':
    try:
        # Inicializa el nodo de ROS
        rospy.init_node('fibonacci_client_py')
        result = fibonacci_client()
        print("Resultado:", ', '.join([str(n) for n in result.secuencia_final]))
    except rospy.ROSInterruptException:
        pass
