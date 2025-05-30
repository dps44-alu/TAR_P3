#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class WallFollower:
    def __init__(self):
        rospy.init_node("wall_follower", anonymous=True)
        #topic para Tb2:
        self.pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
        self.twist = Twist()
        self.rate = rospy.Rate(10)

        #parametros mov
        self.forward_speed = 0.2
        self.angular_speed = 0.4

        #deteccion
        self.front_threshold = 0.8   #se considera obstaculo frontal si la distancia es menor
        self.right_threshold = 0.8   #se espera pared a la derecha si la distancia es menor

        self.laser_data = None

        rospy.Subscriber('/scan', LaserScan, self.laser_callback)

        self.state = "forward"
        self.rotation_start_time = None
        #tiempo para giro pequeño mas o menos son 22 perico,comprueba si va tb3
        self.rotation_duration = 1.0  

    def laser_callback(self, data):
        #indice central corresponde al frente
        #indice 0 corresponde aprox a la derecha
        self.laser_data = data.ranges

    def run(self):
        rospy.loginfo("Iniciando avance continuo hasta detectar pared frontal, luego giro pequeño para ajustar la pared a la derecha")
        while not rospy.is_shutdown():
            #avanza normal si no hay datos
            if self.laser_data is None or len(self.laser_data) == 0:
                self.twist.linear.x = self.forward_speed
                self.twist.angular.z = 0.0
            else:
                num_ranges = len(self.laser_data)
                center_idx = num_ranges // 2
                right_idx = 0  #ajusta este valor si orden angular es distinto en tu sensor

                front_dist = self.laser_data[center_idx]
                right_dist = self.laser_data[right_idx]

                if self.state == "forward":
                    if front_dist < self.front_threshold:
                        rospy.loginfo("Pared frontal detectada (%.2f m). Ejecutando giro pequeño para colocar la pared a la derecha.", front_dist)
                        # Cambiar de estado a "rotate" para hacer un pequeño giro
                        self.state = "rotate"
                        self.rotation_start_time = rospy.get_time()
                        self.twist.linear.x = 0.0
                        # Giro a la izquierda (para que la pared que estaba al frente pase a la derecha)
                        self.twist.angular.z = self.angular_speed  
                    else:
                        # Avanza hacia adelante
                        self.twist.linear.x = self.forward_speed
                        # Si la pared a la derecha no está lo suficientemente cerca, se hace un giro suave a la derecha
                        if right_dist > self.right_threshold:
                            rospy.loginfo("Sin pared cercana a la derecha (%.2f m). Aplicando pequeña corrección hacia la derecha.", right_dist)
                            self.twist.angular.z = -0.2
                        else:
                            self.twist.angular.z = 0.0

                # Estado "rotate": se gira a la izquierda por un tiempo corto (giro pequeño)
                elif self.state == "rotate":
                    self.twist.linear.x = 0.0
                    self.twist.angular.z = self.angular_speed
                    if rospy.get_time() - self.rotation_start_time > self.rotation_duration:
                        rospy.loginfo("Giro pequeño completado. Retomando avance.")
                        self.state = "forward"

            self.pub.publish(self.twist)
            self.rate.sleep()

    def stop(self):
        rospy.loginfo("Deteniendo el robot...")
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.0
        self.pub.publish(self.twist)

if __name__ == '__main__':
    try:
        wf = WallFollower()
        wf.run()
    except rospy.ROSInterruptException:
        wf.stop()

