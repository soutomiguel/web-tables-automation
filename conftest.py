from selenium import webdriver
import pytest
import json
import os

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action = "store",
        default = "prod",
        help = "Select environments using dev, stage or prod"
    )

@pytest.fixture
def environment(request):
    env = request.config.getoption("--env")
    env_file = os.path.join(os.path.dirname(__file__), 'envs', f'{env}.json')

    with open(env_file, 'r') as file:
        config = json.load(file)
        return config

@pytest.fixture
def driver(environment):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(environment["base_url"])
    yield driver
    driver.close()