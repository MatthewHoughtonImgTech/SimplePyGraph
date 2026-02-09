# Requirements

- DearPyGui

# How to Use

call createGraphWindow() which will return a queue

to add items to the graph send a dict that looks like
```python
{
  "name" : name_of_the_line_str
  "xval" : x_axis_value_float
  "yval" : y_axis_value_float
}
```


```python
import GraphingUtil as graph
queue = graph.createGraphWindow()

# SOME TIME LATER #
x = time() #or anything else you'd like
y = someSuperCoolFunctionThatIsAwesome()

queue.put({
  "name" : "line1",
  "xval" : x,
  "yval" : y,
})

```
