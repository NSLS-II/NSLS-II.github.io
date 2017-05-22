#. wget https://github.com/ipython-contrib/IPython-notebook-extensions/raw/master/custom.example.js
#. cp custom.example.js ~/.ipython/profile_default/static/custom/example.js
#. Edit custom.js
   #. Uncomment ``//    IPython.load_extensions('publishing/gist_it')``
   #. Change it to ``    IPython.load_extensions('gist')``
#. Execute the following code in IPython::

   import IPython
   IPython.html.nbextensions.install_nbextension('https://rawgithub.com/minrk/ipython_extensions/master/nbextensions/gist.js')

#. Start IPython notebook
#. Look for the curvy arrow to the right of the ``Cell Toolbar`` box in the
   Toolbar
#. Click it!
#. It will ask for a GitHub OAuth Token which you can create by following
   `these instructions <https://help.github.com/articles/creating-an-access-token-for-command-line-use/>`_

