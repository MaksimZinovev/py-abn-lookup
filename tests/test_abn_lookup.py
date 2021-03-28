import time
import logging
from collections import namedtuple

# Constants
SEARCH_QUERY = "Automic"

# URL
BASE_URL = "https://abr.business.gov.au/"

# Web locators
SEARCH_BUTTON = "#MainSearchButton"

expected_result = namedtuple("ExpectedResults", "abn_number name type location")




def test_abn_lookup(py):
    """Verify search abn"""
    # GIVEN ABN lookup page has loade
    # WHEN user types search query into Search field
    # AND clicks search button
    # THEN results should be relevant to search query

    py.visit(BASE_URL)
    py.get("#SearchText").should().be_visible().type(SEARCH_QUERY)

    py.get(SEARCH_BUTTON).should().be_clickable().click()

    result_rows = py.find("#content-matching  tbody tr ")[1:30]
    abn_col_elements = py.find("#content-matching a")

    assert len(abn_col_elements) > 3

    logging.info(f"row 1: {result_rows[1].get('a').text()}")

    # Row 1
    # assert "27 152 260 814" in result_rows[1].get("a").text()
    # assert "Active" in result_rows[1].get("span").text()
    # assert "AUTOMIC PTY LTD" in result_rows[1].contains("AUTOMIC PTY LTD").text()
    # assert "Entity Name" in result_rows[1].contains("Entity Name").text()

    r1 = ("27 152 260 814", "Active", "AUTOMIC PTY LTD", "Entity Name",)

    assert any(row.get("a").text() == r1[0] for row in result_rows)

    for row in result_rows:
        if row.get("a").text() == r1[0]:
            assert "Active" in row.get("span").text()
            assert "AUTOMIC PTY LTD" in row.contains("AUTOMIC PTY LTD").text()
            assert "Entity Name" in row.contains("Entity Name").text()
            break






    time.sleep(2)
