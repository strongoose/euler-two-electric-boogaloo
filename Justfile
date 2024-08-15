fix: mypy
	rye check --fix && rye fmt

mypy:
    rye run mypy --strict src/euler

test:
    rye test -v

run *problems:
	rye run euler {{problems}}

quick:
	rye run euler -7 -12
