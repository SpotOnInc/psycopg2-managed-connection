try:
    from psycopg2cffi import compat
    compat.register()
except ImportError:
    pass

from .connection import ManagedConnection
