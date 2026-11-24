from services.markdown_parser import extract_markdown_blocks


def test_extract_markdown_blocks():
    with open("tests/fixtures/markdown/langs_comp.md", encoding="utf-8") as f:
        content = f.read()

    return extract_markdown_blocks(content)