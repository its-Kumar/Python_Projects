def find_cost(cost_per_tile, w, h):
    '''
        Return the total cost of tile to cover 
        WxH floor
    '''
    return cost_per_tile * (w*h)


w, h = (int(x) for x in input("Enter W and H : ").split())
cost_tile = float(input("Enter the cost per tile : "))
print("Total cost of tile to cover WxH floor : = {:.3f}".format(
    find_cost(cost_tile, w, h)))
