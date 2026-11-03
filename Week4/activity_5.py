def climb_ladder (stp_remaining, stp_crossed):
    if stp_remaining > stp_crossed:
        print('Still some way to go!')
    else:
        print('We are almost there!')

climb_ladder(3,2)
climb_ladder(2,3)