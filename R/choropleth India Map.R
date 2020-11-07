# Title     : TODO
# Objective : TODO
# Created by: vradja
# Created on: 10/23/20

library(ggplot2)
library(maptools)
library(rgeos)
library(Cairo)
library(ggmap)
library(scales)
library(RColorBrewer)
set.seed(8000)

##set directory to the folder where the shapefile is, then input shapefile
setwd("/Users/vradja/Downloads/IND_adm")
states.shp <- readShapeSpatial("IND_adm1.shp")
class(states.shp)