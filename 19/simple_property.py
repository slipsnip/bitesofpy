from datetime import datetime, timedelta

NOW = datetime.now()


class Promo:
    def __init__(self, name_promotion, expires_datetime):
        self.name_promotion = name_promotion
        self.date_expires = expires_datetime

    @property
    def expired(self):
        return (self.date_expires - NOW).days <= 0
