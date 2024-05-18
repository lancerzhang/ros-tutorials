#!/usr/bin/env python3
#encodeing=utf-8

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("chao_node")
    rospy.logwarn("我的枪")

    pub = rospy.Publisher("kuai_shang_che", String, queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("我要刷屏了")
        msg = String()
        msg.data = "国服马超"
        pub.publish(msg)
        rate.sleep()
