from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
from db import sicbomd5_get_all, sicbomd5_get, sicbomd5_create, sicbomd5_update, sicbomd5_delete

app = Flask(__name__)
app.app_context().push()
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='API Go88',
          description='API Go88',
          )

"""setup config"""
app.config['SECRET_KEY'] = 'dungnt198'
app.config[
    'APP_DB_URI'] = 'mongodb+srv://dungnt196:25Tuananh08@1stcluster17032020.dabsg.azure.mongodb.net/test?retryWrites=true&w=majority'
app.config['APP_NS'] = 'snake_bot'
app.config['SESSION_TYPE'] = 'mongodb'
"""end setup config"""

ns = api.namespace('go88', description='go88 operations')

go88_model = api.model('go88', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'id_phien': fields.String(required=True, description='mã phiên'),
    'xx1': fields.Integer(required=True, description='number xx1'),
    'xx2': fields.Integer(required=True, description='number xx2'),
    'xx3': fields.Integer(required=True, description='number xx3'),
    'rs_number': fields.Integer(required=True, description='kết quả'),
    'rs_str': fields.String(required=True, description='kết quả tài/xỉu'),
    'date_created': fields.String(required=True, description='thời gian tạo')
})


class SibcboMD5(object):
    """
        SicboMD5
    """

    def __init__(self):
        self.lst_sicbomd5 = sicbomd5_get_all()

    def get(self, id_phien):
        for sicbomd5 in self.lst_sicbomd5:
            if sicbomd5['id_phien'] == id_phien:
                return sicbomd5
        api.abort(404, "Todo {} doesn't exist".format(id_phien))

    def create(self, data):
        sicbomd5 = data
        self.lst_sicbomd5.append(sicbomd5)
        return sicbomd5

    def update(self, id, data):
        pass

    def delete(self, id):
        pass


DAOSicboMD5 = SibcboMD5()


# DAO.create({'task': 'Build an API'})
# DAO.create({'task': '?????'})
# DAO.create({'task': 'profit!'})


@ns.route('/')
class SicboList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''

    @ns.doc('list_todos')
    @ns.marshal_list_with(go88_model)
    def get(self):
        '''List all tasks'''
        return DAOSicboMD5.lst_sicbomd5

    @ns.doc('create_sicbomd5')
    @ns.expect(go88_model)
    @ns.marshal_with(go88_model, code=201)
    def post(self):
        '''Create a new task'''
        return DAOSicboMD5.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Sicbo(Resource):
    '''Show a single todo item and lets you delete them'''

    @ns.doc('get_sicbomd5')
    @ns.marshal_with(go88_model)
    def get(self, id_phien):
        '''Fetch a given resource'''
        return DAOSicboMD5.get(id_phien)

    @ns.doc('delete_sicbomd5')
    @ns.response(204, 'Sicbomd5 deleted')
    def delete(self, id_phien):
        '''Delete a task given its identifier'''
        DAOSicboMD5.delete(id_phien)
        return '', 204

    @ns.expect(go88_model)
    @ns.marshal_with(go88_model)
    def put(self, id_phien):
        '''Update a task given its identifier'''
        return DAOSicboMD5.update(id_phien, api.payload)


if __name__ == '__main__':
    app.run(debug=True)
