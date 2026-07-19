from scripts.csv_reader import CSVReader
from scripts.db_loader import DatabaseLoader

from app.config import settings
from app.logger import logger


def main():

    logger.info("Reading NSE equity CSV...")

    reader = CSVReader()

    df = reader.read(
        "scripts/sample_data/EQUITY_L.csv"
    )

    logger.info("Total records : %d", len(df))

    loader = DatabaseLoader(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
    )

    logger.info("Loading data into PostgreSQL...")

    loader.load(df)

    loader.close()

    logger.info("Master stock import completed successfully.")


if __name__ == "__main__":
    main()