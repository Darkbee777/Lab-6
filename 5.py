class request(object):
    def __init__(self):
        self.__count_of_failures = 0
        self.__sended_successfully = False

    def can_retry(self):
        if self.__count_of_failures >= 10:
            return False
        else:
            return True

    def retry(self):
        if self.__sended_successfully or not self.can_retry():
            return False
        self.__sended_successfully = True
        return self.retry()
