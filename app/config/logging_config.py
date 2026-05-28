from loguru import logger
import sys
from pathlib import Path


LOG_DIR = Path("app/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level} | "
        "{message}"
    )
)

logger.add(
    LOG_FILE,
    rotation="10 MB",
    retention="14 days",
    compression="zip",
    level="INFO",
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level} | "
        "{name}:{function}:{line} | "
        "{message}"
    )
)


def get_logger():
    return logger
