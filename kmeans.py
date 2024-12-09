import csv
import pprint
import random

def kmeans(filename, k, epsilon, iterations):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)

        data = [row for row in reader]

        centroids = []
        centroidIndices = random.sample(range(1, len(data)), k)
        print(centroidIndices)
        i = 0
        while(i < k):
            centroids.append(data[centroidIndices[i]])
            i += 1

        print(centroids)

        clusters = [[] for i in range(len(centroids))]

        sumSqErr = 0

        i = 0
        while(i < iterations):

            tempClusters = [[] for i in range(len(centroids))]

            #reassign points to nearest cluster
            for ipoint, point in enumerate(data):
                if ipoint != 0:
                    distance = []
                    for centroid in centroids:
                        sum = 0
                        for ix, x in enumerate(point):
                            sum = sum + (float(x) - float(centroid[ix])) ** 2
                        distance.append(sum)

                    closestCentroid = distance.index(min(distance))
                    tempClusters[closestCentroid].append(point)

            #recompute centroids
            for ic, centroid in enumerate(centroids):
                tempCenter = list(range(len(centroid)))

                for point in tempClusters[ic]:
                    for id, dimension in enumerate(point):
                        tempCenter[id] += float(dimension)

                centroids[ic] = [dimension / len(tempClusters[ic]) for dimension in tempCenter]
            
            clusters = tempClusters
            
            currSumSqErr = 0
            for ic, centroid in enumerate(centroids):
                for point in clusters[ic]:
                    for ix, x in enumerate(point):
                        currSumSqErr = currSumSqErr + (float(x) - float(centroid[ix])) ** 2

            
            if(abs(currSumSqErr - sumSqErr) < epsilon):
                sumSqErr = currSumSqErr
                break

            sumSqErr = currSumSqErr

            i += i + 1
        
        print("Clusters:")
        for ic, cluster in enumerate(clusters):
            print(str(ic) + ":")
            pprint.pprint(clusters[ic], width=65, compact=True)
        print("Cluster sizes:")
        for ic, cluster in enumerate(clusters):
            print(str(ic) + ": " + str(len(cluster)))
        print("Sum of Squared Error: " + str(sumSqErr))

kmeans("iris.csv", 4, .1, 20)