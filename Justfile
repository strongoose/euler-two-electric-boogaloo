fix: mypy
    rye fmt && rye check --fix

mypy:
    rye run mypy --strict src/euler

test:
    rye test -v

run *problems:
	rye run euler {{problems}}

quick:
	rye run euler -7 -12 -14
