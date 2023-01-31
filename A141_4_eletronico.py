from A141_2_log import LogFileMixin

class Electronic:
    def __init__(self, name):
        self._name = name
        self._is_on = False

    def turn_on(self):
        if not self._is_on:
            self._is_on = True

    def turn_off(self):
        if self._is_on:
            self._is_on = False

class Smartphone(Electronic, LogFileMixin):
    def turn_on(self):
        super().turn_on()

        if self._is_on:
            message = f'{self._name} is on.'

            self.log_success(message)

    def turn_off(self):
        super().turn_off()

        if not self._is_on:
            message = f'{self._name} is off.'

            self.log_error(message)
