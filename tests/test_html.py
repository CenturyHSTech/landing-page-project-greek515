"""
Test for HTML requirements
"""
import pytest
import file_clerk.clerk as clerk
from webcode_tk import html_tools as html
from webcode_tk import validator_tools as validator

project_dir = "project/"
all_html_files = html.get_all_html_files(project_dir)

# List of required elements (per web page)
required_elements = [("doctype", 1),
                     ("html", 1),
                     ("head", 1),
                     ("title", 1),
                     ("body", 1),
                     ("h1", 1),
                     ("header", 1),
                     ("main", 1),
                     ("footer", 1)]

min_required_elements = [
    ("h2", 2),
    ("figure", 3),
    ("img", 3),
    ("nav", 1),
    ("a", 5),
    ("figcaption", 3),
    ("p", 5),
    ("ul or ol", 2),
    ("li", 7)]

exact_number_of_elements = html.get_number_of_elements_per_file(
    project_dir, required_elements
)
min_number_of_elements = html.get_number_of_elements_per_file(
    project_dir, min_required_elements
)
html_validation_results = validator.get_project_validation(project_dir)


@pytest.fixture
def html_files():
    html_files = html.get_all_html_files(project_dir)
    return html_files


def test_has_index_file(html_files):
    assert "project/index.html" in html_files


@pytest.mark.parametrize("file,element,num", exact_number_of_elements)
def test_files_for_exact_number_of_elements(file, element, num):
    if not html_files:
        assert False
    actual = html.get_num_elements_in_file(element, file)
    assert actual == num


@pytest.mark.parametrize("file,element,num", min_number_of_elements)
def test_files_for_minimum_number_of_elements(file, element, num):
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


@pytest.mark.parametrize("results", html_validation_results)
def test_passes_html_validation(results):
    assert "pass:" in results


def test_number_of_image_files_for_proficient():
    image_files = []
    image_files += clerk.get_all_files_of_type(project_dir, "jpg")
    image_files += clerk.get_all_files_of_type(project_dir, "png")
    image_files += clerk.get_all_files_of_type(project_dir, "gif")
    image_files += clerk.get_all_files_of_type(project_dir, "webp")
    image_files += clerk.get_all_files_of_type(project_dir, "svg")
    assert len(image_files) >= 3
