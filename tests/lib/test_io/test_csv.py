import pytest

from servier.lib.io.csv import SourceCsv


@pytest.fixture
def input_csvfile_path(tmp_path):
    filepath = tmp_path / "test.csv"
    filepath.write_text("id,name\n1,DOLIPRANE", encoding="utf-8")
    return f"{filepath}"


def test_source_csv(input_csvfile_path):
    class Meds(SourceCsv):
        filepath: str = input_csvfile_path

    meds = Meds()
    meds.load()

    assert list(meds.data.columns) == ["id", "name"]
    assert meds.data.shape == (1, 2)
