### day5
man pythons range function just bit me pretty hard
range(9) prints 0 - 8
sure, no problem, do range(9 + 1)
but then I had to do +1 for coords too - and then that printed a lot of x=0, y=1 coords

I think my main mistake was not understanding I had two points and the coordinates within them
I was trying to do inclusive loop from start to <= max_value - to include the last point
but then doing + 1 meant on straight lines, that I would always double the final value.. Something like that
Just needed those if statements: if x1 != x2