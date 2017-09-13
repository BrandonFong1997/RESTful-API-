from voluptuous import Schema, Optional, Required, Length, All

class Validator:
    _car_schema = Schema({
        Required('id'): All(str, Length(min=24, max=24)),
    })

    _car_put_schema = Schema({
        Optional('make'): All(str, Length(max=20)),
        Optional('model'): All(str, Length(max=20)),
        Optional('colour'): All(str, Length(max=15)),
    })

    _car_post_schema = Schema({
        Required('make'): All(str, Length(max=20)),
        Required('model'): All(str, Length(max=20)),
        Required('colour'): All(str, Length(max=15)),
    })

    @classmethod
    def validate_get(cls, data):
        return cls._car_schema(data)

    @classmethod
    def validate_put(cls, data):
        return cls._car_put_schema(data)

    @classmethod
    def validate_post(cls, data):
        return cls._car_post_schema(data)
