from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel
from services.user_service import login, sign_up
from services.dashboard_service import add_watchlist, dashboard_index_data, remove_watchlist_ticker, see_watchlist_data, watchlist_ticker_related_news
from utils.get_ticker_data import ticker_data
from utils.database import get_connection
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

app = FastAPI()

# Allow your local React development server to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger("MarketAnalyzer")


@app.get("/")
def greet():
    return "Market Analyzer"

# ---------------------- Models ---------------------- #

class WatchlistItem(BaseModel):
    user_id: int
    symbol: str

class SignupRequest(BaseModel):
    user_name: str
    email_id: str
    password: str

class LoginRequest(BaseModel):
    user_name: str
    password: str

@app.post("/sma/v1/dashboard/add_to_watchlist")
def add_to_watchlist(item: WatchlistItem):
    ticker_sym = item.symbol.upper().strip()
    
    # data = ticker_data(ticker_sym)
    # if data.empty:
    #     raise HTTPException(status_code=400, detail=f"Invalid Symbol '{ticker_sym}'. Data not found.")
    
    return add_watchlist(item.user_id, ticker_sym)

@app.delete("/api/watchlist")
def remove_from_watchlist(item: WatchlistItem):
    ticker_sym = item.symbol.upper().strip()
    
    data = remove_watchlist_ticker(item.user_id, ticker_sym)
    return data

@app.get("/sma/v1/dashboard/watchlist/{user_id}")
def get_watchlist(user_id: int):
    print(user_id)
    return see_watchlist_data(user_id)
    


@app.get("/sma/v1/dashboard")
def dashboard():
    # print(False if dashboard_index_data[0]==None else True)
    _indexes = dashboard_index_data(["^NSEI", "^BSESN", "^NSEBANK", "^CNXIT", "NIFTY_FIN_SERVICE.NS"])

    watchlist = get_watchlist(1)
    Watchlist_items = watchlist["Watchlist_items"]

    ticker_news = watchlist_ticker_related_news(["^NSEI", "TCS.ns", "AAPL"])

    return {
        "watchlist": Watchlist_items,
        "indexValues": _indexes,
        "news": ticker_news
    }

# ---------------------- Signup ---------------------- #

@app.post("/sma/v1/signup", status_code=status.HTTP_201_CREATED)
async def user_signup(credentials: SignupRequest):
    """
    Register a new user account.
    """

    logger.info(
        "Signup request received | Username=%s | Email=%s",
        credentials.user_name,
        credentials.email_id
    )

    try:

        response = sign_up(credentials)

        if response.get("status") == "success":

            logger.info(
                "Signup successful | Username=%s",
                credentials.user_name
            )

            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content=response
            )

        logger.warning(
            "Signup failed | Username=%s | Reason=%s",
            credentials.user_name,
            response.get("message", "Unknown")
        )

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=response
        )

    except ValueError as ex:

        logger.warning(
            "Signup validation failed | Username=%s | Error=%s",
            credentials.user_name,
            str(ex)
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex)
        )

    except HTTPException:
        raise

    except Exception:

        logger.exception(
            "Unexpected error during signup | Username=%s",
            credentials.user_name
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to process signup request."
        )


# --------------------------------------------------------------------
# Login API
# --------------------------------------------------------------------

@app.post("/sma/v1/login", status_code=status.HTTP_200_OK)
async def user_login(
    credentials: LoginRequest,
    request: Request
):
    """
    Authenticate application user.
    """

    client_ip = request.client.host if request.client else "Unknown"

    logger.info(
        "Login attempt | Username=%s | ClientIP=%s",
        credentials.user_name,
        client_ip
    )

    try:

        response = login(
            credentials=credentials,
            client_ip=client_ip
        )

        if response.get("status") == "success":

            logger.info(
                "Login successful | Username=%s | ClientIP=%s",
                credentials.user_name,
                client_ip
            )

            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=response
            )

        logger.warning(
            "Authentication failed | Username=%s | ClientIP=%s | Reason=%s",
            credentials.user_name,
            client_ip,
            response.get("message", "Invalid credentials")
        )

        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=response
        )

    except ValueError as ex:

        logger.warning(
            "Login validation failed | Username=%s | ClientIP=%s | Error=%s",
            credentials.user_name,
            client_ip,
            str(ex)
        )

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(ex)
        )

    except HTTPException:
        raise

    except Exception:

        logger.exception(
            "Unexpected error during login | Username=%s | ClientIP=%s",
            credentials.user_name,
            client_ip
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error."
        )

#------------------Signup-----------------------

# @app.post("/sma/v1/signup")
# def user_signup(credentials: SignupRequest):
#     response = sign_up(credentials)

#     print(response)
#     return response

# @app.post("/sma/v1/login")
# def user_login(credentials: LoginRequest, request: Request):
#     ip_addr = request.client.host if request.client else "127.0.0.1"
#     response = login(credentials, client_ip=ip_addr)

#     return response


