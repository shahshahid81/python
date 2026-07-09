from enum import Enum


class TrafficLight(Enum):
    RED = 1
    ORANGE = 2
    GREEN = 3

    def next_light(current_light):
        if current_light == TrafficLight.RED:
            return TrafficLight.GREEN
        elif current_light == TrafficLight.GREEN:
            return TrafficLight.ORANGE
        elif current_light == TrafficLight.ORANGE:
            return TrafficLight.RED


red = TrafficLight(1)
orange = TrafficLight(2)
green = TrafficLight(3)
print(red, red.name, red.value)
print(TrafficLight.next_light(red))
print(TrafficLight.next_light(green))
print(TrafficLight.next_light(orange))


class HTTPStatus(Enum):
    OK = 200
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503
