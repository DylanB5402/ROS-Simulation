cmake_minimum_required(VERSION 3.0.2)
project(ROS-Simulation)

find_package(catkin REQUIRED COMPONENTS rospy geometry_msgs std_msgs)

catkin_package(
  INCLUDE_DIRS scripts
  LIBRARIES urdf_sim_tutorial
  CATKIN_DEPENDS rospy geometry_msgs std_msgs
  DEPENDS system_lib
)

catkin_install_python(PROGRAMS 
  scripts/drive.py 
  scripts/move_head.py 
  scripts/move_model.py 
  scripts/tank_drive.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/scripts
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

#add_executable(drive.py scripts/drive.py)

#catkin_python_setup()




install(DIRECTORY config launch urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

