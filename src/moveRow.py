def moveRow(horizontaldist,horizontalDir,speed, device):

    from src.moveDist import movedist

# -------------------------------------------------------------------------
# TODO: Move up
# -------------------------------------------------------------------------

    movedist(distance=10, direction=1,speed=speed,device=device) #move up off of the plate

# -------------------------------------------------------------------------
# TODO: Move to next node in the row, make sure horizontalDirection is compatiable with -1 or 1
# -------------------------------------------------------------------------

    trueHorzDir = horizontalDir #convert -1 or 1 to direction
    movedist(distance=horizontaldist, direction=trueHorzDir,speed=speed,device=device)

# -------------------------------------------------------------------------
# TODO: Move down
# -------------------------------------------------------------------------
    from src.moveSense import movesense
    movesense()

    return;

