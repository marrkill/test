from tools import decription
import pytest

# from request import api_request
from tools import pet
import api_request


@pytest.fixture(autouse=True)
def print_setting():
    print(decription.run_business_process)


@pytest.mark.parametrize('test_type_request, test_headers, test_body_json, test_json_comparison',
                         [('POST', pet.headers_post_pet, pet.json_pet, pet.json_pet)])
def test_post(test_type_request, test_headers, test_body_json, test_json_comparison):
    assert api_request.post_create_pet_request(type_request=test_type_request,
                                               body_json=test_body_json,
                                               headers=test_headers,
                                               json_comparison=test_json_comparison)
