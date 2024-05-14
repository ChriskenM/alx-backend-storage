#!/usr/bin/env python3
"""
module inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts new document into MongoDB collection based on keyword arguments.
    Args:
        mongo_collection: pymongo collection object.
        **kwargs: keyword arguments representing document attributes.
    Returns:
        The _id of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
