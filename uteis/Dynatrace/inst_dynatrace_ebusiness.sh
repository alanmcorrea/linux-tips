#!/bin/bash

cd /ebusiness/shared

mkdir usr

cd usr

mkdir dynatrace

cd dynatrace

scp asv8z4@npaa1243:/home/ASV8Z4/tmp/*.jar .

PATH=$PATH:/oracle/apps/prd/jdk/jdk1.8.0_60/jre/bin

java -jar dynatrace-agent-6.3.0.1305-unix.jar Y
