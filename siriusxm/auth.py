from __future__ import unicode_literals

import logging
import weakref
#import keyring

import siriusxm
import siriusxm.user
import siriusxm.api

from siriusxm import serialized


__all__ = [
    'auth',
]


logger = logging.getLogger(__name__)


class auth(object):

    """If no ''config'' is provided, the default config is used."""

    @serialized
    def __init__(self, config=None):
        super(auth, self).__init__()

        if config is not None:
            self.config = config
        else:
            self.config = siriusxm.config()

        self._wrCache = weakref.WeakValueDictionary()

    _wrCache = None

    """A :class:`config` instance with the current configuration.

    Once the session has been created, changing the attributes of this object
    will generally have no effect."""
    config = None


    def login(self, username, password=None, remember_me=False):
        """Authenticate to Sirius XM internet radio.

        If you set ''remember_me'' to :class:`True`, the credientials will be
        stored using python's 'keyring' module which will use either:
        Mac OS X Keychain, Linux Secret Service, or Windows Credential Vault.
        You can later login to the same account without providing any
        ``username`` or credentials by calling :meth:`relogin`."""

        if password is not None:
            username = username.decode('utf_8')
        else:
            raise AttributeError('username is required to login')

        if password is not None:
            password = password.decode('utf_8')
        else:
            raise AttributeError('password is required to login')

        api = siriusxm.api(self.config)
        api.authenticate()

    @property
    def remembered_username(self):
        """The username of the remembered user from a previous :meth:`login` call."""
        return None

    def relogin(self):
        """Relogin as the remembered user.

        To be able do this, you must previously have logged in with
        :meth:`login` with the ``remember_me`` argument set to :class:`True`.

        To check what user you'll be logged in as if you call this method, see
        :attr:`remembered_user_name`."""
        pass

    def forget_me(self):
        """Forget the remembered user from a previous :meth:`login` call."""
        pass

    @property
    @serialized
    def username(self):
        """The logged in :class:`User`."""
        username = self.config.username
        if username is None:
            return None
        return siriusxm.user(username)

#this = auth()
