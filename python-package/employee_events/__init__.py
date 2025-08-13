"""
Employee Events Package

This package helps you get information about employees and their performance!
Think of it like a smart assistant that can answer questions about workers.
"""

from .employee import Employee
from .team import Team
from .query_base import QueryBase
from .sql_execution import DatabaseMixin, database_query

__version__ = "1.0.0"
__all__ = ["Employee", "Team", "QueryBase", "DatabaseMixin", "database_query"]
