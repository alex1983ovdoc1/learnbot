MyBot
=========

MyBot - is a telegram bot that is made to make your life better by sending you pictures of cats

Installation
----------------

Сreate a virtual environment and activate it, then run the following:

.. code-block:: text

    pip install -r requirements.txt

Put pictures of cats in your images folder. The title of the photo must start with cat and end with .jpg e.g. cat73489.jpg

Settings
----------

Create file settings.py and add next settings:

.. code-block:: python
    API_KEY = "API_KEY with you received from BotFather"

    USER_EMOJI = [':thumbs_up:', ':cat:', ':panda:', ':dog:', ':cow:', ':frog:', ':fox:', \
        ':rabbit:', ':chicken:', ':goat:', ':bear:', ':crocodile:', ':giraffe:', ':dolphin:',\
        ':duck:', ':koala:', ':horse:', ':house:']

Launch
----------

In the activated virtual environment run:

.. code-block:: text
    
    python bot.py

