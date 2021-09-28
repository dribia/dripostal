Libpostal's [**`expand`**](https://github.com/openvenues/libpostal#examples-of-normalization) method allows us to parse a string 
containing an address and 
[normalize](https://github.com/openvenues/libpostal#examples-of-normalization)
it to its standard form.

To make a query to our Libpostal's `expand` service using `dripostal`, we can 
run the following code:

```python
from dripostal import DriPostal

dripostal = DriPostal(url="http://0.0.0.0:4400")

response = dripostal.expand("C/ Ocho, P.I. 4")
print(response)

"""
[
    'calle 8 poligono industrial 4', 
    'carrer 8 poligon industrial 4',
    'calle 8 piso 4', 
]
"""
```

Note how the response of the `expand` method is a list of strings. This is
because the address can have more than one normalized forms, as in the example
above, where it is not clear if the original address is in Catalan or 
in Spanish.