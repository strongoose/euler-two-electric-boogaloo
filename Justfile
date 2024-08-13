fix: mypy
	rye check --fix && rye fmt

mypy:
    rye run mypy --strict src/euler

test:
    rye test -v

run:
	rye run euler
