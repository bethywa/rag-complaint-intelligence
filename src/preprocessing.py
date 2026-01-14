
import re
import pandas as pd


REQUIRED_PRODUCTS = {
    "Credit card",
    "Personal loan",
    "Savings account",
    "Money transfers",
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
    Keep only complaints related to required products.
    """
    df = df.copy()
    df["Product"] = df["Product"].str.strip()
    return df[df["Product"].isin(REQUIRED_PRODUCTS)]


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
