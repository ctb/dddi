all: investigators.html

clean:
	-rm investigators.rst

investigators.rst: dddi.py
	./make-rst.py > investigators.rst

investigators.html: investigators.rst
	rst2html.py investigators.rst investigators.html
