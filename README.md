# cs6230-final-project-DEAP

## Installation Notes

The installation package for DEAP uses `2to3` in its build. Support for this was removed in [setuptools v58.0.0](https://setuptools.pypa.io/en/latest/history.html#v58-0-0).
Because of this, we create a virtual environment without `setuptools` and then install the last version before version 58.

```shell
virtualenv --no-setuptools .env
source .env/bin/activate # or for Windows, .\.env\Scripts\activate
pip install setuptools<58
pip install -r requirements.txt
```