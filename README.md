# Robotnik - ROS 2 code examples

This repository contains C++ and Python packages with basic code examples in ROS 2.

## Source of the code

The code in this repository is compiled for ROS 2 Foxy. 

These codes and packages are based on the tutorials in the official ROS 2 documentation:

https://docs.ros.org/en/foxy/Tutorials.html

### Requirements

In order to be able to compile the codes from this repository and make them work correctly, it is necessary to have the following installed:

- Ubuntu 20.04.4 LTS Focal
- Ros 2 Foxy

**NOTE:** The next repository explains how to create a Docker container with these requirements.

https://github.com/RobotnikAutomation/robotnik_ros_base_container/tree/foxy-devel

## ROS 2 code examples - Installation

Go to the ROS 2 workspace directory (e.g. named '/workspace' as in the Robotnik ROS 2 Docker container):

```bash
source /opt/ros/foxy/setup.bash
mkdir -p ~/workspace/src
cd ~/workspace/src/
```

In the '/src' folder inside the workspace directory clone this repository  by executing:

```bash
git clone git@github.com:RobotnikAutomation/ros2_code_examples.git
```

Verify that everything has been cloned properly:

```bash
cd ros2_code_examples/
ls
```

Go to the ROS 2 workspace directory to compile it. Then setup the environment in order to use the built packages.

```bash
cd ~/workspace
colcon build
source install/setup.bash
```

## ROS 2 code examples - Testing

First, make sure the workspace is built and the environment is setup:

```bash
source /opt/ros/foxy/setup.bash
cd ~/workspace
colcon build
source install/setup.bash
```

**Testing a simple publisher and subscriber (C++) in a terminal:**

```bash
ros2 launch cpp_pubsub cpp_pubsub_launch.launch.py
```

**Testing a simple publisher and subscriber (Python) in a terminal:**

```bash
ros2 launch py_pubsub py_pubsub_launch.launch.py
```

**Testing a simple publisher and subscriber (C++) on two terminals:**

- First console:

  ```bash
  ros2 run cpp_pubsub talker
  ```

- Second console:

  ```bash
  ros2 run cpp_pubsub talker
  ```

**Testing a simple publisher and subscriber (Python) on two terminals:**

- First console:

  ```bash
  ros2 run py_pubsub talker
  ```

- Second console:

  ```bash
  ros2 run py_pubsub talker
  ```

**Testing a simple publisher in C++ and subscriber in Python on two terminals:**

- First console:

  ```bash
  ros2 run cpp_pubsub talker
  ```

- Second console:

  ```bash
  ros2 run py_pubsub talker
  ```



