from datetime import date


class FormatError(Exception):
    print("Date n'est pas du format AAAA-MM-DD.")


class StringError(Exception):
    print("Date n'est pas un string !")


class ExpireError(Exception):
    print("L'aliment est déjà périmé !")


class ExpirationDate:
    def __init__(self, expiration_date: str):
        """Crée une date d'expiration.

                PRE : /
                POST : Un object de type date.
                RAISES : - StringError si expiration_date n'est pas un string.
                         - FormatError si expiration_date n'est pas un string de la forme AAAA-MM-DD.
                """
        if type(expiration_date) != str:
            raise StringError
        if len(expiration_date) != 10 or expiration_date[4] != "-" or expiration_date[7] != "-":
            raise FormatError
        self.expiration_date = date.fromisoformat(expiration_date)

    def get_date(self):
        """Renvoie le temps compris entre la date d'expiration et la date du jour.

                PRE : /
                POST : Un object de type date.
                RAISE: ExpireError si expiration_date est antérieure à celle du jour.
                """
        time = self.expiration_date - date.today()
        if date.today() > self.expiration_date:
            raise ExpireError
        return time

    def time_count(self):
        """Renvoie le nombre de jour restant avant la date de péremption.

        PRE : /
        POST : Un object de type int.
        """
        time_day = self.get_date().days
        return time_day
