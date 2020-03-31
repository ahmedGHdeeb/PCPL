#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>

using namespace std;

void printPC(pcl::PointCloud<pcl::PointXYZ>::Ptr cloud)
{
for (size_t i = 0; i < cloud->points.size (); ++i)
{std::cout << "    " << cloud->points[i].x << " "    << cloud->points[i].y<< " "    << cloud->points[i].z << std::endl;}
}

void add_point(pcl::PointCloud<pcl::PointXYZ>::Ptr cloud,float point[3])
{
	pcl::PointXYZ Npoint;
	{Npoint.x=point[0];Npoint.y=point[1];Npoint.z=point[2];cloud->push_back(Npoint);}
}

void add_points(pcl::PointCloud<pcl::PointXYZ>::Ptr cloud, int number_of_points,float points[][3])
{
	pcl::PointXYZ Npoint;
	for(int i = 0;i < number_of_points; i++)
	{Npoint.x=points[i][0];Npoint.y=points[i][1];Npoint.z=points[i][2];cloud->push_back(Npoint);}
}


void concatenate_clouds(pcl::PointCloud<pcl::PointXYZ>::Ptr cloud,pcl::PointCloud<pcl::PointXYZ>::Ptr cloud1,pcl::PointCloud<pcl::PointXYZ>::Ptr cloud2){
	for(int i = 0;i < cloud1->points.size();i++){cloud->points.push_back(cloud1->points[i]);}
	for(int i = 0;i < cloud2->points.size();i++){cloud->points.push_back(cloud2->points[i]);}
}

void intersection_clouds(pcl::PointCloud<pcl::PointXYZ>::Ptr cloud,pcl::PointCloud<pcl::PointXYZ>::Ptr cloud1,pcl::PointCloud<pcl::PointXYZ>::Ptr cloud2){
	bool point_i = true;
	for(int i = 0;i < cloud1->points.size();i++){
		point_i = false;
		for(int j = 0;j < cloud2->points.size();j++){
			if(cloud1->points[i].x==cloud2->points[j].x && cloud1->points[i].y==cloud2->points[j].y && cloud1->points[i].z==cloud2->points[j].z)
				point_i = true;
		}
		if(point_i){cloud->points.push_back(cloud1->points[i]);}
	}
}

void union_clouds(pcl::PointCloud<pcl::PointXYZ>::Ptr cloud,pcl::PointCloud<pcl::PointXYZ>::Ptr cloud1,pcl::PointCloud<pcl::PointXYZ>::Ptr cloud2){
	bool point_u = true;
	for(int i = 0;i < cloud1->points.size();i++){
		point_u = true;
		for(int j = 0;j < cloud->points.size();j++){
			if(cloud1->points[i].x==cloud->points[j].x && cloud1->points[i].y==cloud->points[j].y && cloud1->points[i].z==cloud->points[j].z)
				point_u = false;
		}
		if(point_u){cloud->points.push_back(cloud1->points[i]);}
	}
		for(int i = 0;i < cloud2->points.size();i++){
		point_u = true;
		for(int j = 0;j < cloud->points.size();j++){
			if(cloud2->points[i].x==cloud->points[j].x && cloud2->points[i].y==cloud->points[j].y && cloud2->points[i].z==cloud->points[j].z)
				point_u = false;
		}
		if(point_u){cloud->points.push_back(cloud2->points[i]);}
	}
}
int main (int argc, char** argv)
{
	 std::string wait;
	 pcl::PointCloud<pcl::PointXYZ>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZ>);
	 std::cout<<"add point[s]\n";
	 //add point
	 float point[3] = {1,2,3};
	 add_point(cloud,point);

	 //add points
	 float points[3][3] = {{1,2,3},{1,2,4},{0,0,0}};
	 add_points(cloud,3,points);
	 printPC(cloud);

	 //create test points clouds
	 pcl::PointCloud<pcl::PointXYZ>::Ptr cloud1 (new pcl::PointCloud<pcl::PointXYZ>);
	 pcl::PointCloud<pcl::PointXYZ>::Ptr cloud2 (new pcl::PointCloud<pcl::PointXYZ>);
	 float points1[2][3] = {{1,1,1},{2,2,2}};
	 float points2[3][3] = {{2,2,2},{3,3,3}};
	 add_points(cloud1,2,points1);
	 add_points(cloud2,2,points2);
	 
	 //clouds concatenation
	 std::cout<<"clouds concatenation\n";
	 pcl::PointCloud<pcl::PointXYZ>::Ptr con_cloud (new pcl::PointCloud<pcl::PointXYZ>);
	 concatenate_clouds(con_cloud,cloud1,cloud2);
	 printPC(con_cloud);

	 //clouds intersection
	 std::cout<<"clouds intersection\n";
	 pcl::PointCloud<pcl::PointXYZ>::Ptr int_cloud (new pcl::PointCloud<pcl::PointXYZ>);
	 intersection_clouds(int_cloud,cloud1,cloud2);
	 printPC(int_cloud);
	 
	 //clouds union
	 std::cout<<"clouds union\n";
	 pcl::PointCloud<pcl::PointXYZ>::Ptr uni_cloud (new pcl::PointCloud<pcl::PointXYZ>);
	 union_clouds(uni_cloud,cloud1,cloud2);
	 printPC(uni_cloud);

	 
	 std::cin>>wait;
  return (0);
}
