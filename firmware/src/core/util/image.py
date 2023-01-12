def readImageBin(path, width=296, height=128):
    BADGE_IMAGE = bytearray(int(width * height / 8))
    open(path, "rb").readinto(BADGE_IMAGE)
    return BADGE_IMAGE