from tools import decription


def check_structure(type_request, response_request, json_comparison):
    if response_request.ok:
        if response_request.json() == json_comparison:
            print(type_request + ' - ' + decription.request_ok + decription.response_ok)
        else:
            print(type_request + decription.struct_not_expected)
    else:
        print(type_request, decription.occurred_error, response_request.status_code)


# def check_structure_lite(response_request, json_comparison):
#     if response_request.ok:
#         if response_request.json() == json_comparison:
#             return True
#         else:
#             return None
#     else:
#         return False


# def check_structure_lite_dict(response_request, json_comparison):
#     if response_request.ok:
#         if response_request.json() == json_comparison:
#             return {'result': 'true'}
#         else:
#             return {'result': 'error_struct'}
#     else:
#         return {'result': 'false'}


def check_structure_assert(response_request, json_comparison, type_request):
    assert response_request.ok, f'{type_request} {decription.occurred_error} {response_request.status_code}'
    assert response_request.json() == json_comparison, f'{type_request} {decription.struct_not_expected}'
    print(type_request + decription.request_ok + decription.response_ok)
    print(json_comparison)
