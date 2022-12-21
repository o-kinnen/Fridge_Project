from datetime import date


class FormatError(Exception):
    """Date is not YYYY-MM-DD."""
    pass


class StringError(Exception):
    """Date is not a string!"""
    pass


class ExpireError(Exception):
    """The food is already expired!"""
    pass


class ExpirationDate:
    """Class representing expiration date.

        Author : Olivia Kinnen.
        Date : December 2022.
        This class defines how many days are left before a food is expired.
        """
    def __init__(self, expiration_date: str):
        """Creates an expiry date.

                PRE : /
                POST : An object of type date.
                RAISES : - StringError if expiration_date is not a string.
                         - FormatError if expiration_date is not a string of the form AAAA-MM-DD.
                """
        if type(expiration_date) != str:
            raise StringError
        if len(expiration_date) != 10 or expiration_date[4] != "-" or expiration_date[7] != "-":
            raise FormatError
        self.expiration_date = date.fromisoformat(expiration_date)

    def get_date(self):
        """Returns the time between the expiry date and today’s date.

                PRE : /
                POST : An object of type date.
                RAISE: ExpireError if expiration_date is earlier than the current one.
                """
        time = self.expiration_date - date.today()
        if date.today() > self.expiration_date:
            raise ExpireError
        return time

    def time_count(self):
        """Returns the number of days remaining before the expiry date.

        PRE : /
        POST : An object of type int.
        """
        time_day = self.get_date().days
        return time_day

