"""
For the Win students should pass the tests for this file.
"""
import pytest
from webcode_tk import css_tools as css

project_dir = "project/"
advanced_properties_goals = {
        "figure": {
            "properties": ("box-shadow", "border-radius", "animation"),
            "min_required": 2,
        },
    }
advanced_properties_report = css.get_properties_applied_report(
    project_dir,
    advanced_properties_goals)


@pytest.mark.parametrize("results", advanced_properties_report)
def test_for_css_exceeds_advanced_properties_applied(results):
    assert "pass:" in results[:5]

expected_navbar_declarations = {
    "display: flex": False,
    "list-style-type: none": False,
    "display: block": False,
}
styles_by_files = css.get_styles_by_html_files(project_dir)
for row in styles_by_files:
    file = row.get("file")
    stylesheets = row.get("stylesheets")
    for sheet in stylesheets:
        for rule in sheet.rulesets:
            for item in expected_navbar_declarations.keys():
                item_no_spaces = ""
                item_split = item.split()
                if len(item_split) == 3:
                    item_no_spaces = item_split[0] + item_split[-1]
                text = rule._Ruleset__text
                if item in text:
                    expected_navbar_declarations[item] = True
                if item_no_spaces and item_no_spaces in text:
                    expected_navbar_declarations[item] = True
navbar_declarations = list(expected_navbar_declarations.items())


@pytest.mark.parametrize("expected,found", navbar_declarations)
def test_essential_navbar_styles(expected, found):
    if found:
        assert expected
    else:
        assert False
