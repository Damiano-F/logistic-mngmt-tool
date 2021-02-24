init:
    pip install -r requirements.txt

test:
    py.test tests

docs:
	$(MAKE) -C $@

.PHONY: init test docs