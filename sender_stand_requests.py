import requests
import configuration
import data


def post_new_order():
     return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=data.order)
#print(post_new_order().json())

def get_track(new_order_track):
    track_number = configuration.GET_ORDER + "?t=" + str(new_order_track)
    return requests.get(configuration.URL_SERVICE + track_number)
#print(get_track(new_order_track=584443))