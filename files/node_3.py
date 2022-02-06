import config
import rospy

if __name__ == '__main__':
    rospy.init_node(config.Node.node_3)

    topic_3_publisher = rospy.Publisher(config.Topic.topic_3, config.DataType.topic_3, queue_size=config.QueueSize.topic_3)
