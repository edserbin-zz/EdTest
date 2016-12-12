import time
from tempmail import TempMail


# https://pypi.python.org/pypi/temp-mail
class TempEmail(object):
    def __init__(self):
        self.tm = TempMail()
        self.email = self.tm.get_email_address()

    def get_email_by_number(self, number_of_email):
        """
        interval of function checking mail
        if the interval will be to fast(small) like 0.5 seconds
        the server will return 429 error
        """
        delay = 5
        start_time = time.time()
        while True:
            time.sleep(delay)
            mail = self.tm.get_mailbox(self.email)
            current_time = time.time()
            end_time = current_time - start_time
            # if the letter doesnt come in 10 minutes function will return None
            if end_time > 600:
                print('Message hasn`t came more than 10 minutes')
                return None
            if isinstance(mail, list) and len(mail) == number_of_email:
                return mail[number_of_email - 1]
