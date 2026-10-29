import pytest

from estatistica_eng.medidas import media_amostral


def test_media_amostral() -> None:
    assert media_amostral([2, 4, 6]) == pytest.approx(4.0)


def test_media_amostral_vazia() -> None:
    with pytest.raises(ValueError):
        media_amostral([])
