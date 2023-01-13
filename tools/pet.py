url_swagger_pet = 'https://petstore.swagger.io/v2/pet/'

headers_post_pet = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

headers_update_pet = {
    "Content-Type": "application/x-www-form-urlencoded"
}

json_pet = {
    "id": 666,
    "category": {
        "id": 777,
        "name": 'cat'
    },
    "name": "pyp",
    "photoUrls": [],
    "tags": [
        {
            "id": 888,
            "name": "long"
        },
        {
            "id": 999,
            "name": "red"
        }
    ],
    "status": "available"
}

json_pet_update = {
    "id": 666,
    "category": {
        "id": 777,
        "name": 'cat'
    },
    "name": "pupu",
    "photoUrls": [],
    "tags": [
        {
            "id": 888,
            "name": "long"
        },
        {
            "id": 999,
            "name": "red"
        }
    ],
    "status": "pipi"
}

json_pet_error = {
    "id": 777,
    "category": {
        "id": 777,
        "name": 'cat'
    },
    "name": "pyp",
    "photoUrls": [],
    "tags": [
        {
            "id": 888,
            "name": "long"
        },
        {
            "id": 999,
            "name": "red"
        }
    ],
    "status": "available"
}

response_delete = {
    "code": 200,
    "type": "unknown",
    "message": str(json_pet['id'])
}

response_update = {
    "code": 200,
    "type": "unknown",
    "message": str(json_pet['id'])
}
pet_update = dict(name='pupu', status='pipi')
