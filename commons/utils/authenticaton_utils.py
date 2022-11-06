from django.contrib.auth.tokens import PassWordResetTokenGenerator
import six

class PassWordGenerator(PassWordResetTokenGenerator):
    # def _make_hash_value(self,user, timestamp):
    #     return str(user.id) + str(timestamp)+user.
    pass