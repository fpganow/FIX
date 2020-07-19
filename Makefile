PYTHON=python3.8

clean:
	rm -rf venv

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || ${PYTHON} -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

#test:
#	${PYTHON} -m pytest Fix42Tests.py

.PHONY: unit_tests
unit_tests: venv
	@echo "Running unit tests"
	. ./venv/bin/activate; ${PYTHON} -m pytest --disable-pytest-warnings --color=yes -r ap  ./tests/

# make test-TestFix42
# make test-"TestFix42 and test_create_Heartbeat"
.PHONY: test-%
test-%: venv
	@echo "Running tests with filter $*"
	#${PYTHON} -m pytest --color=yes -r ap -k TravelCosts -k "$*" tests
	. ./venv/bin/activate; ${PYTHON} -m pytest --disable-pytest-warnings -r fEsp -k "$*" ./tests/

# make test-info-TestFix42
# make test-info-"TestFix42 and test_create_Heartbeat"
.PHONY: test-info-%
test-info-%: PYTEST_ARGS+=--log-cli-level=info -s
test-info-%: venv
	@echo "Running tests with filter $* and info verbosity"
	. ./venv/bin/activate; ${PYTHON} -m pytest ${PYTEST_ARGS} -r fEsp -k "$*" ./tests/

# make test-debug-TestFix42
# make test-debug-"TestFix42 and test_create_Heartbeat"
.PHONY: test-debug-%
test-debug-%: PYTEST_ARGS+=--log-cli-level=debug -s
test-debug-%: venv
	@echo "Running tests with filter $* and info verbosity"
	. ./venv/bin/activate; ${PYTHON} -m pytest ${PYTEST_ARGS} -r fEsp -k "$*" ./tests/
