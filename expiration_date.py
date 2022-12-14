from datetime import date


class ExpirationDate:
    def __init__(self, expiration_date: str):
        """Crée une date d'expiration.

                PRE : /
                POST : Deux object de type date
                RAISES : SyntaxError si expiration_date n'est pas un string de la forme AAAA-MM-DD
                """
        if expiration_date == "":
            self.expiration_date = date.today()
        else:
            self.expiration_date = date.fromisoformat(expiration_date)
        self.today = date.today()

    def get_date(self):
        """Renvoie le temps compris entre la date d'expiration et la date du jour.

                PRE : /
                POST : Un object de type date
                RAISES: ExpireError si expiration_date est antérieur à celle du jour
                """
        time = self.expiration_date - self.today
        return time

    def time_count(self):
        """Renvoie le nombre de jour restant avant la date de péremption.

        PRE : /
        POST : Un object de type int
        """
        time_day = self.get_date().days
        return time_day
