from watch import parse
import pytest


def main():
    test_youtube_link()


def test_http_s_www_youtube_link():
    assert (
        parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>')
        == "https://youtu.be/xvFZjo5PgG0"
    )
    assert (
        parse(
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        )
        == "https://youtu.be/xvFZjo5PgG0"
    )


def test_http_s_youtube_link():
    assert (
        parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>')
        == "https://youtu.be/xvFZjo5PgG0"
    )
    assert (
        parse(
            '<iframe width="560" height="315" src="https://youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        )
        == "https://youtu.be/xvFZjo5PgG0"
    )


def test_no_youtube_link():
    assert (
        parse(
            '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
        )
        == None
    )


if __name__ == "__main__":
    main()
