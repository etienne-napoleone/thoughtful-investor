from functools import wraps

from thoughtful_investor.handlers.errors import error
from thoughtful_investor.handlers import catchalls
from thoughtful_investor.handlers import commands

__all__ = ['catchalls', 'commands', 'error']
