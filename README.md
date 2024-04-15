# CarPark-Example-Application
Created For L2 and L3 Python Programming Class

[![CodeQL](https://github.com/Josh-HOY-Account/CarPark-Example-Application/actions/workflows/codeql.yml/badge.svg)](https://github.com/Josh-HOY-Account/CarPark-Example-Application/actions/workflows/codeql.yml)[![Python application](https://github.com/Josh-HOY-Account/CarPark-Example-Application/actions/workflows/python-app.yml/badge.svg?event=pull_request)](https://github.com/Josh-HOY-Account/CarPark-Example-Application/actions/workflows/python-app.yml)

Please Note Currently The Program has been Manually Tested and has Passed, Automatic Testing Is Currrently Not Supported
## Car Park Example Application
- there are Known Issues Currently In V1 and V2 that effect Billing for Days over the 10 days set in the config (ParkingExpire = 10) found in Data.py where the amount shown to the user will be about £1000 Lower than if you did the calculation your self, this seems to be due to the hours per day being 6.001492537313433 according to the code

> Please Note this Program is For Private Use Within [Heart of Yorkshire Education Group](https://heartofyorkshire.ac.uk/) and Should Not be Used With out Permission
> if you are not part of [Heart of Yorkshire Education Group](https://heartofyorkshire.ac.uk/). For Permission Please email ake16003763@heartofyorkshire.ac.uk

## Installation
This Program Uses [Python 3.11+](https://www.python.org/downloads/) to run. and Might not work on older Verions

~~~
git clone https://github.com/Josh-HOY-Account/CarPark-Example-Application/ &&
cd CarPark-Example-Application &&
cd "V1 - CLI Based" &&
py CarPark.py
~~~
~~~
git clone https://github.com/Josh-HOY-Account/CarPark-Example-Application/ &&
cd CarPark-Example-Application &&
cd "V2 - Commands" &&
py CarPark.py
~~~
~~~
git clone https://github.com/Josh-HOY-Account/CarPark-Example-Application/ &&
cd CarPark-Example-Application &&
cd "V3 - GUI" &&
py gui.py
~~~
