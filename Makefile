.PHONY: about
about:
	@echo "This is a simple BinarySearch api using FastAPI."

.PHONY: run
run:
	@echo "Running the FastAPI server..."
	@cd src && uvicorn main:app --reload

.PHONY: install
install:
	pip install -r src/requirements.txt