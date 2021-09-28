## PIP

Installation is as simple as:

```shell
pip install dripostal
```

Dripostal's only dependency is [**Pydantic**](https://pydantic-docs.helpmanual.io/), 
a _data validation framework_ we use to build Dripostal's response schemas:

### Async

To use the asynchronous Dripostal client provided in the `dripostal.aio` module
you should have [AIOHTTP](https://docs.aiohttp.org/en/stable/) already installed, 
or install it as an extra dependency for Dripostal:

```shell
pip install dripostal[aiohttp]
```
