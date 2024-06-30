import pytest
import requests
import jsonschema

from src.assertions.asserions_schema import assert_schemas
from src.singleton import Singleton


@pytest.mark.smoke
def test_CG_06_TC1_GET_verificar_obtencion_exitosa_de_un_customer_group_por_id(get_token_login):
    group_id = 1

    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/{group_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers)
    response_data = response.json()
    assert response.status_code == 200

def test_esquema_verificar_obtencion_exitosa_de_un_customer_group_por_id(get_body_of_obtain_customer_group_by_id):
    response_data = get_body_of_obtain_customer_group_by_id
    assert_schemas(response_data, 'get_customer_group.json')

