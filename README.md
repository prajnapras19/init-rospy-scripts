# Init Rospy Scripts
---
## Description
This script was created to make initialization of scripts with `rospy` easier, with the creator of the projects already designed the list of nodes, topics, and publish-subscribe behavior.

## Instruction
- Create 3 files: `node.txt`, `topic.txt`, `pubsub.txt`.
- `node.txt` contains all nodes, each node name separated by a newline, and every word of a node name separated with a space.
- `topic.txt` contains all topics, each topic name separated by a newline, and every word of a topic name separated with a space.
- `pubsub.txt` contains all pubsub of topics in each line in following format:
    ```
    [pub / sub] [node name]: [topic 1], [topic 2], ...
    ```
  
    e.g.:
    ```
    pub node1: topic1, topic2
    sub node1: topic3, topic4
    ```
- Usage:
    ```
    python3 generate.py
    ```

## Notes
- All letters are in lowercase alphanumeric, following already known variable naming conventions.
- All topics and nodes in `pubsub.txt` should exists in `node.txt` and `topic.txt`.
- This script is not being tested yet. Will check on it later.