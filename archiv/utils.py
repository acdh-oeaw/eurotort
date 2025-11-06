from io import BytesIO

import pandas as pd
import requests


def gsheet_to_df(sheet_id: str) -> pd.DataFrame:
    """Converts a Google Sheet to a pandas DataFrame.
    This function takes a Google Sheet ID and returns the sheet's content as a pandas DataFrame.
    The sheet must be publicly accessible or have appropriate sharing settings.
    Args:
        sheet_id (str): The ID of the Google Sheet. This can be found in the sheet's URL between
            /d/ and /edit.
    Returns:
        pd.DataFrame: A pandas DataFrame containing the sheet's data.
    Raises:
        requests.exceptions.RequestException: If there's an error fetching the sheet.
        pd.errors.EmptyDataError: If the sheet is empty or contains no valid data.
    Example:
        >>> sheet_id = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
        >>> df = gsheet_to_df(sheet_id)
    """

    GDRIVE_BASE_URL = "https://docs.google.com/spreadsheet/ccc?key="
    url = f"{GDRIVE_BASE_URL}{sheet_id}&output=csv"
    r = requests.get(url)
    print(r.status_code)
    data = r.content
    df = pd.read_csv(BytesIO(data))
    return df
