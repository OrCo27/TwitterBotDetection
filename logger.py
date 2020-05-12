import time

class Log:
    def __init__(self, log_method):
        self.log_method = log_method
        self.disabled = False

    def disable_log(self):
        self.disabled = True

    def enable_log(self):
        self.disabled = False

    def write_log(self, description, title=None):
        if self.disabled:
            return

        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("[%m/%d/%Y %H:%M:%S] -", named_tuple)

        if title is not None:
            line_log = str.format(f'-- {time_string} [{title.upper()}] - {description}')
        else:
            line_log = str.format(f'-- {time_string} {description}')

        self.log_method(line_log)