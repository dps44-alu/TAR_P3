#!/usr/bin/env bash
#
# Lanza un contenedor Docker con ROS 2 Humble
#

export containerName=ros_humble

# Permitir X11 local para aplicaciones gráficas (opcional)
xhost +local:docker

docker run --rm -it \
  --name ${containerName} \
  --network host \
  -e DISPLAY=${DISPLAY} \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v "$PWD/..:/workspace:rw" \
  --workdir /workspace \
  ros_humble:latest \
  bash
