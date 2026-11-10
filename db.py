"""Shared MySQL connection for HotelierPro.

Connection settings come from environment variables so no credentials live in the code:
  HOTELIER_DB_HOST      (default: localhost)
  HOTELIER_DB_USER      (default: root)
  HOTELIER_DB_PASSWORD  (required)
  HOTELIER_DB_NAME      (default: dbmspackage)
"""
import os

import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host=os.environ.get("HOTELIER_DB_HOST", "localhost"),
        user=os.environ.get("HOTELIER_DB_USER", "root"),
        password=os.environ.get("HOTELIER_DB_PASSWORD", ""),
        database=os.environ.get("HOTELIER_DB_NAME", "dbmspackage"),
    )
