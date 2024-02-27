def pictureGrid(grid):
    for row in grid:
        for character in row:
            print(str(character), end='')
        print('')

pictureGrid([['a',1,'c'], \
              ['d','e',True], \
              ['g',-17.546,'i']])
