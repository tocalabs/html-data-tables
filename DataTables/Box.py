class Box:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.max_x = int(x) +  int(w)
        self.max_y = int(y) + int(h)

    def intersection(self, otherbox):
        x_overlap = (self.max_x >= otherbox.x and otherbox.max_x >= self.x) or (self.x >= otherbox.max_x and otherbox.x >= self.max_x)
        y_overlap = (self.max_y >= otherbox.y and otherbox.max_y >= self.y) or (self.x >= otherbox.max_y and otherbox.x >= self.max_y)
        return x_overlap and y_overlap