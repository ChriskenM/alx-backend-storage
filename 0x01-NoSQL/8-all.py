#!/usr/bin/env python3
"""
Module lists all documents in collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in the given MongoDB collection.
    Args:
        mongo_collection: pymongo collection object.
    Returns:
        A list of documents in the collection.
    """
    return list(mongo_collection.find())
