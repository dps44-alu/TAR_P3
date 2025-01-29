#!/bin/bash

export containerName=ros_noetic
sleep 3 && \
        xhost +local:`docker inspect --format='{{ .Config.Hostname }}' $containerName` >/dev/null 2>&1 &

docker run --rm -it -e "TERM=xterm-256color" \ 
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -e DISPLAY=${DISPLAY} --network host \
        --volume="$PWD:/workspace:rw" \
        --name $containerName \
        ros_noetic:latest bash
