from screens import (
    dashboard,
    landing,
    login,
    settings,
    signup,
    stock_details,
    stock_search,
    watchlist,
)

from utils.constants import *

ROUTES = {
    LANDING: landing.render,
    LOGIN: login.render,
    SIGNUP: signup.render,
    DASHBOARD: dashboard.render,
    STOCK_SEARCH: stock_search.render,
    STOCK_DETAILS: stock_details.render,
    WATCHLIST: watchlist.render,
    SETTINGS: settings.render,
}