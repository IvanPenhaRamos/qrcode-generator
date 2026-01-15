import pytest
from qrcode_generator.domain.url_validator import URL_validator

def test_valid_url():
    url, name = URL_validator("google.com")
    assert url == "https://google.com"
    assert name == "google.com"

def test_invalid_url():
    with pytest.raises(ValueError):
        URL_validator("esto no es una url")
