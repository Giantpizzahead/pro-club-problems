1. The easiest way to store Bessie's signal would be using a 2D array of characters (or an array of strings). It might also help to create another 2D array of characters storing the enlarged version of the signal. Then, try to find a way to convert each individual pixel of the original image into a bigger pixel in the enlarged image.

2. How could the below relationship be translated into code? (Each enlarged pixel is mapped to one of the original pixels.)
```text
Original image (K = 1):
12
34

K = 2:
1122
1122
3344
3344

K = 3:
111222
111222
111222
333444
333444
333444

...
```