from Point import *
from Color import *
import time
import numpy
import math 
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import sys
import collections

class Canvas(object):
    X_MIN = 0
    X_MAX = 20
    Y_MIN = 0
    Y_MAX = 20

    @staticmethod
    def createPointsN(number):
        listOfPoints = []
        for i in range(number):
            x = randint(1,16)
            y = randint(1,16)
            if True == Point.checkExistingPoint(Point(x,y),listOfPoints):
                i -= 1
                continue
            color = "white"
            listOfPoints.append(Point(x,y,color))
        return listOfPoints

    @staticmethod
    def createCentroidsN(number):
        listOfCentroids = Canvas.createPointsN(number)
        Canvas.changeColor(listOfCentroids)
        return listOfCentroids

    @staticmethod
    def plotPoints(clusters,listOfPoints, listOfCentroids):
        index = 1
        cluster = {}
        while True:

            for x in range(len(listOfCentroids)):
                print "###->/" + str(listOfCentroids[x])
            Canvas.computeCluster(listOfPoints,listOfCentroids)
            cluster.clear()
            print cluster
            cluster = Canvas.createClusters(listOfPoints, listOfCentroids) 
            # for i in listOfPoints:
            #     print str(i)
            plt.ion()
            plt.figure(index)
            index +=1
            plt.title("K-means clustering")

            Canvas.displayCentroids(listOfCentroids)
            Canvas.displayPoints(cluster)

            plt.axis([Canvas.X_MIN, Canvas.X_MAX, Canvas.Y_MIN, Canvas.Y_MAX])            
            plt.draw()
            Canvas.updateCentroid(listOfPoints,listOfCentroids)
            if Canvas.isFinished(listOfPoints, listOfCentroids) != False or index == 15:
                Canvas.displayCluster(cluster,listOfPoints, listOfCentroids)
                break

    @staticmethod
    def displayCluster(cluster, listOfPoints, listOfCentroids):
        Canvas.computeCluster(listOfPoints,listOfCentroids)
        plt.ion()
        plt.figure()
        plt.title("Final State: K-means clustering")
        Canvas.displayPoints(cluster)
        Canvas.displayCentroids(listOfCentroids)
        plt.axis([Canvas.X_MIN, Canvas.X_MAX, Canvas.Y_MIN, Canvas.Y_MAX])
        plt.draw()

    @staticmethod
    def isFinished(listOfPoints, listOfCentroids):
        for element in listOfPoints:
            tempCent = Canvas.getCloserCentroid(element,listOfCentroids)
            if element.color != tempCent.color:
                print "Current element : " + str(element) + ": Centroid: " + str(tempCent)
                return False
        return True
       
    @staticmethod
    def displayCentroids(listOfCentroids):
        keys = []
        values = []
        for element in listOfCentroids:
            keys.append(element.color)
            values.append([[],[]])
        dictionary = dict(zip(keys, values))
        for element in listOfCentroids:
            dictionary[element.color][0].append(element.x)
            dictionary[element.color][1].append(element.y)
        for key in dictionary.keys():
            temp = dictionary.get(key)
            Xl = temp[0]
            Yl = temp[1]
            plt.plot(Xl,Yl, linestyle='', marker='^', color=Color.colors[key])

    @staticmethod
    def displayPoints(currentCluster):
        print currentCluster
        for key in currentCluster.keys():
            temp = currentCluster.get(key)
            Xl = temp[0]
            Yl = temp[1]
            plt.scatter(Xl, Yl, 50,c= Color.colors[key], alpha=0.5)


    @staticmethod
    def createClusters(listOfPoints, listOfCentroids):
        keys = []
        values = []
        dictionary = []
        for element in listOfCentroids:
            keys.append(element.color)
            values.append([[],[]])
        dictionary = dict(zip(keys, values))

        for element in listOfPoints:
            dictionary[element.color][0].append(element.x)
            dictionary[element.color][1].append(element.y)

            print element.color  + " : " + str(dictionary[element.color])     
        return dictionary

    @staticmethod
    def computeCluster(listOfPoints, listOfCentroids):
        for element in listOfPoints:
            print "Computing for : " + str(element)
            tempCent = Canvas.getCloserCentroid(element,listOfCentroids)
            element.color = tempCent.color
            print "Computed for : " + str(element)
        print "_______________________________________________" + str("\n")
    
    @staticmethod
    def getCloserCentroid(point, listOfCentroids):
        minDistanse  = sys.float_info.max
        closestCent = listOfCentroids[0]
        for element in listOfCentroids:
            distanse = Point.calculateDistance(point,element)
            # print "Distanse  "+ str(distanse) + " between Point :" + str(point) + " and Centroid: " + str(element)

            if distanse < minDistanse:
                minDistanse = distanse
                closestCent = element
        return closestCent

    @staticmethod
    def updateCentroid(listOfPoints, listOfCentroids):
        AllX = 0
        AllY = 0
        InCluster = 0
    
        for elementCent in listOfCentroids:
            for elementPnt in listOfPoints:
                if(elementPnt.color == elementCent.color):
                    AllX += elementPnt.x
                    AllY += elementPnt.y
                    InCluster += 1
            
            if(InCluster > 0):
                elementCent.x = (AllX / InCluster)
                elementCent.y = (AllY / InCluster)
        
    @staticmethod
    def changeColor(listOfPoints):
        colorIndex = 2
        for index in range(len(listOfPoints)):
            if colorIndex >= len(listOfPoints):
                colorIndex = 0
            else:
                colorIndex = index
            listOfPoints[index].color = Color.colors.keys()[colorIndex]
