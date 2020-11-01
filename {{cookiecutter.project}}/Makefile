.PHONY: test

default: test

test:
	virtualenv venv -q
	./venv/bin/pip3 install -r fites-scripts-sender/requirements.txt -q
	./venv/bin/pip3 install -r tests/requirements.txt -q
	cd tests; \
	    PYTHONPATH=../fites-scripts-sender \
	    ../venv/bin/python3 -m pytest \
	    --cov=../fites-scripts-sender/ --cov-report=html:../reports/coverage \
	    --html=../reports/unit-integration/test-report.html --self-contained-html \
	    --capture=tee-sys

cicd-test:
	pip3 install -r fites-scripts-sender/requirements.txt -q
	pip3 install -r tests/requirements.txt -q
	cd tests; \
	    PYTHONPATH=../fites-scripts-sender \
	    python3 -m pytest \
	    --cov=../fites-scripts-sender/ --cov-report=html:../reports/coverage \
	    --html=../reports/unit-integration/test-report.html --self-contained-html \
	    --capture=tee-sys

image:
	docker build -t fites-scripts-sender .

rpm:
	rpmbuild -ba rpm.spec \
	    --define '_MODULE monitran-ws' \
	    --define '_PROJECT_DIR $(shell pwd)' \
	    --define '_VERSION_APP $(shell cat VERSION | cut -d- -f 1)' \
	    --define '_VERSION_PKG $(shell cat VERSION | cut -d- -f 2)'
