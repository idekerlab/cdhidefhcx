Integration testing
=======================

To support `integration testing <https://en.wikipedia.org/wiki/Integration_testing>`__ the unit tests in **cdhidefhcx**
include a parallel set of tests reside in the existing test framework and
can be activated if ``CDHIDEFHCX_INTEGRATION_TEST`` environment
variable is set to any value:

Example variable:

.. code-block::

    export CDHIDEFHCX_INTEGRATION_TEST="true"
    make test
