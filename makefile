all:

clean:
	rm -rf _pycache_
	rm -rf webapp/_pycache_

test:
	pytest

run:
	flask --app webapp/app.py run