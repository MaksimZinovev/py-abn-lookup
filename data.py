from collections import namedtuple


# Constants
ABN_DETAILS_PAGE_H1 = "Current details for ABN 27 152 260 814"

# URL
BASE_URL = "https://abr.business.gov.au/"

# Web locators
# Search results page
SEARCH_BUTTON = "#MainSearchButton"
SEARCH_INPUT_FIELD = "#SearchText"
RESULTS_TABLE_ROWS = "#content-matching  tbody tr"

# ABN details page
LOCATION = "[itemprop='addressLocality']"
ENTITY_NAME = "[itemprop='legalName']"
SEARCH_QUERY = "Automic"

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

expected_results = [automic_pty_ptd, automic_legal, automic_finance, automic_group]
ExpectedAbnDetails = namedtuple("ExpectedAbnDetails",
                                "entity_name abn_status entity_type business_location business_names abn_number")
automic_pty_ltd_details = ExpectedAbnDetails(
    entity_name="AUTOMIC PTY LTD",
    abn_status="Active from 19 Jun 2012",
    entity_type="Australian Private Company",
    business_location="NSW 2000",
    business_names=["CoSecPro", "Automic Group", "Invana", ],
    abn_number="27152260814",
)
