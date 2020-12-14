from rest_api_framework import models
from rest_api_framework.datastore import SQLiteDataStore
from rest_api_framework.views import JsonResponse
from rest_api_framework.controllers import Controller
from rest_api_framework.datastore.validators import UniqueTogether

class UserModel(models.Model):

    fields = [models.StringField(name="key", required=True),
              models.StringField(name="value", required=True),
              models.PkField(name="id")]


class UserEndPoint(Controller):
    ressource = {
        "ressource_name": "keyvalues",
        "ressource": {"name": "database/keyvalues.db", "table": "keyvalues"},
        "model": UserModel,
        "datastore": SQLiteDataStore
        }

    controller = {
        "list_verbs": ["GET", "POST"],
        "unique_verbs": ["GET", "PUT", "DELETE"]
        }

    view = {"response_class": JsonResponse,
        "options": {"formaters": ["add_ressource_uri","remove_id"]}}

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    from rest_api_framework.controllers import WSGIDispatcher
    app = WSGIDispatcher([UserEndPoint])
    run_simple('localhost', 5000, app, use_debugger=True, use_reloader=False)