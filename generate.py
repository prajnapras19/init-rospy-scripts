import os
import shutil

TAB = ' ' * 4

f = open('node.txt')
lst = f.read().strip('\n').split('\n')
f.close()
nodes = {}
nodes_list = []
for x in lst:
    nodes_list.append(x)
    nodes[x] = {}
    nodes[x]['snake'] = x.replace(' ', '_')
    nodes[x]['pascal'] = x.title().replace(' ', '')

f = open('topic.txt')
lst = f.read().strip('\n').split('\n')
f.close()
topics = {}
topics_list = []
for x in lst:
    topics_list.append(x)
    topics[x] = {}
    topics[x]['snake'] = x.replace(' ', '_')
    topics[x]['pascal'] = x.title().replace(' ', '')
    topics[x]['camel'] = x.split(' ')[0] + ' '.join(x.split(' ')[1:]).title().replace(' ', '')

f = open('pubsub.txt')
lst = f.read().strip('\n').split('\n')
for x in lst:
    n, top = x.split(': ')
    ps = n[:3]
    n = n[4:]
    nodes[n][ps] = top.split(', ')
f.close()

nodes_list.sort()
topics_list.sort()

save_dir = 'files/'
try:
    shutil.rmtree(save_dir)
except:
    pass
os.mkdir(save_dir)

# config
f = open(save_dir + 'config.py', 'w')
f.write('from std_msgs.msg import Float64\n')
f.write('\nclass Node():\n')
for x in nodes_list:
    f.write(TAB + nodes[x]['snake'] + ' = \'' + nodes[x]['pascal'] + '\'' + '\n')

f.write('\nclass Topic():\n')
for x in topics_list:
    f.write(TAB + topics[x]['snake'] + ' = \'/' + topics[x]['snake'] + '\'\n')

f.write('\nclass DataType():\n')
for x in topics_list:
    f.write(TAB + topics[x]['snake'] + ' = Float64\n')

f.write('\nclass QueueSize():\n')
for x in topics_list:
    f.write(TAB + topics[x]['snake'] + ' = 8\n')
f.close()

# node files
for x in nodes_list:
    f = open(save_dir + nodes[x]['snake'] + '.py', 'w')
    f.write('import config\n')
    f.write('import rospy\n')

    try:
        for y in nodes[x]['sub']:
            f.write('\ndef ' + topics[y]['camel'] + 'Callback(msg):\n    pass\n')
    except:
        pass

    f.write('\nif __name__ == \'__main__\':\n')
    f.write(TAB + 'rospy.init_node(config.Node.' + nodes[x]['snake'] +')\n')

    try:
        zzz = True
        for y in nodes[x]['pub']:
            if zzz:
                zzz = False
                f.write('\n')
            res = TAB
            res += topics[y]['snake']
            res += '_publisher = rospy.Publisher(config.Topic.'
            res += topics[y]['snake']
            res += ', config.DataType.'
            res += topics[y]['snake']
            res += ', queue_size=config.QueueSize.'
            res += topics[y]['snake']
            res += ')\n'
            f.write(res)
    except:
        pass

    try:
        zzz = True
        for y in nodes[x]['sub']:
            if zzz:
                zzz = False
                f.write('\n')
            res = TAB
            res += topics[y]['snake']
            res += '_subscriber = rospy.Subscriber(config.Topic.'
            res += topics[y]['snake']
            res += ', config.DataType.'
            res += topics[y]['snake']
            res += ', '
            res += topics[y]['camel'] + 'Callback)\n'
            f.write(res)
        res = '\n'
        res += TAB
        res += 'rospy.spin()\n'
        f.write(res)
    except:
        pass
    
    f.close()
