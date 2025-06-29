class solid_collider():
    # meant for convex polygons
    def __init__(self, contour, center_of_mass = None):
        if isinstance(contour, list):
            self.contour = contour
        else:
            raise TypeError(f"ERROR: Invalid type for contour. Expected `list`, got `{type(contour)}`")
        if isinstance(center_of_mass,tuple) or isinstance(center_of_mass,list):
            self.center_of_mass = tuple(center_of_mass)
        elif isinstance(center_of_mass, type(None)):
            self.calculate_center()
        else:
            raise TypeError(f"ERROR: Invalid type for center_of_mass. Expected `list`, `tuple`, or `None`, got `{type(contour)}`")

    def calculate_center(self):
        center = (0,0)
        count = 0
        for edge in self.contour:
            for point in edge:
                center = (center[0]+point[0],center[1]+point[1])
                count+=1
        center = (center[0]/count,center[1]/count)
        
    def collides_with(self, other):
        for a in self.contour:
            for b in other.contour:
                if a[0] in b or a[1] in b:
                    return True
                # find point of intersection or parallelness
                # test for counding box collision
                if min([a[0][0],a[1][0]]) >= max([b[0][0], b[1][0]]) and min([a[0][1],a[1][1]]) >= max([b[0][1], b[1][1]]):
                    pass
                else:
                    continue
                    
                # determine delta vectors
                d_a = (a[0][0] - a[1][0], a[0][1] - a[1][1])
                d_b = (b[0][0] - b[1][0], b[0][1] - b[1][1])

                # Check for verticality
                a_vertical = d_a[0]==0
                b_vertical = d_b[0]==0
                
                # if both lines are vertical
                if a_vertical and b_vertical and a[0][0]==b[0][0]:
                    return True
                else:
                    continue
                
                # if only one is vertical
                if a_vertical or b_vertical:
                    if b_vertical:
                        c=a
                        a=b
                        b=c
                    #wlog a_vertical and not b_vertical
                    if min([b[0][0],b[1][0]]) <= a[0][0] <= max([b[0][0],b[1][0]]):
                        return True
                    else:
                        continue
                
                # if neither vertical
                slope = d_a[1]
                intercept = a[0][1] - a[0][0]*slope
                y_0 = slope*b[0][0] + intercept
                y_1 = slope*b[1][0] + intercept
                
                # check if points in b are on line a
                if b[0][1] == y_0 or b[1][1] == y_1:
                    return True
                
                # check opposite signs
                if ( y_0 < b[0][1]) != (y_1 < b[1][1]):
                    return True
        # if no intersections...
        return False
        # ignores one object fully inside another.
        
class world():
    def __init__(self):
        self.elements = []

class player_controller():
    def __init__(self):
        pass


class camera():
    pass