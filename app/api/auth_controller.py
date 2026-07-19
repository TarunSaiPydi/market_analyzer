"""
Authentication Controller

Exposes authentication related REST APIs.
"""

from fastapi import APIRouter, Request, status, Depends

from app.models.request_models import LoginRequest, SignupRequest

from app.dependencies.auth_dependencies import get_auth_service

from app.logger import logger
from app.services.auth_service import AuthService
from app.models.response_models import ApiResponse
from app.dependencies.security_dependencies import get_current_user
from app.utils.response_builders import success

router = APIRouter(
    prefix="/sma/v1",
    tags=["Authentication"]
)

# Signup

@router.post(
    "/signup",
    summary="Register User",
    description="Create a new user account.",
    response_model=ApiResponse,
    status_code=status.HTTP_201_CREATED
)
async def signup(credentials: SignupRequest, auth_service: AuthService = Depends(get_auth_service)):
    """
    Register a new application user.
    """

    return auth_service.signup(credentials)


# ---------------------------------------------------------
# Login
# ---------------------------------------------------------

@router.post("/login",
            summary="Authenticate User",
            description="Authenticate a registered user using username and password.",
            response_model=ApiResponse,
            status_code=status.HTTP_200_OK)
async def login(credentials: LoginRequest, request: Request, auth_service: AuthService = Depends(get_auth_service)):
    """
    Authenticate application user.
    """

    client_ip = (
        request.client.host
        if request.client
        else "Unknown"
    )

    return auth_service.login(
        credentials,
        client_ip
    )

# User related Endpoints

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return {
        "message": "Authenticated successfully",
        "user": current_user,
    }

@router.get("/me")
def get_profile(current_user=Depends(get_current_user)):
    return success(
        message="Profile fetched successfully.",
        data=current_user
    )