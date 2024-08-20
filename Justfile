fix: mypy
    rye fmt && rye check --fix

mypy:
    rye run mypy --strict src/euler

test:
    rye test -v

run *problems:
	rye run euler {{problems}}

quickrun:
	rye run euler -7 -12 -14 -23 -27

quicktest:
    rye test -v -- -k 'not (test_p7 or test_p12 or test_p14 or test_p23 or test_p27)'
