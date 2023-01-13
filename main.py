from tools import pet
import api_request


api_request.post_create_pet_request(headers=pet.headers_post_pet,
                                    body_json=pet.json_pet,
                                    json_comparison=pet.json_pet,
                                    type_request='POST')

api_request.get_pet_request(type_request='GET',
                            pet_id=str(pet.json_pet['id']),
                            json_comparison=pet.json_pet)

api_request.post_update_pet_request(type_request='UPDATE',
                                    json_comparison=pet.response_update,
                                    params=pet.pet_update,
                                    pet_id=str(pet.json_pet['id']))

api_request.get_pet_request(type_request='GET',
                            pet_id=str(pet.json_pet['id']),
                            json_comparison=pet.json_pet_update)

api_request.delete_pet_request(type_request='DELETE',
                               pet_id=str(pet.json_pet['id']),
                               json_comparison=pet.response_delete)

api_request.get_pet_request(type_request='GET',
                            pet_id=str(pet.json_pet['id']),
                            json_comparison=pet.json_pet_update)
