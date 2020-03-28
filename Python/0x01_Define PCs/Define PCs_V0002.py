"""
this class has the defination of the PointCloud

#create new PC
pc = PointCloud([[0,0,0],[1,1,1],[0,0,0]],"pc1")
print(pc)


#add point, no points duplication allowed
pc.add_point([1,1,1])
print(pc)

#+
#union of tow point clouds
#adding point clouds (unioin point clouds, not duplicating points)
pc2 = PointCloud([[0,0,0],[1,1,1]],"pc2")
pc3 = pc + pc2
print(pc3)

#adding a point
pc3 = pc + [1,2,3]
print(pc3)


#adding a list of points
pc3 = pc + [[1,2,4],[1,2,3]]
print(pc3)


#-
#difference between first point cloud and the other point cloud
pc4 = PointCloud([[0,0,0]],"pc4")
print(pc4)
pc5 = pc3 - pc4
print(pc5)


pc6 = pc3 - [1,1,1]
print(pc6)

pc7=pc3 - [[1,2,3],[1,2,4]]
print(pc7)

#*
#intersection between two or more point cloud
pc8=PointCloud([[1,2,3],[2,3,4],[3,4,5],[1,3,4]],"pc8")
print(pc8)

#intersection with a point
print("9")
pc9 = pc8 * [1,2,3]
print(pc8)
print(pc9)

pc10 = pc8 * [0,0,0]
print(pc10)

#intersection with list of points
pc11 = pc8 * [[1,2,3],[0,0,0]]
print(pc11)

#intersection with a point cloud
pc13=PointCloud([[1,2,3],[2,3,4],[3,4,5],[1,3,4],[0,0,0]],"pc13")

pc14 = pc13 * pc8
print(pc14)


print(pc8)


#To Do:
#1_Check that each point has the same dimension (1,2,3...) using a variable rank
#2_better way to name the PointClouds
#3_read and write pcd files

"""

__version__="0.0.0.2"


class PointCloud():
    size = int()
    points = list()
    name = str()      
    def __init__(self,list_of_3_dim_lists_of_points, name = ""):
        self.points = []
        if(name!=""):print("creating new point cloud " + name + "...", end="")
        #print("checking name")
        if(type(name) != type(str())): raise TypeError("Point Cloud name is not a string")
        if(list_of_3_dim_lists_of_points==None) : return
        try:
            for point in list_of_3_dim_lists_of_points:
                #print("checking name")
                if(type(list_of_3_dim_lists_of_points) != type(list())): raise TypeError("points are not list");
                #if(len(point) != 3): raise ValueError("point is not in 3 dimension space");
                if(type(point) != type(list())): raise TypeError("point is not list");
                #print("checking coordinates")
                for coor in point:
                   if(type(coor) != type(int()) and type(coor) != type(float())): raise TypeError("coordinates are not numbers")               
                for point in list_of_3_dim_lists_of_points:
                    if(not point in self.points):
                        self.points.append(point)
            self.size=len(self.points)
            self.name = name
            if(name!=""):print("Done.")
        except TypeError as ex:
            print("Falied")
            print("TypeError:")
            if(str(ex) == "Point Cloud name is not a string") : print(ex,", make sure to use a string as a name for your point cloud")
            if(str(ex) == "points are not list") : print(ex,", put the points in a list using[]")
            if(str(ex) == "point is not list"): print(ex, ", put the point in a list using[]")
            if(str(ex) == "coordinates are not numbers") : print(ex, ", coordinates of each point must be numbers (integers or floats)")
            print(ex)
            
        except ValueError as ex:
            print("Falied")
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

    def add_point(self,list_of_x_y_z_coordinate):
        print("adding new point...",end="")
        try:
            if(list_of_x_y_z_coordinate in self.points):
                pass
            else:
                self.points.append(list_of_x_y_z_coordinate);self.size=1+self.size
            print("Done.")
        except BaseException as bex:
            print(bex)

    def __add__(self,PC):
        '''return (point cloud) the resullt of union two point clouds or apoint cloud with list of points or point cloud with a point as a list'''
        try:
            if(isinstance(PC, PointCloud)):
                print("adding point clouds...",end="")
                pc=self;pc.points = []
                for point in PC.points:
                    if(point in self.points):
                        pass
                    else:
                        pc.points.append(point)
                pc.size=len(pc.points);pc.name=self.name;
                print("Done.")
                return pc
            
            elif(type(PC)==type(list()) and type(PC[0])!=type(list())): #adding a point
                print("adding point...",end="")
                pc = self
                for coor in PC:
                    if(type(coor) != type(int()) and type(coor) != type(float())): raise TypeError("coordinates are not numbers")
                if(not PC in pc.points) : pc.points+=[PC] 
                pc.size=len(pc.points)
                print("Done.")
                return pc
                
            elif(type(PC)==type(list()) and type(PC[0])==type(list())): #adding list of points
                print("adding points...",end="")
                pc = self
                for point in PC:
                    for coor in point:
                        if(type(coor) != type(int()) and type(coor) != type(float())): raise TypeError("coordinates are not numbers")
                for point in PC:
                    if not (point in pc.points):
                        pc.points.append(point)
                pc.size=len(pc.points)
                pc.name = pc.name + "_n" +str(pc.size)
                print("Done.")
                return pc

            else:
                raise TypeError("not adding to PointCloud")
                
        except TypeError as te:
            print("Failed")
            print("TypeError:")
            print(te,end="")
            if(str(te) == "not adding to PointCloud") : print(te,", addition of PointClouds works only PointClouds make sure to add only PointClouds or list of points or a point")
            if(str(te) == "coordinates are not numbers") : print(te,", coordinates of each point must be numbers (integers or floats)")
            return None
        except BaseException as be:
            print(be)

    def __sub__(self,PC):
        '''return (point cloud) the resullt of differece of two point clouds or apoint cloud with list of points or point cloud with a point as a list'''
        try:
            if(isinstance(PC, PointCloud)):
                print("subtracting point clouds...",end="")
                pc = self;new_points = [];               
                for point in self.points:
                    if not(point in PC.points):
                        new_points.append(point)
                pc.points = new_points
                pc.size = len(pc.points);pc.name=self.name+"-"+PC.name;
                print("Done.")
                return pc
            
            elif(type(PC)==type(list()) and type(PC[0])!=type(list())): #subtracting a point
                print("subtracting point...",end="")
                pc = self;new_points = [];
                for coor in PC:
                    if(type(coor) != type(int()) and type(coor) != type(float())): raise TypeError("coordinates are not numbers")
                for point in self.points:
                    if(point != PC): new_points+=[point]
                pc.points = new_points
                pc.size=len(pc.points)
                print("Done.")
                return pc
                
            elif(type(PC)==type(list()) and type(PC[0])==type(list())): #subtracting list of points
                print("subtracting points...",end="")
                pc = self;new_points = [];
                for point in PC:
                    for coor in point:
                        if(type(coor) != type(int()) and type(coor) != type(float())): raise TypeError("coordinates are not numbers")
                for point in self.points:
                    if not (point in PC):
                        new_points+=[point]
                pc.points = new_points
                pc.size=len(pc.points)
                pc.name = pc.name + "_n" +str(pc.size)
                print("Done.")
                return pc

            else:
                raise TypeError("not subtracting to PointCloud")
                
        except TypeError as te:
            print("Failed")
            print("TypeError:")
            print(te,end="")
            if(str(te) == "not subtracting to PointCloud") : print(te,", subtracting of PointClouds works only PointClouds make sure to add only PointClouds or list of points or a point")
            if(str(te) == "coordinates are not numbers") : print(te,", coordinates of each point must be numbers (integers or floats)")
            return None
        except BaseException as be:
            print(be)


    def __mul__(self, PC):
        '''return (point cloud) the resullt of intersection of two point clouds or apoint cloud with list of points or point cloud with a point as a list'''
        try:
            if(isinstance(PC, PointCloud)):
                print("intersection point clouds...",end="")
                pc = PointCloud(None);new_points = [];               
                for point in self.points:
                    if (point in PC.points):
                        new_points.append(point)
                pc.points = new_points
                pc.size = len(pc.points);pc.name=self.name+"*"+PC.name;
                print("Done.")
                return pc
            
            elif(type(PC)==type(list()) and type(PC[0])!=type(list())): #subtracting a point
                print("intersection point...",end="")
                pc = PointCloud(None);new_points = [];
                for coor in PC:
                    if(type(coor) != type(int()) and type(coor) != type(float())): raise TypeError("coordinates are not numbers")
                if(PC in self.points): new_points+=[PC]
                pc.points = new_points
                pc.size=len(pc.points)
                print("Done.")
                return pc
                
            elif(type(PC)==type(list()) and type(PC[0])==type(list())): #subtracting list of points
                print("subtracting points...",end="")
                pc = PointCloud(None);new_points = [];
                for point in PC:
                    for coor in point:
                        if(type(coor) != type(int()) and type(coor) != type(float())): raise TypeError("coordinates are not numbers")
                for point in PC:
                    if (point in self.points):
                        new_points+=[point]
                pc.points = new_points
                pc.size=len(pc.points)
                pc.name = pc.name + "_n" +str(pc.size)
                print("Done.")
                return pc

            else:
                raise TypeError("not subtracting to PointCloud")
                
        except TypeError as te:
            print("Failed")
            print("TypeError:")
            print(te,end="")
            if(str(te) == "not intersection to PointCloud") : print(te,", intersecting of PointClouds works only PointClouds make sure to add only PointClouds or list of points or a point")
            if(str(te) == "coordinates are not numbers") : print(te,", coordinates of each point must be numbers (integers or floats)")
            return None
        except BaseException as be:
            print(be)


               
        
#create new PC
pc = PointCloud([[0,0,0],[1,1,1],[0,0,0]],"pc1")
print(pc)


#add point, no points duplication allowed
pc.add_point([1,1,1])
print(pc)

#+
#union of tow point clouds
#adding point clouds (unioin point clouds, not duplicating points)
pc2 = PointCloud([[0,0,0],[1,1,1]],"pc2")
pc3 = pc + pc2
print(pc3)

#adding a point
pc3 = pc + [1,2,3]
print(pc3)


#adding a list of points
pc3 = pc + [[1,2,4],[1,2,3]]
print(pc3)


#-
#difference between first point cloud and the other point cloud
pc4 = PointCloud([[0,0,0]],"pc4")
print(pc4)
pc5 = pc3 - pc4
print(pc5)


pc6 = pc3 - [1,1,1]
print(pc6)

pc7=pc3 - [[1,2,3],[1,2,4]]
print(pc7)

#*
#intersection between two or more point cloud
pc8=PointCloud([[1,2,3],[2,3,4],[3,4,5],[1,3,4]],"pc8")
print(pc8)

#intersection with a point
print("9")
pc9 = pc8 * [1,2,3]
print(pc8)
print(pc9)

pc10 = pc8 * [0,0,0]
print(pc10)

#intersection with list of points
pc11 = pc8 * [[1,2,3],[0,0,0]]
print(pc11)

#intersection with a point cloud
pc13=PointCloud([[1,2,3],[2,3,4],[3,4,5],[1,3,4],[0,0,0]],"pc13")

pc14 = pc13 * pc8
print(pc14)


print(pc8)


#To Do:
#1_Check that each point has the same dimension (1,2,3...) using a variable rank
#2_better way to name the PointClouds
#3_read and write pcd files





