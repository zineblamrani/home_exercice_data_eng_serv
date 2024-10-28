import re


def tokenize_unique(df_col):
    """
    Tokenise values of column in dataframe.

    Args:
    df_col: Series pandas of text

    Returns:
        New Series which text tokens in an list
    """
    return df_col.apply(lambda text: set(re.findall(r"\b\w+\b", text.upper())))
