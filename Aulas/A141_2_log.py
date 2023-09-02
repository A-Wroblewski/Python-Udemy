from pathlib import Path

LOG_FILE = Path(__file__).parent / 'A141_3_log.txt'

class Log:  # abstração
    def _log(self, message):  # assinatura do método
        raise NotImplementedError('Implement the log method.')

    def log_success(self, message):
        return self._log(f'Success: {message}')

    def log_error(self, message):
        return self._log(f'Error: {message}')


class LogFileMixin(Log):  # mixin indica que essa classe serve para adicionar funcionalidades dentro de outras classes numa herança múltipla
    def _log(self, message):
        formatted_message = f'{message} ({self.__class__.__name__})'

        print('Sending to log:', formatted_message)

        with open(LOG_FILE, 'a') as file:
            file.write(formatted_message)
            file.write('\n')


class LogPrintMixin(Log):
    def _log(self, message):
        print(f'{message} ({self.__class__.__name__})')


if __name__ == '__main__':
    # log = Log()  # classe Log levanta um erro pois não é para ser usada
    # log._log('x')

    log_print = LogPrintMixin()
    log_print.log_success('message success')
    log_print.log_error('message error')

    log_file = LogFileMixin()
    log_file.log_success('message success')
    log_file.log_error('message error')
