"""
For the Win students should pass the tests for this file.
"""
import pytest
from webcode_tk import html_tools as html

project_dir = "project/"

min_required_elements = [
    ("figure", 4),
    ("img", 4),
    ("p", 7),
    ("ul or ol or dl", 3),
    ("li", 12)]

min_number_of_elements = html.get_number_of_elements_per_file(
    project_dir, min_required_elements
)

html_docs = html.get_all_html_files(project_dir)


@pytest.fixture
def html_files():
    html_files = html.get_all_html_files(project_dir)
    return html_files


@pytest.mark.parametrize("file,element,num", min_number_of_elements)
def test_for_html_exceeds_number_of_elements(file, element, num):
    if not html_files:
        assert False
    if "or" in element.lower():
        elements = element.split()
        actual = 0
        for el in elements:
            el = el.strip()
            actual += html.get_num_elements_in_file(el, file)
    else:
        actual = html.get_num_elements_in_file(element, file)
    assert actual >= num


@pytest.mark.parametrize("file", html_docs)
def test_for_dl_and_children(file):
    num_dl = html.get_num_elements_in_file("dl", file)
    if num_dl:
        num_dt = html.get_num_elements_in_file("dt", file)
        num_dd = html.get_num_elements_in_file("dd", file)
        assert num_dt >= 4 and num_dd >= 4
