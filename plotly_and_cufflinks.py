# -*- coding: utf-8 -*-
"""Plotly and Cufflinks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yw6mGCzsFLPbd3NUetuCT-o1lbs1ze1m

#Plotly and Cufflinks
"""

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

import cufflinks as cf
cf.go_offline()

"""we need to define this function first:


"""

def configure_plotly_browser_state():
  import IPython
  display(IPython.core.display.HTML('''
        <script src="/static/components/requirejs/require.js"></script>
        <script>
          requirejs.config({
            paths: {
              base: '/static/base',
              plotly: 'https://cdn.plot.ly/plotly-latest.min.js?noext',
            },
          });
        </script>
        '''))

"""And call it in each offline plotting cell:"""

configure_plotly_browser_state()