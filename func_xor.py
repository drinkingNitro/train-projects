
import functools as func
import sys

print(
    *map(
        lambda z: func.reduce(
            lambda x, y: abs(x - y),
            z
        ),
        zip(
            *map(
                lambda line: map(
                    int,
                    line.split()
                ),
                sys.stdin.readlines()[1:]
            )
        )
    )
)
