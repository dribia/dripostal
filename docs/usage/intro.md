
## Libpostal
[Libpostal](https://github.com/openvenues/libpostal) is a `C` 
library for parsing/normalizing street addresses around the world 
using statistical NLP and open data. It has officially supported Python 
bindings in the [PyPostal](https://github.com/openvenues/pypostal) library.
However, a common alternative is to run Libpostal as a REST service and query it to obtain 
the desired results, e.g. using the [Pelias Libpostal REST service](https://github.com/pelias/libpostal-service).

## Pelias Libpostal Service

One of the best backed Libpostal services is the one that comes with
[Pelias](https://github.com/pelias/pelias). One can run the service using [Docker](https://www.docker.com/) 
with the following command:

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

## DriPostal
DriPostal allows us to query the two methods offered by Libpostal, namely:

* [**Parse**](parse.md): Parse a string containing an address to label its parts.
* [**Expand**](expand.md): Normalize a string containing an address to its standard form.

The main object to use is the `DriPostal` class, which has interface methods to query such endpoints. 

To initialize the `DriPostal` class, one should provide the URL of the service.
For instance, if you have used the command above to run the Pelias Libpostal REST
service in your computer, you should initialize the class as follows:

```python
from dripostal import DriPostal

dripostal = DriPostal(url="http://0.0.0.0:4400")
```

Now, with the `dripostal` object, you can make any query to both the [**`parse`**](parse.md)
and [**`expand`**](expand.md) endpoints.

!!!info
    There is also a mirror [asynchronous client](async.md) providing the same interface in the `dripostal.aio` module.
