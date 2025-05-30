cmake_minimum_required(VERSION 3.5)
project(battery_act)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Genera primero la interfaz .action
rosidl_generate_interfaces(\${PROJECT_NAME}
  "action/Battery.action"
)
ament_export_dependencies(rosidl_default_runtime)

# Instala tus scripts QUE ESTÁN EN scripts/
install(PROGRAMS
  scripts/battery_charger.py
  scripts/battery_client.py
  DESTINATION lib/\${PROJECT_NAME}
)

ament_package()
