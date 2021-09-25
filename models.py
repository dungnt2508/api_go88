# from db import sicbomd5_get_all, sicbomd5_get, sicbomd5_create, sicbomd5_update, sicbomd5_delete
#
#
# class SibcboMD5(object):
#     """
#         SicboMD5
#     """
#
#     def __init__(self):
#         self.lst_sicbomd5 = sicbomd5_get_all()
#
#     def get(self, id_phien):
#         for sicbomd5 in self.lst_sicbomd5:
#             if sicbomd5['id_phien'] == id_phien:
#                 return sicbomd5
#         # api.abort(404, "Todo {} doesn't exist".format(id_phien))
#
#     def create(self, data):
#         sicbomd5 = data
#         self.lst_sicbomd5.append(sicbomd5)
#         return sicbomd5
#
#     def update(self, id, data):
#         pass
#
#     def delete(self, id):
#         pass
