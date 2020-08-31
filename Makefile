test-unit:
	pip install -r test-requirements.txt
	ansible-test units --python 3.8 --color

build-doc:
	ansible-doc-extractor ./docs ./plugins/modules/ros_*.py
