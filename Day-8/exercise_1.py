def paint_calc(height = 0, width = 0, cover = 0 ):
    number_of_cans = (height * width) / cover
    print("Number of cans should be", number_of_cans.round()

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
