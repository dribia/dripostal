DriPostal offers also an asynchronous client to interact with the 
Libpostal service.

Using the asynchronous client instead of the standard one might be a bit
more complicated, but can introduce significant performance improvements.

Note that Dripostal needs the [AIOHTTP](https://docs.aiohttp.org/en/stable/) library to run the async client. 
It can be installed as an [optional dependency](../install.md).

## Usage
This is the simplest example we can think of:

=== "Python >=3.7"

    ```python
    import asyncio
    
    from dripostal.aio import DriPostal
    
    dripostal = DriPostal(url="http://0.0.0.0:4400")
    
    response = asyncio.run(dripostal.parse("Carrer de la Llacuna, 162, 08018"))
    print(type(response))
    
    """
    <class 'dripostal.schemas.Address'>
    """
    ```

=== "Python 3.6"
    
    ```python
    import asyncio
    
    from dripostal.aio import DriPostal
    
    dripostal = DriPostal(url="http://0.0.0.0:4400")
    
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(dripostal.parse("Carrer de la Llacuna, 162, 08018"))
    loop.close()
    print(type(response))
    
    """
    <class 'dripostal.schemas.Address'>
    """
    ```


Note how the response type is an `Address` model, the same type we would obtain
from the standard synchronous client.

Now, the most common use-case would be to parse -or expand- a list of addresses.

=== "Python >= 3.7"

    ```python
    import asyncio
    
    from dripostal.aio import DriPostal
    
    dripostal = DriPostal(url="http://0.0.0.0:4400")
    
    addresses = [
        "777 Brockton Avenue, Abington MA 2351",
        "30 Memorial Drive, Avon MA 2322",
        "250 Hartford Avenue, Bellingham MA 2019",
    ]
    
    async def main():
        return await asyncio.gather(*list(map(dripostal.parse, addresses)))
    
    results = asyncio.run(main())
    print(results)
    
    """
    [
        Address(house=None, ...),
        Address(house=None, ...),
        Address(house=None, ...),
    ]
    """
    ```

=== "Python 3.6"

    ```python
    import asyncio
    
    from dripostal.aio import DriPostal
    
    dripostal = DriPostal(url="http://0.0.0.0:4400")
    
    addresses = [
        "777 Brockton Avenue, Abington MA 2351",
        "30 Memorial Drive, Avon MA 2322",
        "250 Hartford Avenue, Bellingham MA 2019",
    ]
    
    async def main():
        return await asyncio.gather(*list(map(dripostal.parse, addresses)))
    
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main())
    loop.close()
    
    print(results)
    
    """
    [
        Address(house=None, ...),
        Address(house=None, ...),
        Address(house=None, ...),
    ]
    """
    ```
