.. :changelog:

History
=======

Pending Release
---------------

* Removed support for old Django versions
* Fixed all deprecation warnings on Django 1.7 and 1.8
* Historically Nexus had a module that embedded Django Admin; this has not worked since Django 1.3 due to removal of
  the ``adminmedia`` template tag that the templates were still using. Because it seems that no one has been using it,
  it has been removed. Users are encourage to just use the normal Django Admin instead. Nexus thus ships with no
  modules included.

1.0.0 (2015-12-09)
------------------

* First publication on PyPI as ``nexus-yplan``
* Django 1.8 compatibility
