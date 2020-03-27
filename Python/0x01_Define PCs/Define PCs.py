class PointXYZ:
    x = float()
    y = float()
    z = float()
    
class PointCloud():
    size = int()
    points = list()
    name = str()
    def __init__(self):
        pass

    def __init__(self,list_of_3_dim_lists_of_points, name = ""):
        #print("checking name")
        if(type(name) != type(str())): raise TypeError("Point Cloud name is not a string")
        try:
            for point in list_of_3_dim_lists_of_points:
                #print("checking name")
                if(type(list_of_3_dim_lists_of_points) != type(list())): raise TypeError("points are not list");
                if(len(point) != 3): raise ValueError("point is not in 3 dimension space");
                if(type(point) != type(list())): raise TypeError("point is not list");
                #print("checking coordinates")
                for coor in point:
                   if(type(coor) != type(int()) and type(coor) != type(float())): raise TypeError("coordinates are not numbers")
            self.points+=list_of_3_dim_lists_of_points                  
            #print("adding points")
            self.size=len(self.points)
            self.name = name
            
        except TypeError as ex:
            print("TypeError:")
            if(str(ex) == "Point Cloud name is not a string") : print(ex,", make sure to use a string as a name for your point cloud")
            if(str(ex) == "points are not list") : print(ex,", put the points in a list using[]")
            if(str(ex) == "point is not list"): print(ex, ", put the point in a list using[]")
            if(str(ex) == "coordinates are not numbers") : print(ex, ", coordinates of each point must be numbers (integers or floats)")

        except ValueError as ex:
            print("ValueError:")
            print(ex, ", each point must have x, y, and z coordiante")
            #print(ex)


    def __str__(self):
        summary = ""
        summary += "\n" + "-"*20
        summary += "\n" + "point cloud name: "+ str(self.name)
        summary += "\n" + "point cloud size: "+ str(self.size)
        if(self.size == 0):
            summary += "\n" + "point cloud is empty"
        else:
            summary += "\n" + "points\nx\ty\tz\t\n"
            for point in self.points: summary += str(point[0])+"\t"+str(point[1])+"\t"+str(point[2])+"\n"
        summary += "\n" + "-"*20
        return summary

    def remove_duplicated_points(self):
        new_points = []
        print("removeing dunplicated points...",end="")
        for point in self.points:
            if(not point in new_points):
                new_points.append(point)
        self.points = new_points
        self.size = len(new_points)
        print("Done.")

    def add_point(self,list_of_x_y_z_coordinate):
        print("adding new point...",end="")
        try:
            self.__init__([list_of_x_y_z_coordinate], self.name)
            print("Done.")
        except BaseException as bex:
            print(bex)
        
#create new PC
pc = PointCloud([[0,0,0],[1,1,1]],"pc1")
print(pc)

#add point
pc.add_point([1,1,1])
print(pc)

#remove duplicated points
pc.remove_duplicated_points()
print(pc)

#adding point clouds (unioin point clouds, not duplicating points)

#difference between first point cloud and the other point cloud

#intersection between two or more point cloud




