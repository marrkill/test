from tools import pet
from tools import check_response_structure

import requests
import datetime


def post_create_pet_request(headers, body_json, json_comparison, type_request):
    print(datetime.datetime.now())
    response = requests.post(pet.url_swagger_pet,
                             headers=headers,
                             json=body_json)
    print(datetime.datetime.now())
    check_response_structure.check_structure_assert(response_request=response,
                                                    json_comparison=json_comparison,
                                                    type_request=type_request)
    print(response.json())
    print(datetime.datetime.now())
    return True


def get_pet_request(type_request, pet_id, json_comparison):
    print(datetime.datetime.now())
    response = requests.get(pet.url_swagger_pet + pet_id)
    print(datetime.datetime.now())
    check_response_structure.check_structure_assert(type_request=type_request,
                                                    response_request=response,
                                                    json_comparison=json_comparison)
    print(datetime.datetime.now())
    print(response.json())


def post_update_pet_request(type_request, json_comparison, params, pet_id):
    print(datetime.datetime.now())
    response = requests.post(pet.url_swagger_pet+pet_id,
                             data=params
                             )
    print(datetime.datetime.now())
    check_response_structure.check_structure_assert(type_request=type_request,
                                                    response_request=response,
                                                    json_comparison=json_comparison)
    print(datetime.datetime.now())
    print(response.json())


def delete_pet_request(type_request, pet_id, json_comparison):
    print(datetime.datetime.now())
    response = requests.delete(pet.url_swagger_pet + pet_id)
    print(datetime.datetime.now())
    check_response_structure.check_structure_assert(type_request=type_request,
                                                    response_request=response,
                                                    json_comparison=json_comparison)
    print(datetime.datetime.now())
