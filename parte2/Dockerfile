FROM ubuntu:22.04

# Evitar prompts al instalar paquetes y fijar zona horaria
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Madrid

# Argumentos de build para igualar usuario y UID con tu host
ARG USERNAME
ARG USER_UID

# Instalación de dependencias y ROS 2 Humble
RUN apt-get update && apt-get install -y \
    tzdata \
    locales curl gnupg2 lsb-release \
  && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
  && dpkg-reconfigure --frontend noninteractive tzdata \
  && locale-gen en_US.UTF-8 \
  && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 \
  && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
     | apt-key add - \
  && echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" \
     > /etc/apt/sources.list.d/ros2-latest.list \
  && apt-get update && apt-get install -y \
     ros-humble-desktop \
     python3-colcon-common-extensions \
     python3-rosdep \
     python3-argcomplete

# Inicializa rosdep
RUN rosdep init \
  && rosdep update

# Crea un usuario dentro del contenedor con tu UID
RUN useradd -m -s /bin/bash -u ${USER_UID} ${USERNAME} \
  && echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER ${USERNAME}
WORKDIR /home/${USERNAME}/workspace

# Fuente automática de ROS 2 en cada shell
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
