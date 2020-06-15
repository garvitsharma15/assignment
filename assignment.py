def required_steps(n, forward, backward):
    if n <= forward:
        return n
    return (forward + backward) * (n - forward) + forward

forward = 3
backward = 2
n = 150
print(required_steps(n, forward, backward))
