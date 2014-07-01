#Test cases definition

def test_case(set_up):
    driver = set_up.driver
    driver.get(set_up.base_url + "/")
    # Test all data