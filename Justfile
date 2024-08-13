fix: mypy
	rye check --fix && rye fmt

mypy:
    rye run mypy --strict src/euler

run:
	rye run euler
