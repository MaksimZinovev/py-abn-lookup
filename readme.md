

![](img/abn_lookup_page.png)

# ABN Lookup: Automated Web UI Tests

> This repository contains examples of  automated  web UI tests  built using Selenium, Python and Pyleniumio 

**Tests :**

- **TC-1** 

  - Steps:
    - Open browser and navigate to https://abr.business.gov.au/
    - Type" Automic" in the lookup field

  - Expected:
    - The search results shall contain
    - ![search_results](img/search_results.png)



- TC-2
  - Steps:

    - Execute TC-1

    - Click on link “27 152 260 814”

      

  - Expected:

    - ABN details should contain
    - ![abn_details](img/abn_details.png)



## Installation

Installation includes the following steps:

1. Clone repo.

2. Create virtual environment.

3. Activate virtual environment.

4. Install dependencies  from requirements.txt




Dependencies include:

- python 3
- pip
- virtualenv (or alternative tool)
- pyleniumio
- pytest



Please find below more details on how to install on macOS.



### Clone repo

- Clone this repo to your local machine using 

```
▶ git clone 
```



### Create virtual environment

```shell
▶ cd py-abn-lookup
▶ virtualenv venv
```



### Activate virtual environment

```shell
▶ source venv/bin/activate
```



### Install dependencies  from requirements.txt

```shell
▶ pip install requirements.txt
▶ pylenium --version
```



## Install driver



Pylenium installs these for you automatically! YOU DO NOT NEED TO DO THIS!

For more details, please visit [Pyleniumio docs](https://elsnoman.gitbook.io/pylenium/misc/install-chromedriver).



## Running the tests

Run all tests

```
▶ pytest tests   
```



Headless tests

```shell
# Headless tests
pytest tests --options="headless, disable-gpu, no-sandbox"
```



Run the tests using Chrome.

Pylenium.json is located in the root folder of the repo.

```json
# pylenium.json
"driver": {
    "browser": "chrome",
    "remote_url": "",
    "wait_time": 10,
    "page_load_wait_time": 0,
    "options": [],
    "experimental_options": null,
    "capabilities": {},
    "extension_paths": [],
    "version": "latest"
  }

```



Configuring browser from terminal. This is the browser name - "chrome" or "firefox" or "ie" or "opera" or "edge". For example, Chrome

```shell
pytest tests --browser=chrome
```



![test_results](img/test_results.png)





## FAQ

- **I am getting the error related to driver**
    
    - Please check your browser version. Browser version should match driver version. 
    - Update your browser if necessary or specify which driver version you want to use in pylenium.json.
    - For more info please visit [Pyleniumio docs.](https://elsnoman.gitbook.io/pylenium/)
    
    ![chrome_version](img/chrome_version.png)
    
    ![driver_manager](img/driver_manager.png)

---



## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Author: [Maksim Zinovev](https://github.com/MaksimZinovev) 

