from flask import current_app, g, session, jsonify
from werkzeug.local import LocalProxy
import pymongo
from pymongo import MongoClient, DESCENDING, ASCENDING
from pymongo.write_concern import WriteConcern
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from pymongo.read_concern import ReadConcern


def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)
    APP_DB_URI = current_app.config["APP_DB_URI"]
    APP_DB_NAME = current_app.config["APP_NS"]
    if db is None:
        db = g._database = pymongo.MongoClient(
            APP_DB_URI,
            # username="root",
            # password="abcd1234",
            maxPoolSize=50,  # Set the maximum connection pool size to 50 active connections.
            w='majority',  # Set the write timeout limit to 2500 milliseconds.
            wtimeout=2500
        )[APP_DB_NAME]
    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)


def sicbomd5_get_all():
    data = list(db.sicbomd5.find({}, {"_id": 0})) if db.sicbomd5.find({}, {"_id": 0}) else []
    return data


def sicbomd5_get(id_phien):
    data = db.sicbomd5.find_one({"id_phien": id_phien}, {"_id": 0})
    return data


def sicbomd5_create(sicbomd5):
    db.sicbomd5.insert_one(sicbomd5)


def sicbomd5_update(id_phien):
    pass


def sicbomd5_delete(id_phien):
    pass