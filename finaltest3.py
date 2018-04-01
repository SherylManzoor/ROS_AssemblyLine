#!/usr/bin/env python
# BEGIN ALL
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math
from math import pi
# quaternion transformations
from tf.msg import tfMessage
from tf.transformations import quaternion_from_euler


print "============ Starting tutorial setup"
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',
                anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("manipulator") #  must find the config file to check this name. what if 3 robot arms

print "============ Reference frame: %s" % group.get_planning_frame()
print "============ Reference frame: %s" % group.get_end_effector_link()
print "============ Robot Groups:"
print robot.get_group_names()
print "============ Printing robot state"
print robot.get_current_state()
print "============"
print "============ Generating plan 1"
q1 = quaternion_from_euler(0, pi/2, 0)
print "The quaternion representation is %s %s %s %s." % (q1[0], q1[1], q1[2], q1[3])
pose_target1 = geometry_msgs.msg.Pose()
pose_target1.position.x = 0.6
pose_target1.position.y = 0
pose_target1.position.z = 0.1
pose_target1.orientation.x = q1[0]
pose_target1.orientation.y = q1[1]
pose_target1.orientation.z = q1[2]
pose_target1.orientation.w = q1[3]
group.set_pose_target(pose_target1)
plan1 = group.plan()
group.go(wait=True)
rospy.sleep(5)
group.clear_pose_targets()

print "============ Generating plan 2"
q2 = quaternion_from_euler(pi, 0 , 0)
print "The quaternion representation is %s %s %s %s." % (q2[0], q2[1], q2[2], q2[3])
pose_target2 = geometry_msgs.msg.Pose()
pose_target2.position.x = -0.6
pose_target2.position.y = 0
pose_target2.position.z = 0.1
pose_target1.orientation.x = q2[0]
pose_target1.orientation.y = q2[1]
pose_target1.orientation.z = q2[2]
pose_target1.orientation.w = q2[3]
group.set_pose_target(pose_target2)
plan2 = group.plan()
group.go(wait=True)
rospy.sleep(5)
group.clear_pose_targets()








# END ALL
