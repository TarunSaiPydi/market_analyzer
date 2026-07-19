from fastapi import APIRouter, Depends
from app.dependencies.dashboard_dependencies import get_dashboard_service
from app.dependencies.security_dependencies import get_current_user
from app.services.dashboard_service import DashboardService
from app.utils.response_builders import success


router = APIRouter(
    prefix="/sma/v1",
    tags=["Dashboard"],
)


@router.get("/dashboard")
def get_dashboard(
    current_user=Depends(get_current_user),
    dashboard_service: DashboardService = Depends(get_dashboard_service),
):
    dashboard = dashboard_service.get_dashboard(current_user["id"])

    return success(
        message="Dashboard data retrieved successfully.",
        data=dashboard.model_dump(by_alias=True),
    )