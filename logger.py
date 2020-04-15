import time

class Log:
    def __init__(self, log_method):
        self.log_method = log_method

    def write_log(self, description, title=None, timestamp=True):
        named_tuple = time.localtime()  # get struct_time

        if timestamp:
            time_string = time.strftime("[%m/%d/%Y %H:%M:%S] -", named_tuple)
        else:
            time_string = ""

        if title is not None:
            line_log = str.format(f'-- {time_string} [{title.upper()}] - {description}')
        else:
            line_log = str.format(f'-- {time_string} {description}')

        self.log_method(line_log)