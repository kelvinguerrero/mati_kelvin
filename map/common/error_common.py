from map.models import Teacher
import json


def error_json(numero, mensaje):
    json_response = json.dumps({"Error": numero, "mensaje": mensaje})
    return json_response