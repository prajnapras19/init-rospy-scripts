import config
import rospy

def topic1Callback(msg):
    pass

if __name__ == '__main__':
    rospy.init_node(config.Node.node_4)

    topic_1_subscriber = rospy.Subscriber(config.Topic.topic_1, config.DataType.topic_1, topic1Callback)

    rospy.spin()
