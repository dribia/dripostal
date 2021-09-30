
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

### API Method Names
In case your Libpostal REST service has a different API layout,
DriPostal allows you to modify the names of the target API methods, for both `parse` and `expand`.
To do so, you should specify them when initializing the class:
```python
from dripostal import DriPostal

dripostal = DriPostal(
    url="http://0.0.0.0:4400", 
    parse_method="parser", 
    expand_method="expander",
)
```
In the example above, DriPostal's `parse` method will be querying `http://0.0.0.0:4400/parser` 
instead of `http://0.0.0.0:4400/parse`, and its `expand` method will be querying 
`http://0.0.0.0:4400/expander`. 

!!!warning
    DriPostal is designed to interact with GET-based Libpostal REST APIs. Its URL template is:
    ```
    <schema>://<domain>/<method>?q=<query>
    ```

    If you are trying to query a POST-based Libpostal REST service like 
    [`libpostal-rest-docker`](https://github.com/johnlonganecker/libpostal-rest-docker) DriPostal is not your tool 😔
