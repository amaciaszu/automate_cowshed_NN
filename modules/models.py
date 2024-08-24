class Cow:
    def __init__(self, id, name, birthdate): # , birthdate
        self.id = id
        self.name = name
        self.birthdate = birthdate

class Measurement:
    def __init__(self, sensor_id, cow_id, timestamp, value):
        self.sensor_id = sensor_id
        self.cow_id = cow_id
        self.timestamp = timestamp
        self.value = value

class Sensor:
    def __init__(self, id, unit):
        self.id = id
        self.unit = unit