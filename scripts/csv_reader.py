from pathlib import Path

import pandas as pd


class CSVReader:

    REQUIRED_COLUMNS = [
        "SYMBOL",
        "NAME OF COMPANY",
        "SERIES",
        "ISIN NUMBER",
    ]

    def read(self, file_path: str) -> pd.DataFrame:
        df = pd.read_csv(file_path)

        df.columns = df.columns.str.strip()

        missing = [
            column
            for column in self.REQUIRED_COLUMNS
            if column not in df.columns
        ]

        if missing:
            raise ValueError(
                f"Missing columns: {missing}"
            )

        df = df[self.REQUIRED_COLUMNS]

        df = df.fillna("")

        return df


if __name__ == "__main__":
    reader = CSVReader()

    df = reader.read(
        Path("sample_data") / "EQUITY_L.csv"
    )

    print(df.head())