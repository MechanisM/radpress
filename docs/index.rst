.. radpress documentation master file, created by
   sphinx-quickstart on Fri May 25 15:23:49 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Radpress
========
Radpress is a simple blog application for Djangonauts. It doesn't use WYSIWYG
editor. The default markup syntax is `reStructuredText`_ and you can preview
your entry simply before published it.

Installation
------------
You can install Radpress with `pip` or `easy_install`::

    pip install radpress

It also installs it's dependencies, but you need some configuration after
package installation. In your django project, you should add `easy_thumbnails`
before `radpress`.

Contents:

.. toctree::
   :maxdepth: 2

   configuration



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _reStructuredText: http://docutils.sourceforge.net/rst.html
