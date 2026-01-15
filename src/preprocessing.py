
import re
import pandas as pd


# Map raw CFPB product labels to project-level categories
PRODUCT_MAPPING = {
    # Credit card
    "Credit card": "Credit card",
    "Credit card or prepaid card": "Credit card",
    "Prepaid card": "Credit card",

    # Personal loan
    "Payday loan, title loan, or personal loan": "Personal loan",
    "Payday loan, title loan, personal loan, or advance loan": "Personal loan",
    "Consumer Loan": "Personal loan",
    "Payday loan": "Personal loan",
    "Vehicle loan or lease": "Personal loan",

    # Savings account
    "Checking or savings account": "Savings account",
    "Bank account or service": "Savings account",

    # Money transfers
    "Money transfer, virtual currency, or money service": "Money transfers",
    "Money transfers": "Money transfers",

    # Credit reporting
    "Credit reporting": "Credit reporting",
    "Credit reporting or other personal consumer reports": "Credit reporting",
    "Credit reporting, credit repair services, or other personal consumer reports": "Credit reporting",
}



BOILERPLATE_PATTERNS = [
    r"i am writing to file a complaint",
    r"this is a complaint regarding",
    r"i would like to report",
    r"i am filing a complaint",
]

def normalize_text(text) -> str:
    """
    Clean complaint narrative text for embedding quality.
    """
    # Case 1: real bytes
    if isinstance(text, bytes):
        text = text.decode("utf-8", errors="ignore")

    # Case 2: stringified bytes like "b'...'"
    if isinstance(text, str) and text.startswith("b'"):
        text = text[2:]  # remove leading b'
    
    if not isinstance(text, str):
        return ""

    text = text.lower()

    # Remove boilerplate phrases
    for pattern in BOILERPLATE_PATTERNS:
        text = re.sub(pattern, "", text)

    # Remove special characters (keep numbers)
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text



def filter_products(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter dataset to required products and map them to
    unified project-level product categories.
    """
    df = df.copy()

    # Keep only rows we know how to map
    df = df[df["Product"].isin(PRODUCT_MAPPING.keys())]

    # Map raw labels to clean categories
    df["Product"] = df["Product"].map(PRODUCT_MAPPING)

    return df



def remove_empty_narratives(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Keep only rows where narrative is NOT null
    df = df[df["Consumer complaint narrative"].notna()]

    # Strip whitespace
    df["Consumer complaint narrative"] = (
        df["Consumer complaint narrative"]
        .str.strip()
    )

    # Remove empty strings
    df = df[df["Consumer complaint narrative"] != ""]

    return df



def clean_narratives(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply text normalization to complaint narratives.
    """
    df = df.copy()
    df["cleaned_narrative"] = df["Consumer complaint narrative"].apply(normalize_text)
    return df
