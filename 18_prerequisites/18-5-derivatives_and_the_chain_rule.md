# Lesson 18.5 - Derivatives and the Chain Rule

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Appendices A–F (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 18 - Mathematical and Python Prerequisites

## The big picture: finding the bottom of a curve

Least squares (Lesson 13.1) says "choose the line with the **smallest** sum of squared errors". To find that minimum exactly, we need derivatives. Lesson 8.2 already used calculus for areas under curves. Here we use it for slopes.

**1. A derivative is a slope at a point.**

$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

It is the slope of the **tangent line**, the straight line that just touches the curve at $x$. Negative means the curve is going down, positive means going up, and 0 means flat.

**2. The rules you need.**

| Function | Derivative |
|---|---|
| constant $c$ | $0$ |
| $x^r$ | $r\,x^{r - 1}$ (power rule) |
| $c\,f(x)$ | $c\,f'(x)$ |
| $f(x) + g(x)$ | $f'(x) + g'(x)$ |
| $f(g(x))$ | $f'(g(x))\cdot g'(x)$ (**chain rule**) |

**3. The chain rule: outside times inside.** For something like $(5 - 2m)^2$, differentiate the **outside** (the square: $2 \times$ whatever is inside), then multiply by the derivative of the **inside** ($5 - 2m$ gives $-2$).

**4. At a minimum, the derivative is 0.** At the bottom of a smooth valley the tangent is flat. So: set $f'(x) = 0$ and solve. Then check that it really is a **minimum**: the **second derivative** $f''(x) > 0$ means the curve bends upward (a valley, not a hill).

![Left: the U-shaped loss L(m) = (5 − 2m)² with three tangent lines: slope −12 at m = 1 (red, downhill), slope 0 at m = 2.5 (green, flat at the bottom), slope +12 at m = 4 (orange, uphill). Right: the derivative L′(m) = 8m − 20, a straight line crossing zero at m = 2.5, marked as the minimum; a note says L″(m) = 8 > 0 so the curve bends upward](figures/derivative_and_minimum.png)

Left: the tangent slopes are −12, 0 and +12. Right: the derivative is negative to the left of 2.5 and positive to the right. It crosses 0 exactly at the bottom of the curve.

**5. A numerical check.** You can check a derivative with a small step $h$:

$$f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}$$

Too large an $h$ is inaccurate, and too tiny an $h$ loses precision in the computer. Something like $h = 10^{-5}$ is usually fine. It is a check, not a replacement for the exact derivative.

---

## Goal

Differentiate simple functions with the power and chain rules, and use $f'(x) = 0$ and $f''(x) > 0$ to find a minimum.

## Formulas

$$\frac{d}{dx}x^r = r\,x^{r - 1}, \qquad \frac{d}{dx}f(g(x)) = f'(g(x))\,g'(x)$$

At a minimum: $f'(x) = 0$ and $f''(x) > 0$.

---

## Example

Minimise $L(m) = (5 - 2m)^2$.

**Step 1: derivative by the chain rule.** Outside: $u^2 \to 2u$. Inside: $u = 5 - 2m \to -2$.
$$L'(m) = 2(5 - 2m)(-2) = -4(5 - 2m) = 8m - 20$$

**Step 2: set it to 0.**
$$8m - 20 = 0 \quad\Rightarrow\quad m = 2.5$$

**Step 3: second derivative.**
$$L''(m) = 8 > 0 \quad \Rightarrow \text{ a minimum}$$

**Step 4: check.** $L(2.5) = (5 - 5)^2 = 0$, the smallest possible value of a square. Tangent slopes at other points: $L'(1) = -12$ and $L'(4) = +12$, as in the figure.

**Step 5: numerical check at $m = 1$.** With $h = 0.001$:
$$\frac{L(1.001) - L(0.999)}{0.002} = \frac{(2.998)^2 - (3.002)^2}{0.002} = \frac{8.988 - 9.012}{0.002} = -12 \checkmark$$

---

## Doing it in Excel

Put $m$ in A2 and `=(5-2*A2)^2` in B2. A numerical slope: `=((5-2*(A2+0.001))^2-(5-2*(A2-0.001))^2)/0.002`. *Solver* can minimise B2 by changing A2. It finds 2.5.

---

## Your turn

Differentiate $(7 - 3m)^2$ and find its minimum.

**Answer:** $\dfrac{d}{db}(7 - 3m)^2 = 2(7 - 3m)(-3) = 18m - 42$. Setting it to 0 gives $m = 7/3 \approx 2.333$. The second derivative is $18 > 0$, so this is the unique minimum.

---

## Key takeaways

- A derivative is the slope of the tangent: negative going down, positive going up, 0 when flat.
- Power rule: $x^r \to r x^{r - 1}$. Chain rule: outside derivative × inside derivative.
- To minimise a smooth function: set the derivative to 0, solve, and check that the second derivative is positive.
- A finite-difference slope is a useful check of a hand-derived derivative.
