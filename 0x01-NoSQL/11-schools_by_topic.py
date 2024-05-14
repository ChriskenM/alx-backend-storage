#!/usr/bin/env python3
"""
module returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.
    Args:
        mongo_collection: pymongo collection object.
        topic: Topic to search.
    Returns:
        A list of schools having the specified topic.
    """
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
