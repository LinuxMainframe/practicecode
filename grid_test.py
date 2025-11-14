"""
	Random code I was messing around with when I discovered some weird behavior.
	It seems to be a python3 list/array behavior, but its kinda cool.
	This is just a note so I can reference it later if need be.

	Aidan A. Bradley
	Sometime in October 2025
"""

grid = [[0] * 3] * 3
test = [[0] * 3]
test2 = [0] * 3


print(grid)
print(test)
print(test2)
print(grid[0][0])
grid[0][0] = 3
print(grid)
print(grid[0][0])

"""

```markdown
# Python List Multiplication Thing (wtf)

okay so i was messing around with lists and found something weird

## What I Did

```python
grid = [[0] * 3] * 3
grid[0][0] = 3
print(grid)
# Output: [[3, 0, 0], [3, 0, 0], [3, 0, 0]]
```

like why did ALL the rows change??? i only changed `grid[0][0]`

## What's Actually Happening

so apparently when you do `[[0] * 3] * 3`, python doesn't make 3 different lists. it makes ONE list and then just... copies the reference to it 3 times?

basically:
```
grid = [pointer, pointer, pointer]
         |        |        |
         +--------+--------+---> [0, 0, 0]
                                 (same list)
```

so when you change one, they ALL change because they're literally the same list in memory. kinda mind-blowing tbh

## Why This Confused Me

i thought `*` would like... duplicate the list properly. but nope. it just makes multiple references to the same thing.

this works fine with regular numbers:
```python
test = [0] * 3  # [0, 0, 0] - this is fine
```

because numbers are immutable (can't be changed in place) so python doesn't care if they share references

but with LISTS inside lists? total disaster

## The Fix

use list comprehension instead:
```python
grid = [[0] * 3 for _ in range(3)]
```

this actually makes 3 separate lists. each iteration of the loop creates a NEW list instead of copying references

## Testing It

```python
# bad way
bad_grid = [[0] * 3] * 3
bad_grid[0][0] = 99
print(bad_grid)  # [[99, 0, 0], [99, 0, 0], [99, 0, 0]] <- bruh

# good way
good_grid = [[0] * 3 for _ in range(3)]
good_grid[0][0] = 99
print(good_grid)  # [[99, 0, 0], [0, 0, 0], [0, 0, 0]] <- nice
```

## tldr

- `[[0] * 3] * 3` = bad (copies references)
- `[[0] * 3 for _ in range(3)]` = good (makes new lists)
- this is apparently a super common mistake lol
```
"""