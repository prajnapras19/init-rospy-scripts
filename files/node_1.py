import config
import rospy

def topic2Callback(msg):
    pass

def topic3Callback(msg):
    pass

if __name__ == '__main__':
    rospy.init_node(config.Node.node_1)

    topic_1_publisher = rospy.Publisher(config.Topic.topic_1, config.DataType.topic_1, queue_size=config.QueueSize.topic_1)

    topic_2_subscriber = rospy.Subscriber(config.Topic.topic_2, config.DataType.topic_2, topic2Callback)
    topic_3_subscriber = rospy.Subscriber(config.Topic.topic_3, config.DataType.topic_3, topic3Callback)

    rospy.spin()
