ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
GENERATOR_CMD:=/home/toni/project/personal/routeros-generator/bin/console
PYTHON:=3.8

install:
	pip install -r requirements.txt -r test-requirements.txt

resources:
	export TARGET_DIR=${ROOT_DIR}
	TARGET_DIR=${ROOT_DIR} ${GENERATOR_CMD} app:generate
	tox
	$(MAKE) test-unit
	$(MAKE) sanity

sanity:
	ansible-test sanity --python ${PYTHON}

test-unit:
	ansible-test units --python ${PYTHON} --color

build-doc:
	ansible-doc-extractor ./docs ./plugins/modules/ros_*.py
