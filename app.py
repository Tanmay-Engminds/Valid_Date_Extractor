import re
from datetime import date
from typing import List, Tuple
#Month name matching (case-insensitive)
_MONTH_MAP = {
    "jan": 1, "january": 1,
    "feb": 2, "february": 2,
    "mar": 3, "march": 3,
    "apr": 4, "april": 4,
    "may": 5,
    "jun": 6, "june": 6,
    "jul": 7, "july": 7,
    "aug": 8, "august": 8,
    "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "october": 10,
    "nov": 11, "november": 11,
    "dec": 12, "december": 12,
}
#Regex patterns
#Using verbose for readability
#ISO style: YYYY-MM-DD
ISO_PATTERN = re.compile(
    r"""
    (?P<year>(19|20)\d{2})-  #Year:1900-2099
    (?P<month>0[1-9]|1[0-2])- #Month:01-12
    (?P<day>0[1-9]|[12]\d|3[01]) #Day:01-31
    """,
    re.VERBOSE,
)
#Slash style: DD/MM/YYYY
SLASH_PATTERN = re.compile(
    r"""
    (?P<day>0[1-9]|[12]\d|3[01])/ #Day:01-31
    (?P<month>0[1-9]|1[0-2])/     #Month:01-12
    (?P<year>(19|20)\d{2})        #Year:1900-2099
    """,
    re.VERBOSE,
)
#Long style: Month DD, YYYY
LONG_PATTERN = re.compile(
    r"""
    (?P<month_name>[A-Za-z]{3,9})   #Months
    \s+                             #spaces
    (?P<day>\d{1,2})                #day: 1/2 digits
    \s*,\s*                         #If there are spaces
    (?P<year>(19|20)\d{2})          #year: 1900–2099
    """,
    re.VERBOSE,
)
#Checking
def _is_valid_date(year: int, month: int, day: int) -> bool:
    if not (1900 <= year <= 2099): #Returns true if it is valid date
        return False
    try:
        date(year, month, day)
    except ValueError:
        return False
    return True
def _extract_iso(text: str) -> List[Tuple[int, str]]:
    results = []
    for m in ISO_PATTERN.finditer(text):
        y = int(m.group("year"))
        mth = int(m.group("month"))
        d = int(m.group("day"))
        if _is_valid_date(y, mth, d):
            results.append((m.start(), m.group(0)))
    return results
def _extract_slash(text: str) -> List[Tuple[int, str]]:
    results = []
    for m in SLASH_PATTERN.finditer(text):
        d = int(m.group("day"))
        mth = int(m.group("month"))
        y = int(m.group("year"))
        if _is_valid_date(y, mth, d):
            results.append((m.start(), m.group(0)))
    return results
def _extract_long(text: str) -> List[Tuple[int, str]]:
    results = []
    for m in LONG_PATTERN.finditer(text):
        month_name_raw = m.group("month_name")
        month_name = month_name_raw.lower()
        month = _MONTH_MAP.get(month_name)
        if month is None:
            #For not a valid month name
            continue
        d = int(m.group("day"))
        y = int(m.group("year"))
        if _is_valid_date(y, month, d):
            # Keep original spacing/case as in input
            results.append((m.start(), m.group(0).strip()))
    return results
def extract_valid_dates(text: str) -> List[str]:
    """
    Extract all valid dates in supported formats from a text string.
    Supported formats:
      - YYYY-MM-DD
      - DD/MM/YYYY
      - Month DD, YYYY
      - Mon DD, YYYY
    """
    candidates: List[Tuple[int, str]] = []
    candidates += _extract_iso(text)
    candidates += _extract_slash(text)
    candidates += _extract_long(text)
    # Sort based on original position
    candidates.sort(key=lambda x: x[0])
    return [c[1] for c in candidates]
def extract_valid_dates_from_file(path: str, encoding: str = "utf-8") -> List[str]:
    """
    Read the entire file and extract valid dates from its contents.
    """
    with open(path, "r", encoding=encoding) as f:
        content = f.read()
    return extract_valid_dates(content)
if __name__ == "__main__":
    #File Path
    file_path = r"path_to_file.txt"
    dates = extract_valid_dates_from_file(file_path)
    for d in dates:

        print(d)
