#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

def callback_odom(data):
    # Lấy dữ liệu vị trí (pose) từ odom
    position = data.pose.pose.position
    orientation = data.pose.pose.orientation

    # Ghi dữ liệu vào file
    with open("/home/yi/catkin_ws/src/agv_multigoal/src/log/data_odom.txt", "a") as f:
        f.write(f"{rospy.Time.now().to_sec()}, {position.x}, {position.y}, {orientation.z}, {orientation.w}\n")
    rospy.loginfo("Ghi dữ liệu odom: x=%f, y=%f", position.x, position.y)

def main():
    rospy.init_node('odom_logger', anonymous=True)
    rospy.Subscriber("/odom", Odometry, callback_odom)
    rospy.loginfo("Node đang ghi dữ liệu odom vào /home/yi/catkin_ws/src/agv_multigoal/src/log/data_odom.txt")
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        rospy.loginfo("Node bị gián đoạn!")