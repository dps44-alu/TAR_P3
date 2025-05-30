#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import sys

class TrajectoryPlotter:
    def __init__(self):
        #configuracion inicio
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        self.x_data = []
        self.y_data = []
        self.line, = self.ax.plot([], [], 'b-', lw=2, label='Trayectoria')
        self.start_point = None
        self.movement_name = ""
        
        #gráfico
        self.ax.set_xlabel('X (metros)')
        self.ax.set_ylabel('Y (metros)')
        self.ax.set_title('Trayectoria del TurtleBot2 en Tiempo Real')
        self.ax.grid(True)
        self.ax.legend()
        self.ax.axis('equal')  # Mantener proporción 1:1
        
        rospy.Subscriber("/odom", Odometry, self.odom_callback)
        
        # Identificar movimiento actual
        if len(sys.argv) > 1:
            mov_num = int(sys.argv[1])
            self.movement_name = {
                0: "Línea Recta (2m)",
                1: "Triángulo (3m)",
                2: "Cuadrado (1m)",
                3: "Infinito"
            }.get(mov_num, "Desconocido")

    def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        
        if not self.x_data:
            self.start_point = (x, y)
        
        self.x_data.append(x)
        self.y_data.append(y)
        
        #actualiza limites
        if len(self.x_data) > 10:
            margin = 0.5
            self.ax.set_xlim(min(self.x_data)-margin, max(self.x_data)+margin)
            self.ax.set_ylim(min(self.y_data)-margin, max(self.y_data)+margin)
            self.ax.set_title(f'Trayectoria: {self.movement_name}\n'
                             f'Posición Actual: X={x:.2f}m, Y={y:.2f}m')

    def update_plot(self, frame):
        if self.x_data and self.y_data:
            self.line.set_data(self.x_data, self.y_data)
            
            #empieza
            if self.start_point:
                if not hasattr(self, 'start_marker'):
                    self.start_marker, = self.ax.plot(
                        self.start_point[0], self.start_point[1], 
                        'go', markersize=8, label='Inicio')
                else:
                    self.start_marker.set_data(self.start_point[0], self.start_point[1])
        
        return self.line, self.start_marker if hasattr(self, 'start_marker') else self.line

    def run(self):
        ani = FuncAnimation(self.fig, self.update_plot, interval=200, blit=True)
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    rospy.init_node('turtlebot_trajectory_plotter', anonymous=True)
    
    if len(sys.argv) < 2:
        print("Uso: rosrun tu_paquete dibuja_mov.py <0|1|2|3>")
        print("0: Línea, 1: Triángulo, 2: Cuadrado, 3: Infinito")
        sys.exit(1)
    
    try:
        plotter = TrajectoryPlotter()
        plotter.run()
    except rospy.ROSInterruptException:
        pass
