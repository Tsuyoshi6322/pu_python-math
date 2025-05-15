# pu_python-math

Project for Uni Python classes - approximation of $\pi$ via Monte Carlo's method, Pythagorean trios and approximation of Euler's Constant $e$.

## Assignments

1. Write a code that approximates $\pi$:
    - Use Monte Carlo's method.
    - Test the program for 100 and 10K tries.

2. Write a code that definies and calculates Pythagorean Trio: $a^2+b^2=c^2$
    - Accept variables `a`,`b`,`c` as input.
    - Include a check to verify if they form a right triangle.

3. Write a code that calculates the sum for any value `n` using the formula
    $$\sum_{k=1}^{n}(2k-1)$$

4. Write a code that approximates Euler's number using the infinite series
    $$e = \sum_{n=0}^{\infty}\frac{1}{n!}$$

## In depth info

### Monte Carlo's method for $\pi$

Imagine a square with a side length of 2 units.
Inside this square, draw a circle centered at the square's center with a radius of 1 unit.
The circle will perfectly fit inside the square, touching the midpoint of each side.

- The area of the square is $2^2 = 4$
- The area of the circle is $\pi \times 1^2 = \pi$

The idea behind it is that you throw points randomly into the square.
Some will fall inside the circle, some not - but will remain inside the square.

The ratio of the points inside the circle to the total points thrown should be approximately equal to the ratio of the areas:

$$
    \frac{\text{Points inside circle}}{\text{Total points}}
    \approx
    \frac{A_\text{circle}}{A_\text{square}}
    =
    \frac{\pi}{4}
$$

$$
    \pi = 4 \times \frac{\text{Points inside circle}}{\text{Total points}}
$$

#### Step by step

1. Generate random points ($x,y$) where $x$ and $y$ are uniformly distributed between $-1$ and $1$.
   This means that the points will fall inside the square that stretches from points $(-1,-1)$ to $(1,1)$

2. For each point, check if it lies inside the circle byu using the equation of a circle centered at $(0,0)$ with radius $1$:
   $$x^2 + y^2 \leq 1$$

   - If yes, increment the count of points inside the circle.

3. Repeat this for all points and calculate the results:
   $$\pi \approx 4 \times \frac{\text{Points inside circle}}{\text{Total points}}$$

### Pythagorean Trio

There are two steps that need to be performed for this assignment:

1. Verify if the provided values form a Pythagorean triple:

    - Check if the values are positive integers
    - Check whether $a^2+b^2 = c^2$

2. Verify if the values form a right triangles, treating them as the lengths of the sides:

    - Check if the values are positive integers
    - Check if they can be sorted so the value `c` is the largest
    - Check whether $a^2+b^2 = c^2$

### Calculate the sum of `n` odd numbers

This is a simple sum of `n` odd numbers:
$$\sum_{k=1}^{n}(2k-1)$$

### Approximate Euler's Constant $e$

Euler's Constant $e$ is a transcendental number (can't be written as a solution to any algebraic equation).
It's most commonly approximated via an infinite series:
$$e = \sum_{n=0}^{\infty}\frac{1}{n!}$$
