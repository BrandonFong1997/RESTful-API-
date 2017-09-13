from voluptuous import Schema, Optional, Required, Length, All

class Validator:
    _car_schema = Schema({
        Required('id'): All(str, Length(min=24, max=24)),
    })

    @classmethod
    def validate_get(cls, data):
        return cls._car_schema(data)
