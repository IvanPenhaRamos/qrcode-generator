import pytest
from qrcode_generator.url_validator import URLvalidator

def test_adds_https_when_missing():
    url = "google.com"
    result = URLvalidator(url)
    assert result == "https://google.com"

def test_invalid_url_raises_error():
    with pytest.raises(ValueError):
        URLvalidator("esto_no_es_una_url")

def test_valid_url_passes_unchanged():
    url = "https://github.com"
    result = URLvalidator(url)
    assert result == url
