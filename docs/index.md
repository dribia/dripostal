<p style="text-align: center; padding-bottom: 1rem;">
    <a href="https://dribia.github.io/dripostal">
        <img 
            src="https://dribia.github.io/dripostal/img/logo_dribia_blau_cropped.png" 
            alt="dripostal" 
            style="display: block; margin-left: auto; margin-right: auto; width: 40%;"
        >
    </a>
</p>

<p style="text-align: center">
    <a href="https://github.com/dribia/dripostal/actions?query=workflow%3ATest" target="_blank">
        <img src="https://github.com/dribia/dripostal/workflows/Test/badge.svg" alt="Test">
    </a>
    <a href="https://github.com/dribia/dripostal/actions?query=workflow%3APublish" target="_blank">
        <img src="https://github.com/dribia/dripostal/workflows/Publish/badge.svg" alt="Publish">
    </a>
    <a href="https://codecov.io/gh/dribia/dripostal" target="_blank">
        <img src="https://img.shields.io/codecov/c/github/dribia/dripostal?color=%2334D058" alt="Coverage">
    </a>
    <a href="https://pypi.org/project/dripostal" target="_blank">
        <img src="https://img.shields.io/pypi/v/dripostal?color=%2334D058&label=pypi%20package" alt="Package version">
    </a>
</p>

<p style="text-align: center;">
    <em>A tiny API client for the Pelias Libpostal REST service.</em>
</p>

---

**Documentation**: <a href="https://dribia.github.io/dripostal" target="_blank">https://dribia.github.io/dripostal</a>

**Source Code**: <a href="https://github.com/dribia/dripostal" target="_blank">
https://github.com/dribia/dripostal</a>

---

[**Libpostal**](https://github.com/openvenues/libpostal) is a widely known C library for 
**parsing and normalizing street addresses** around the world. 

Despite having its own Python bindings, getting to install the library can be quite hard and time-consuming.
A common workaround is then to use a dockerized service exposing Libpostal as a REST API, 
e.g. [**Pelias' Libpostal REST service**](https://github.com/pelias/libpostal-service).

**Dripostal** aims to provide a Python interface with such API, both in the synchronous and the asynchronous ways.

## Key features

* Query Libpostal's [**`parse`**](https://github.com/openvenues/libpostal#examples-of-parsing) and [**`expand`**](https://github.com/openvenues/libpostal#examples-of-normalization) methods.
* Return results as [**Pydantic**](https://pydantic-docs.helpmanual.io/) models.
* Provides a mirror [**async client**](https://docs.python.org/3/library/asyncio.html) enabling asynchronous queries to the Libpostal REST service.

## Example

In order to successfully run the following example, a Libpostal service should be running locally:

```shell
docker run -d -p 4400:4400 pelias/libpostal-service
```

!!!info
    The command above will be pulling the `libpostal-service` Docker image from **Pelias** and 
    running a container that will serve the Libpostal REST service through its port 4400.

    * With option `-p 4400:4400` we are mapping port 
      `4400` in the docker container to port `4400` in the docker host, i.e. your computer. 
      You could map it to another port of the host, e.g. the `8080`, changing `4400:4400` for `8080:4400`.
    * With option `-d` we are running the docker container in _detached mode_, i.e. in the background. 

Now we should be able to run the following code:

```python
from dripostal import DriPostal

dripostal = DriPostal(url="http://0.0.0.0:4400")

dripostal.parse("Planta 3 mòdul 303, Carrer de la Llacuna, 162, 08018 Barcelona")

"""
Address(
    house='mòdul 303', 
    house_number='162', 
    road='carrer de la llacuna', 
    level='planta 3', 
    postcode='08018', 
    city='barcelona', 
    country=None, 
    ...
)
"""
```
