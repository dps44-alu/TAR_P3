cmake_minimum_required(VERSION 3.5)
project(service_temp)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rosidl_default_runtime REQUIRED)

# 1) Generar las interfaces .srv
rosidl_generate_interfaces(\${PROJECT_NAME}
  "srv/ConvertTemp.srv"
)

ament_export_dependencies(rosidl_default_runtime)

# 2) Instalar los scripts Python en lib/service_temp
install(PROGRAMS
  service_temp/server.py
  service_temp/client.py
  DESTINATION lib/\${PROJECT_NAME}
)

ament_package()
