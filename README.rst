.. image:: preview.jpg
  :width: 400
  :alt: Preview
  

Prerequisites
=============

#. Download and Install Google Chrome
#. Download and Install chromedriver https://sites.google.com/chromium.org/driver/
#. Add chrome to PATH and give it executable rights

.. code-block:: shell

    cp chromedriver /usr/local/bin/
    sudo xattr -d com.apple.quarantine /usr/local/bin/chromedriver

Dev
===

.. code-block:: shell

    brew install python@3.9
    CXXFLAGS="-I/opt/homebrew/include" pipenv install

    # this is because we need the latest pyinstaller for macOS M1 Silicon arm64 arch
    git clone --depth 1 https://github.com/pyinstaller/pyinstaller.git
    pushd pyinstaller/bootloader
    python ./waf all
    popd
    pipenv run pip install file://`pwd`/pyinstaller/

    cp mydesk.ini ~/mydesk.ini (and also edit this file)
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
