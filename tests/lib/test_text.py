import pandas as pd

from servier.lib.text import tokenize_unique


def test_tokenize_unique():
    df_input = pd.DataFrame([{"text": "Hello world, how are you ? how are you ?"}])
    df_input["tokens"] = tokenize_unique(df_input["text"])
    assert df_input.iloc[0].tokens == set(["HELLO", "WORLD", "HOW", "ARE", "YOU"])
