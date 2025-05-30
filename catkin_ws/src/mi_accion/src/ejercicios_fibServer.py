#!/usr/bin/env python3
import rospy
import actionlib
import math
import mi_accion.msg

class EjFibonacciAction(object):
    _feedback = mi_accion.msg.FibonacciFeedback()
    _result = mi_accion.msg.FibonacciResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, mi_accion.msg.FibonacciAction, execute_cb=self.execute_cb, auto_start=False)
        self._as.start()

    def execute_cb(self, goal):
        r = rospy.Rate(1)
        success = True
        self._feedback.secuencia_actual = [0, 1]
        rospy.loginfo('%s: Ejecutando con orden %i' % (self._action_name, goal.orden))

        for i in range(2, goal.orden):
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Cancelado' % self._action_name)
                self._as.set_preempted()
                success = False
                break

            # add next number
            next_number = self._feedback.secuencia_actual[-1] + self._feedback.secuencia_actual[-2]
            self._feedback.secuencia_actual.append(next_number)

            # avg y sqrt
            media = sum(self._feedback.secuencia_actual) / len(self._feedback.secuencia_actual)
            self._feedback.progreso = math.sqrt(media)

            self._as.publish_feedback(self._feedback)
            rospy.loginfo('%s: Progreso %f' % (self._action_name, self._feedback.progreso))

            r.sleep()

        if success:
            self._result.secuencia_final = self._feedback.secuencia_actual
            rospy.loginfo('%s: Completado' % self._action_name)
            self._as.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node('ej_fibonacci_server')
    server = EjFibonacciAction(rospy.get_name())
    rospy.loginfo('Servidor de Fibonacci lanzado y esperando un objetivo!')
    rospy.spin()
