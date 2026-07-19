from pydantic import BaseModel, Field


class AddWatchlistRequest(BaseModel):
    symbol: str = Field(
        ...,
        min_length=1,
        max_length=20,
        examples=["TCS"]
    )