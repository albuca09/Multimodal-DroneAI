
FROM nvcr.io/nvidia/l4t-tensorrt:r35.4.1-py3
WORKDIR /app
COPY ros2_ws /app/ros2_ws
RUN apt-get update && apt-get install -y ros-humble-desktop
RUN pip install pycuda
CMD ["bash"]
