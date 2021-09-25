from flask import current_app, g, session, jsonify, json
from werkzeug.local import LocalProxy
import pymongo
from datetime import datetime
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
    result, msg = ('1', None)
    try:
        data = list(db.sicbomd5.find({}, {"_id": 0})) if db.sicbomd5.find({}, {"_id": 0}) else []
        result = 1
        msg = 'get all ok'
    except Exception as e:
        result, msg = ('0', str(e))
    return data


def sicbomd5_get(id_phien):
    result, msg, items = ('1', None, [])
    try:
        data = db.sicbomd5.find_one({"id_phien": id_phien}, {"_id": 0})
    except Exception as e:
        print(e)

    return data


def sicbomd5_create(sicbomd5):
    result, msg, items = ('1', None, [])
    try:
        sicbomd5["rs_number"] = sicbomd5["xx1"] + sicbomd5["xx2"] + sicbomd5["xx3"]
        sicbomd5["rs_str"] = "Tài" if sicbomd5["rs_number"] > 10 else "Xỉu"
        sicbomd5["date_created"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data = db.sicbomd5.insert_one(sicbomd5)
        # print(data)
        result = 1
        msg = "insert item done"
    except Exception as e:
        result, msg = ('0', str(e))
    return jsonify({'result': result, 'msg': msg, 'items': items})


def sicbomd5_update(id_phien):
    pass


def sicbomd5_delete(id_phien):
    pass