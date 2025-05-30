#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from battery_act.action import Battery
from rclpy.executors import MultiThreadedExecutor

class BatteryCharger(Node):
    def __init__(self):
        super().__init__('battery_charger')
        self._server = ActionServer(
            self,
            Battery,
            'battery_warning',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        target = goal_handle.request.target_percentage
        self.get_logger().info(f'Objetivo de aviso: {target}%')
        current = 100
        feedback = Battery.Feedback()
        while current > target:
            current -= 5
            feedback.current_percentage = current
            goal_handle.publish_feedback(feedback)
            self.get_logger().info(f'Batería actual: {current}%')
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                return Battery.Result()
            time.sleep(1.0)
        result = Battery.Result()
        result.warning = 'Batería Baja, por favor cargue el robot!'
        goal_handle.succeed()
        return result

def main(args=None):
    rclpy.init(args=args)
    node = BatteryCharger()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    executor.spin()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
