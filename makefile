FILES :=        \
    .gitignore  \
    .travis.yml \
    apiary.apib \
    IDB.log     \
    models.html \
    models.py   \
    tests.py    \
    UML.pdf     \

all:

check:
	@for i in $(FILES);                                         \
    do                                                          \
        [ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; \
    done

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__
	rm -f models.out
	rm -f tests.out

sqlite3:
	#python3 manage.py makemigrations www
	#python3 manage.py sqlmigrate www 0001 &> sqlmigrate.log
	#cat sqlmigrate.log
	#python3 manage.py migrate
	python3 manage.py check
	django-admin testserver data/countries.json data/matches.json data/players.json --addrport localhost:8000
	django-admin sqlall www

test:
	python3 manage.py test --keepdb

models.html:
	export DJANGO_SETTINGS_MODULE="main.settings"
	pydoc3 -w ./
	mv copaDB.models.html copaDB/models.html
	rm -rf *.html
	mv copaDB/models.html models.html

IDB.log:
	git log > IDB.log

