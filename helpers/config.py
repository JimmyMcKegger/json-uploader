from dotenv import dotenv_values
from typing import Tuple
import logging
import coloredlogs


def get_logger() -> logging.Logger:
    """
    This function is responsible for setting up the logger.
    It returns the logger.
    """
    logger = logging.getLogger(__name__)
    # custom format.
    field_styles = coloredlogs.DEFAULT_FIELD_STYLES
    level_styles = coloredlogs.DEFAULT_LEVEL_STYLES
    fmt = "%(asctime)s %(levelname)s %(message)s"

    coloredlogs.install(
        level="INFO",
        logger=logger,
        fmt=fmt,
        field_styles=field_styles,
        level_styles=level_styles,
    )

    if not logger.handlers:
        logger.addHandler(logging.StreamHandler())
    return logger


def get_api_settings() -> Tuple[str, dict]:
    """
    This function is responsible for setting up the configuration required for the API.
    It reads the required values from the .env file and constructs the URL and headers.
    It returns these two values.
    """
    config = dotenv_values(".env")

    shop = config["SHOP"]
    api_version = config["API_VERSION"]
    url = f"https://{shop}/admin/api/{api_version}/graphql.json"
    link = f"https://admin.shopify.com/store/{shop[:-14]}/content/files"
    headers = {
        "X-shopify-access-token": config["API_ACCESS_TOKEN"],
        "Content-Type": "application/json",
    }

    return url, link, headers
