Libpostal's [**`parse`**](https://github.com/openvenues/libpostal#examples-of-parsing) method allows us to parse a string containing
an address and label its parts, e.g. identify its `road`, `city`, `country`, etc.

To make a query to our Libpostal's `parse` service using `dripostal`, we can 
run the following code:

```python
from dripostal import DriPostal

dripostal = DriPostal(url="http://0.0.0.0:4400")

response = dripostal.parse("Carrer de la Llacuna, 162, 08018 Barcelona")
print(type(response))

"""
<class 'dripostal.schemas.Address'>
"""
```

## Address

Note how the `response` variable of the above code chunk is of a special 
`Address` type. This is the response model of DriPostal's `parse` method, 
and is a Pydantic model. Then, its attributes are type-validated, currently
being all of them `str` types.

The attributes of the `Address` response model are every possible 
Libpostal's `parse` method label. A complete list can be found 
[here](https://github.com/openvenues/libpostal#parser-labels).

### List

PyPostal, the Libpostal's Python bindings library, returns the `parse` results
as a list of tuples. This is why `Address` response models have a `list` method,
to recover this structure.

```python
from dripostal import DriPostal

dripostal = DriPostal(url="http://0.0.0.0:4400")

response = dripostal.parse("Carrer de la Llacuna, 162, 08018 Barcelona")
print(type(response.list()))

"""
[('house', 'mòdul 303'), ('house_number', '162'), ...]
"""
```
