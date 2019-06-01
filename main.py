usb_size = 1

memes = [('meme1.jpg', 205, 6),
         ('meme2.png', 410, 10),
         ('meme3.gif', 180, 5),
         ('meme4.gif', 200,7),
         ('meme5.bmp', 600, 12),
         ('meme6.elo', 702, 19),
         ('meme7.mp4', 819, 24),
         ('meme8.png', 13, 1),
         ('meme9.avi', 256, 10),
         ('meme10.avi', 300, 9),]



def calculate(usb_size, memes):
    """
        Takes two arguments and returns a tuple with solution and set of memes
        usb_size -- capacity of our memory
        memes -- list of tuples with memes
    """
    # calculate size of usb stick in MiB
    size_in_mb = usb_size * 1024
    # variable for the optimal solution
    sum_of_caps = 0
    # set for memes which our solution contains
    chosen_memes = set()
    # maximum size of usb stick
    maximum = 0
    # makes a list filled with 0s in dimension size / the num of memes
    list = [[0 for i in range(size_in_mb + 1)] for j in range(len(memes) + 1)]
    # nested for loops iterates through each cell of list
    for j in range(len(memes) + 1):
        for i in range(size_in_mb + 1):
            # fill first element of each row with 0
            if j == 0 or i == 0:
                list[j][i] = 0
            # check if previous column size is greater than column number
            elif memes[j - 1][1] > i:
                # if it's - fill up this cell with value from previous row cell
                list[j][i] = list[j - 1][i]
            else:
                # otherwise fill up this cell with return of max function.
                list[j][i] = max(memes[j - 1][2] + list[j - 1][i - memes[j - 1][1]], list[j - 1][i])
    # assign the last value from list to sum_of_caps - it's a solution of the problem
    sum_of_caps = list[len(memes)][size_in_mb]
    # make a temp variable for sum_of_caps
    max_val_caps = sum_of_caps
    # assign size of usb stick to maximum var for calculations
    maximum = size_in_mb
    # decreasing for loop from len(memes) to 1
    for i in range(len(memes), 0, -1):
        # ignore value if solution is equal to last column previous row cell value
        if max_val_caps == list[i - 1][maximum]:
            continue
        else:
            # otherwise add to chosen_memes set a meme with index i - 1
            chosen_memes.add(memes[i - 1][0])
            # decrease max_val_caps by value of this meme
            max_val_caps -= memes[i - 1][2]
            # and decrease maximum size by size of this meme
            maximum -= memes[i - 1][1]
    # return a tuple of solution and set of memes
    return (sum_of_caps, chosen_memes)

print(calculate(usb_size, memes))


