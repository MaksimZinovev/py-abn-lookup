from data import *


def test_abn_lookup(py):
    """Verify search abn"""
    # GIVEN ABN lookup page has loaded
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


def test_abn_details(py):
    """Verify Current details for ABN page"""
    # GIVEN ABN lookup page with the results has loaded
    # WHEN user clicks ABN link
    # THEN user is redirected to the Current details for ABN page
    # AND ABN details match expected details

    py.visit(BASE_URL)
    py.get(SEARCH_INPUT_FIELD).should().be_visible().type(SEARCH_QUERY)
    py.get(SEARCH_BUTTON).should().be_clickable().click()

    found_row = py.contains(automic_pty_ptd.name).parent()
    found_row.get("[href]").should().be_clickable().click()

    assert py.url().endswith(automic_pty_ltd_details.abn_number)
    assert ABN_DETAILS_PAGE_H1 in py.get("h1").text()

    assert automic_pty_ltd_details.entity_name in py.get(ENTITY_NAME).text()
    assert automic_pty_ltd_details.abn_status in py.contains("ABN status:").parent().get("td").text()
    assert automic_pty_ltd_details.entity_type in py.contains("Entity type:").parent().get("a").text()
    assert automic_pty_ltd_details.business_location in py.get(LOCATION).text()
    for business_name in automic_pty_ltd_details.business_names:
        assert business_name in py.contains("Business name(s)").parent().text()
