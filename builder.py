class mech:
    def init(self, torso):
        self.servos = [torso]
        self.total_cp = torso.cp
        self.total_weight = torso.weight

    def add_servo(self, servo):
        self.servos += servo
        self.total_cp += servo.cp
        self.total_weight += servo.wight

    def remove_servo(self, name):
        for servo in self.servos:
            if servo.name == name:
                self.servos.remove(servo)
                self.total_cp -= servo.cp
                self.total_weight -= servo.wight
                break

class servo:

