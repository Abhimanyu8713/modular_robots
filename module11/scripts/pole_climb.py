#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import Float64
from std_msgs.msg import String
import math 
count =0 
theta = 0
class snakeBot(object):
	def __init__(self):
		self.publishers_list=[]
		self.angle=[0,0,0,0,0,0,0,0,0,0]
		self.RFH=rospy.Publisher('/snakeBot/RFH_position_controller/command',Float64, queue_size=1)
		self.LFV=rospy.Publisher('/snakeBot/LFV_position_controller/command',Float64, queue_size=1)
		self.LSH=rospy.Publisher('/snakeBot/LSH_position_controller/command',Float64, queue_size=1)
		self.LSV=rospy.Publisher('/snakeBot/LSV_position_controller/command',Float64, queue_size=1)
		self.LTH=rospy.Publisher('/snakeBot/LTH_position_controller/command',Float64, queue_size=1)
		self.LTV=rospy.Publisher('/snakeBot/LTV_position_controller/command',Float64, queue_size=1)
		self.LFrH=rospy.Publisher('/snakeBot/LFrH_position_controller/command',Float64, queue_size=1)
		self.LFrV=rospy.Publisher('/snakeBot/LFrV_position_controller/command',Float64, queue_size=1)
		self.LFiH=rospy.Publisher('/snakeBot/LFiH_position_controller/command',Float64, queue_size=1)
		self.LFiV=rospy.Publisher('/snakeBot/LFiV_position_controller/command',Float64, queue_size=1)

		self.publishers_list.append(self.RFH)
		self.publishers_list.append(self.LFV)
		self.publishers_list.append(self.LSH)
		self.publishers_list.append(self.LSV)
		self.publishers_list.append(self.LTH)
		self.publishers_list.append(self.LTV)
		self.publishers_list.append(self.LFrH)
		self.publishers_list.append(self.LFrV)
		self.publishers_list.append(self.LFiH)
		self.publishers_list.append(self.LFiV)

		self.k=0
		self.j=0
		self.PI=math.pi
		self.count= 4
		self.ll = self.PI/2
		self.sl = self.PI/4
		self.sr = -self.PI/4
		self.sl = -self.PI/2
		self.angle=[0,0,0,0,0,0,0,0,0,0]
		            

	def publishAngle(self,angles):
		i=0
		for pubs in self.publishers_list:
			jointAngles=Float64()
			jointAngles.data=angles[i]
			pubs.publish(jointAngles)
			i=i+1


	
	def generateAngle(self):
		#self.count=self.count+1

		if self.count<40:
			if  (self.count%10) == 0:
				self.angle[0] = -2*(self.PI/6)
			else:
				self.angle[self.count%10] = 2*(self.PI/6)

			self.publishAngle(self.angle)
			self.count = self.count +2
			print self.count
		if self.count>=40:
			self.angle=[0,0,0,0,0,0,0,0,0,0]
			self.angle[5]= self.PI/3
			self.angle[7]= -self.PI/3
			self.angle[6]= self.PI/3
			self.angle[8]= -self.PI/3

			self.publishAngle(self.angle)
			self.count = self.count +2
			print self.count
		

if __name__=="__main__":
	rospy.init_node('joint_publisher_node')
	rate_value = 10
	snakeBot_control=snakeBot() 
	rate = rospy.Rate(rate_value)
	while not rospy.is_shutdown():
		snakeBot_control.generateAngle()
		rate.sleep()
			
