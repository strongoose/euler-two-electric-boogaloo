fix: mypy
	rye check --fix && rye fmt

mypy:
    rye run mypy --strict src/euler

test:
    rye test

run:
	rye run euler
