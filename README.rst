.. image:: preview.jpg
  :width: 400
  :alt: Preview
  
  
Dev
===

.. code-block:: shell

    cp mydesk.ini ~/mydesk.ini (and also edit this file)
    pipenv install .
    mydesk

Release
=======

.. code-block:: shell

    ./pyinstaller.sh

Environment Variables
=====================

.. list-table:: Supported Environment Variables

    * - Name
      - Description
    * - MYDESK_CONFIG_FILE
      - Defaults to ~/mydesk.ini
