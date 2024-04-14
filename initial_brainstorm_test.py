import numpy as np

# Question 1 Answer
ans1 = lambda t, A, k, m, phi: A * np.sin(np.sqrt(k / m) * t + phi)
ans1_cos = lambda t, A, k, m, phi: A * np.cos(np.sqrt(k / m) * t + phi)

# Question 2 Answer
t1 = np.linspace(0, 20, 10000)
x1 = ans1(t1, 1, 10, 1.5, np.pi/2)

# Question 4 Answer
def ans4(k, m, x0, v0, dt):
    a0 = - k * x0 / m
    vf = v0 + a0 * dt
    xf = x0 + v0 * dt
    return xf, vf

# Question 5 Answer
x2 = np.array([1])
v2 = np.array([0])
t2 = np.array([0])

for i in np.arange(10000):
    x0 = x2[-1]
    v0 = v2[-1]
    t0 = t2[-1]
    
    xf, vf = ans4(10, 1.5, x0, v0, 0.002)
    tf = t0 + 0.002
    
    x2 = np.append(x2, xf)
    v2 = np.append(v2, vf)
    t2 = np.append(t2, tf)

# Autograder tests
def test1(f):
    args_list = [list(np.random.uniform(0.1, 5.1, 5)) for i in np.arange(10)]
    if [f(*args) for args in args_list] == [ans1_cos(*args) for args in args_list]:
        raise Exception("You probably used a cosine function instead of sine. If that's the case, your answer is correct! However, for consistency with the rest of the exercise, we want you to use a sine function here.")  
    elif [f(*args) for args in args_list] != [ans1(*args) for args in args_list]:
        raise Exception("Your code is incorrect.")
    else:
        print("Correct!")
        print("Well done!")

def test2(t, x):
    if (t == t1).all() and (x == x1).all():
        print("Correct!")
        print("Well done!")
    else:
        raise Exception("Your code is incorrect.")

def test4(f):
    args_list = [list(np.random.uniform(0.1, 5.1, 5)) for i in np.arange(10)]
    if [f(*args) for args in args_list] == [ans4(*args) for args in args_list]:
        print("Correct!")
        print("Well done!")
    else:
        raise Exception("Your code is incorrect.")

def test5(x, v, t):
    if (x == x2).all() and (v == v2).all() and (t == t2).all():
        print("Correct!")
        print("Well done!")
    else:
        raise Exception("Your code is incorrect.")
