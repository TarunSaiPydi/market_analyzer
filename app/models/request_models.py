"""
Request DTOs (Data Transfer Objects)

These models define the payload expected by the API.
"""

from pydantic import BaseModel, EmailStr, Field


class SignupRequest(BaseModel):
    """
    User registration request.
    """

    user_name: str = Field(
        ...,
        min_length=3,
        max_length=30,
        description="Unique username"
    )

    email_id: EmailStr

    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        description="User password"
    )


class LoginRequest(BaseModel):
    """
    User login request.
    """

    user_name: str = Field(
        ...,
        min_length=3,
        max_length=30
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

