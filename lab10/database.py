from __future__ import annotations
from typing import Optional

import psycopg2

from config import load_database_config, DatabaseConfig



class Database:
    connections: dict[DatabaseConfig, psycopg2.extensions.connection] = {}
    
    @staticmethod
    def connect(config: DatabaseConfig) -> Optional[psycopg2.extensions.connection]:
        """ Connect to the PostgreSQL database server """
        try:
            return psycopg2.connect(**config._asdict())
        except (psycopg2.DatabaseError, Exception) as error:
            print(f'Error connecting to the PostgreSQL server: {error}')
            return None

    def __init__(self, config: Optional[DatabaseConfig] = None, commit: bool = True):
        self.commit = commit
        
        if config is None:
            config = load_database_config()
        if config in Database.connections:
            self.conn = Database.connections[config]
        else:
            self.conn = self.connect(config)
            if self.conn is not None:
                self.connections[config] = self.conn

    def __enter__(self) -> tuple[psycopg2.extensions.connection, psycopg2.extensions.cursor]:
        return self.conn, self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.commit:
            self.conn.commit()