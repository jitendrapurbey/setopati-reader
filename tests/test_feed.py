"""Tests for the reader.feed module"""
# Standard library imports
import os.path

# Third party imports
import pytest

# Reader imports
from reader import feed

# Current directory
HERE = os.path.dirname(__file__)


@pytest.fixture
def local_feed():
    """Use local file instead of downloading feed from web"""
    return os.path.join(HERE, "setopati_20190626.xml")


@pytest.fixture
def local_summary_feed():
    """Use local file instead of downloading feed from web"""
    return os.path.join(HERE, "setopati_descriptions_20190626.xml")


#
# Tests
#
def test_site(local_feed):
    """Test that we can read the site title and link"""
    expected = "The latest tutorials from Setopati – Nepal's Digital Newspaper (https://setopati.net)"
    assert feed.get_site(url=local_feed) == expected


def test_article_title(local_feed):
    """Test that title is added at top of article"""
    article_id = 0
    title = feed.get_titles(url=local_feed)[article_id]
    article = feed.get_article(article_id, url=local_feed)

    assert article.strip("# ").startswith(title)


def test_article(local_feed):
    """Test that article is returned"""
    article_id = 2
    article_phrases = [
        "logging.info('This is an info message')",
        "By using the `level` parameter",
        "  * `level`: The root logger",
    ]
    article = feed.get_article(article_id, url=local_feed)

    for phrase in article_phrases:
        assert phrase in article


def test_titles(local_feed):
    """Test that titles are found"""
    titles = feed.get_titles(url=local_feed)

    assert len(titles) == 20
    assert titles[0] == "Socialist lawmaker suspended for attending Free Tibet program calls suspension unfortunate"
    assert titles[9] == "Unreliable Trump confounds both foes and allies"


def test_summary(local_summary_feed):
    """Test that summary feeds can be read"""
    article_id = 1
    summary_phrases = [
        "Get the inside scoop",
        "this list of\ninformative videos",
    ]
    summary = feed.get_article(article_id, url=local_summary_feed)

    for phrase in summary_phrases:
        assert phrase in summary


def test_invalid_article_id(local_feed):
    """Test that invalid article ids are handled gracefully"""
    article_id = "wrong"
    with pytest.raises(SystemExit):
        feed.get_article(article_id, url=local_feed)
