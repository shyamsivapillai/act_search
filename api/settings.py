import os

DEFAULT_DB_URI = "postgresql://postgres:1234@db:5432/legal_acts_db"

def get_settings():
    DB_URI = os.environ.get("ACT_SEARCH_DB_URI", DEFAULT_DB_URI)
    RESULT_PAGE_LIMIT = os.environ.get("RESULT_PAGE_LIMIT", 10)

    return {
        "DB_URI": DB_URI,
        "RESULT_PAGE_LIMIT": RESULT_PAGE_LIMIT
    }