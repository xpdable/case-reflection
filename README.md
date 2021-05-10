# Case - Reflection
We have Json file describing a list for functions calls history from the system.
Each element of the Json array is representing an invoking action.
For example, below snippet means function `fooONE` is called with two parameters `param1` and `param2`, and the function returned a value (Not None/null). Please refer to [example](func.json).
```Json
[
  ...
    {
        "func": "fooONE",
        "param": ["param1", "param2"],
        "return": true
    }
  ...
]
```
Now, teams want to evaluate all actions, therefore please write a function to traverse all historical calls according to a given json file.
## Hints
- The number of functions is not fixed, it is according to the system runtime calls. Sometimes, during a period of time, there are only one function is called, and sometimes 500+ different functions.

## Lean Mode

- If `param` makes the function complicated, you can image your function deal with only one `Object` as parameter. 
- If `return` value makes your confused, you can ignore it as well.
- In this case, please refer to [simple-example](func-simple.json)
```json
[
  ...
    {
        "func": "fooONE",
        "param": "Object"
    }
  ...
]
```

## Bonus

- `order` is a key to describe the order of the call. You can manages this in your function as well.

```json
[
  ...
    {
        "func": "fooONE",
        "param": "Object",
        "return": true,
        "order": 666
    }
  ...
]
```
