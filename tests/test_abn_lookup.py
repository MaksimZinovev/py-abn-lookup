import time
import logging
from collections import namedtuple

# Constants
SEARCH_QUERY = "Automic"

# URL
BASE_URL = "https://abr.business.gov.au/"

# Web locators
SEARCH_BUTTON = "#MainSearchButton"
SEARCH_INPUT_FIELD = "#SearchText"
RESULTS_TABLE_ROWS = "#content-matching  tbody tr"

ExpectedResult = namedtuple("ExpectedResults", "abn_number status name type location")

# Expected results
automic_pty_ptd = ExpectedResult(
    abn_number="27 152 260 814",
    status="Active",
    name="AUTOMIC PTY LTD",
    type="Entity Name",
    location="2000 NSW",
)

automic_finance = ExpectedResult(
    abn_number="37 085 283 601",
    status="Active",
    name="AUTOMIC FINANCE PTY LTD",
    type="Entity Name",
    location="2000 NSW",
)

automic_legal = ExpectedResult(
    abn_number="80 147 418 942",
    status="Active",
    name="AUTOMIC LEGAL PTY LTD",
    type="Entity Name",
    location="2000 NSW",
)

automic_group = ExpectedResult(
    abn_number="27 152 260 814",
    status="Active",
    name="Automic Group",
    type="Business Name",
    location="2000 NSW",
)


# expected_results = [automic_pty_ptd]
expected_results = [automic_pty_ptd, automic_legal, automic_finance, automic_group]


def test_abn_lookup(py):
    """Verify search abn"""
    # GIVEN ABN lookup page has loade
    # WHEN user types search query into Search field
    # AND clicks search button
    # THEN results contain expected results, such as ABN number, Name, Type, Location

    py.visit(BASE_URL)
    py.get(SEARCH_INPUT_FIELD).should().be_visible().type(SEARCH_QUERY)
    py.get(SEARCH_BUTTON).should().be_clickable().click()
    search_results_rows = py.find(RESULTS_TABLE_ROWS)[1:]
    for expected_result in expected_results:
        assert len(search_results_rows) > 4
        assert any((expected_result.name in row.text()) for row in search_results_rows)

        found_row = py.contains(expected_result.name).parent()
        assert expected_result.abn_number in found_row.get("a").text()
        assert expected_result.status in found_row.get("span").text()
        assert found_row.contains(expected_result.name)
        assert found_row.contains(expected_result.type)
        assert expected_result.location in found_row.text()


ExpectedAbnDetails = namedtuple("ExpectedAbnDetails",
                                "entity_name abn_status entity_type business_location business_names")

automic_pty_ptd_details = ExpectedAbnDetails(
    entity_name="AUTOMIC PTY LTD",
    abn_status="Active from 19 Jun 2012",
    entity_type="Australian Private Company",
    business_location="NSW 2000",
    business_names=["CoSecPro", "Automic Group", "Invana", ]
)

ENTITY_TYPE = "//a[contains(text(), 'Australian Private Company')]"


def test_abn_details(py):
    """Verify search abn"""
    # GIVEN ABN lookup page with the results has loaded
    # WHEN user clicks on the ABN link
    # THEN user is redirected to the Current details for ABN page
    # AND ABN details match expected details

    py.visit(BASE_URL)
    py.get(SEARCH_INPUT_FIELD).should().be_visible().type(SEARCH_QUERY)
    py.get(SEARCH_BUTTON).should().be_clickable().click()

    found_row = py.contains(automic_pty_ptd.name).parent()
    found_row.get("[href]").should().be_clickable().click()
    assert py.url().endswith("27152260814")
    assert "Current details for ABN 27 152 260 814" in py.get("h1").text()

    assert automic_pty_ptd_details.entity_name in py.get("[itemprop='legalName']").text()
    assert automic_pty_ptd_details.abn_status in py.getx('//th[contains(text(), "ABN status")]').parent().text()
    assert automic_pty_ptd_details.entity_type in py.contains("Entity type:").parent().get("a").text()
    assert automic_pty_ptd_details.business_location in py.get("[itemprop='addressLocality']").text()
    for business_name in automic_pty_ptd_details.business_names:
        assert business_name in py.contains("Business name(s)").parent().text()





    time.sleep(2)
