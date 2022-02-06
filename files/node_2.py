import config
import rospy

if __name__ == '__main__':
    rospy.init_node(config.Node.node_2)

    topic_2_publisher = rospy.Publisher(config.Topic.topic_2, config.DataType.topic_2, queue_size=config.QueueSize.topic_2)
