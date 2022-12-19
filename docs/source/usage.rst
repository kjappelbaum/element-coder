Usage
=====

Logging 
---------

element_coder uses the `loguru <https://loguru.readthedocs.io/en/stable/index.html>`_  for logging. 
By default, logging from element_coder is disabled to not interfere with your logs.

However, you can easily customize the logging:

.. code-block:: python

    import sys
    from loguru import logger

    # enable element_coder logging 
    logger.enable("element_coder")
    
    # define the logging level
    LEVEL = "INFO || DEBUG || WARNING || etc."

    # set the handler
    # for logging to stdout
    logger.add(sys.stdout, level=LEVEL) 
    # or for logging to a file
    logger.add("my_log_file.log", level=LEVEL, enqueue=True) 


In many cases, however, you might find it convenient to simply call :py:meth:`~element_coder.helpers.enable_logging`

.. code-block:: python

    from element_coder.utils import enable_logging

    enable_logging()

which will enable logging with sane defaults (i.e. logging to ``stderr`` for ``INFO`` and ``WARNING`` levels).

.. automodule:: element_coder.encode
    :members:

.. automodule:: element_coder.decode
    :members:
