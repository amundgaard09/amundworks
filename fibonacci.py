

# ------------------------------------------------- # fibonacci calculator
while True:                                         # repeater
    try:                                            # failsafe
        MOO = int(input("list or int? (1, 2):"))    # user input
        if MOO < 1 or MOO > 2:                      # filter
            print("invalid number")                 # error feedback
            continue                                # restarter
    except ValueError:                              # filter
        print("invalid input")                      # error feedback
        continue                                    # restarter
# ------------------------------------------------- #
    if MOO == 1:                                    # list mode
        try:                                        # failsafe
            n = int(input("how many fibs:"))        # user input
            if n < 1:                               # filter
                print("invalid number")             # error feedback
                continue                            # restarter
        except ValueError:                          # filter
            print("invalid input")                  # error feedback
            continue                                # restarter
# - - - - - - - - - - - - - - - - - - - - - - - - - #
        totalfib = [0, 1]                           # list starter
        fib0, fib1 = 0, 1                           # variable starter
        for i in range(0,(n-2)):                    # repeater
            newfib = fib0 + fib1                    # fibonacci calculator module
            fib0 = fib1                             # fibonacci calculator module 
            fib1 = newfib                           # fibonacci calculator module
            totalfib.append(newfib)                 # list adder
        goldenratio = newfib/fib0                   # golden ratio calculator module
        print(totalfib)                             # printer
        print(f"golden ratio:{goldenratio}")        # printer
# ------------------------------------------------- #
    elif MOO == 2:                                  # single int mode                              
        try:                                        # failsafe
            n = int(input("which fib:"))            # user input 
            if n < 1:                               # filter
                print("invalid number")             # error feedback
                continue                            # restarter
        except ValueError:                          # filter
            print("invalid input")                  # error feedback
            continue                                # restarter
# - - - - - - - - - - - - - - - - - - - - - - - - - #
        fib0, fib1 = 0, 1                           # variable starter
        for i in range (0,(n-2)):                   # repeater
            newfib = fib0 + fib1                    # fibonacci calculator module
            fib0 = fib1                             # fibonacci calculator module
            fib1 = newfib                           # fibonacci calculator module
        lastfib = newfib                            # last fibonacci int definer
        goldenratio = lastfib/fib0                  # golden ratio calculator module
        print(f"{n}th fib: {lastfib}")              # printer 
        print(f"golden ratio: {goldenratio:.100f}") # printer
# ------------------------------------------------- #

