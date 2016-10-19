= Protocol =

== Scoreboard ==

* Connect to IP, port 8000
* Listen for "side:A,button:B,press:C", where A=1 or 2; B=1 or 2; C=single or double

== Button server ==

* Connect to IP, port 8000
* Publish messages based on what was pressed:

	* "side:A,button:B,press:C", where A=1 or 2; B=1 or 2; C=single or double

