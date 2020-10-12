# -*- coding: utf-8 -*-
"""
"""

from fplib import dictf, mapf, flip_dict, unlist1, relist1, deepmap

#%% Examples
def example_1():
  """
  <E1>  

  .. |fplib| replace::
    *fplib*

  .. currentmodule:: fplib

  Let us start with showing some examples of function composition. 
  
  One of the functions that is commonly used within |fplib| is :func:`dictf`, 
  which simply transforms a dictionary into a function. 
  
  Imagine having defined a few colors, and a color encoding dictionary. 
  
  >>> colors = ['red', 'green', 'blue']
  >>> encd = {'red': 0, 'green': 1, 'blue': 2}

  We can encode the colors like this:

  >>> encf = dictf(encd) # create the encoding function
  >>> encs = map(encf, colors) # map it over the colors
  >>> encs
  [0, 1, 2]
  
  Now suppose that the structure of the colors becomes more complex.
  
  >>> lcolors = [['red', 'green'], ['green', 'blue']]
  
  If we want to encode and preserve the structure, there are multiple 
  approaches we can take. We will show three of them:

  **1. Transforming the function into a function over lists**
  
  One option is to transform a function `f` over an element into a 
  function `g` over a *list* of elements 
  (which applies the function `f` over each element).
  For this purpose, we have another function :func:`mapf`. 

  We can make it work over lists as follows:
  
  >>> lencf = mapf(encf) # transform into function over lists
  >>> lencf(colors) # map over the list of colors
  [0, 1, 2]
  
  If we want to make it further work over lists-of-lists, 
  we can do the following:  
  
  >>> llencf = mapf(lencf) # transform again
  >>> llencf(lcolors)
  [[0, 1], [1, 2]]

  Although the structure might look rather unlikely to occur, 
  similar situations happen quite often when dealing with 
  :class:`pandas.DataFrames`. 
  
  Suppose the frame contains lists of colors in a column.
  
  >>> import pandas as pd  
  >>> df = pd.DataFrame({'colors': lcolors})
  >>> df
            colors
  0   [red, green]
  1  [green, blue]
  
  We could simply encode them as follows:  
  
  >>> df['encs'] = df['colors'].apply(mapf(dictf(encd)))
  >>> df
            colors    encs
  0   [red, green]  [0, 1]
  1  [green, blue]  [1, 2]
  
  Therefore, if we often apply functions, it is useful to be 
  able to combine them in a compact manner.   
  
  Otherwise we would need to do something as follows:
  
  >>> df['encs'] = df['colors'].apply(lambda l: [encd[e] for e in l])

  Although this example looks quite alright in both cases, 
  we needed to use two purely auxiliary names (`l` and `e`) for the latter. 
  For such a basic computational process, 
  it might seem as too much, especially because what *we want to express
  is rather straightforward*. 
  
  **2. Playing with structure**

  Another approach we could take with |fplib| is to flatten the 
  structure of the `lcolors` list, apply the encoding and put the 
  structure back. 

  For this, we can remove the outer structure with :func:`unlist1`.

  >>> ucolors = unlist1(lcolors)
  >>> ucolors
  ['red', 'green', 'green', 'blue']
  
  Now we can map directly: 
  
  >>> uencs = map(encf, ucolors)
  >>> uencs
  [0, 1, 1, 2]
  
  And finally, we can relist it back to the previous structure. 
  
  >>> lencs = relist1(uencs, lcolors)
  >>> lencs
  [[0, 1], [1, 2]]
  
  .. note:: 
    This approach is useful if we can perform some calculation 
    much faster over the linear structure, but we need to restructure
    the results.
  
  **3. Deep mapping**  
  
  Yet another approach would be to map deeply over the listed structure
  using :func:`deepmap`. 
  
  This approach, however, is of different semantics, and is here shown 
  rather as an example.   
  
  >>> deepmap(encf, lcolors)
  [[0, 1], [1, 2]]
  
  **Summary**

  The functions in |fplib| can sometimes make the code more compact and 
  more readable for some people. 
  
  </E1>
  """

#%% Main 
if __name__ == "__main__":
  import doctest
  doctest.testmod()

