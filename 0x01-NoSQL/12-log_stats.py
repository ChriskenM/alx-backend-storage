#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB:
"""
from pymongo import MongoClient


def get_log_count(collection):
    """Returns the number of documents in the collection."""
    return collection.count_documents({})


def get_method_counts(collection):
    """Returns the counts of each HTTP method in the collection."""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    counts = {}
    for method in methods:
        counts[method] = collection.count_documents({"method": method})
    return counts


def get_status_check_count(collection):
    """Returns the count of logs with method=GET and path=/status."""
    return collection.count_documents({"method": "GET", "path": "/status"})


def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Get total log count
    total_logs = get_log_count(collection)
    print("{} logs".format(total_logs))

    # Get method counts
    print("Methods:")
    method_counts = get_method_counts(collection)
    for method, count in method_counts.items():
        print("\tmethod {}: {}".format(method, count))

    # Get count of logs with method=GET and path=/status
    status_check_count = get_status_check_count(collection)
    print("{} status check".format(status_check_count))


if __name__ == "__main__":
    main()
