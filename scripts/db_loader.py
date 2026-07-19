from typing import List, Tuple

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values


class DatabaseLoader:

    def __init__(
        self,
        host: str,
        port: int,
        database: str,
        user: str,
        password: str,
    ):
        self.connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
        )

    def load(self, df: pd.DataFrame):

        rows: List[Tuple] = []

        for _, row in df.iterrows():

            rows.append(
                (
                    row["SYMBOL"].strip(),
                    row["NAME OF COMPANY"].strip(),
                    "NSE",
                    row["SERIES"].strip(),
                    row["ISIN NUMBER"].strip(),
                    "INR",
                    "India",
                    True,
                )
            )

        query = """
        INSERT INTO stocks
        (
            symbol,
            company_name,
            exchange,
            series,
            isin,
            currency,
            country,
            is_active
        )
        VALUES %s

        ON CONFLICT(symbol)
        DO UPDATE
        SET

            company_name = EXCLUDED.company_name,

            exchange = EXCLUDED.exchange,

            series = EXCLUDED.series,

            isin = EXCLUDED.isin,

            updated_at = CURRENT_TIMESTAMP;
        """

        cursor = self.connection.cursor()

        execute_values(
            cursor,
            query,
            rows,
            page_size=500,
        )

        self.connection.commit()

        cursor.close()

    def close(self):

        self.connection.close()