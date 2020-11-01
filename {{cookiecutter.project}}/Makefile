.PHONY: test

default: test

test:
	virtualenv venv -q
	./venv/bin/pip3 install -r {{cookiecutter.project}}/requirements.txt -q
	./venv/bin/pip3 install -r tests/requirements.txt -q
	cd tests; \
	    PYTHONPATH=../{{cookiecutter.project}} \
	    ../venv/bin/python3 -m pytest \
	    --cov=../{{cookiecutter.project}}/ --cov-report=html:../reports/coverage \
	    --html=../reports/unit-integration/test-report.html --self-contained-html \
	    --capture=tee-sys

cicd-test:
	pip3 install -r {{cookiecutter.project}}/requirements.txt -q
	pip3 install -r tests/requirements.txt -q
	cd tests; \
	    PYTHONPATH=../{{cookiecutter.project}} \
	    python3 -m pytest \
	    --cov=../{{cookiecutter.project}}/ --cov-report=html:../reports/coverage \
	    --html=../reports/unit-integration/test-report.html --self-contained-html \
	    --capture=tee-sys

image:
	docker build -t {{cookiecutter.project}} .

rpm:
	rpmbuild -ba rpm.spec \
	    --define '_PROJECT_DIR $(shell pwd)' \
	    --define '_VERSION_APP $(shell cat VERSION | cut -d- -f 1)' \
	    --define '_VERSION_PKG $(shell cat VERSION | cut -d- -f 2)'
