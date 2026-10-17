import requests
import configuration
import data


def create_order():
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=data.order_body,
        timeout=30
    )


def get_order(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
        params={"t": track},
        timeout=30
    )
