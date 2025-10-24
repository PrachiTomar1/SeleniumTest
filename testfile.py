import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Test case to validate search functionality on Selenium Playground website
def test_search_functionality():
    # Setup: Initialize WebDriver for Chrome
    driver = webdriver.Chrome()

    try:
        # Navigate to the Selenium Playground Table Search Demo page
        driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")

        # Locate the search box element and input the search term "New York"
        search_box = driver.find_element(By.ID, "task-table-filter")
        search_term = "New York"
        search_box.clear()
        search_box.send_keys(search_term)

        # Retrieve visible rows after the search
        rows = driver.find_elements(By.XPATH, "//table[@id='task-table']/tbody/tr")
        visible_rows = [row for row in rows if row.is_displayed()]

        # Assert that there are 5 visible rows
        assert len(visible_rows) == 5, f"Expected 5 visible entries, but found {len(visible_rows)}"

        print("Test Passed: Search functionality works as expected.")
    except Exception as e:
        pytest.fail(f"Test Failed: {str(e)}")
    finally:
        # Teardown: Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    pytest.main(["-v", "--tb=short", __file__])

