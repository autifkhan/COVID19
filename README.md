# COVID19

## Requirements
uuid
thttpd web server
Python
bash

## Starting the thttpd server
thttpd -C thttpd.config

## Stopping the thttpd server
killall -USR1 thttpd

## Set up
Download COVID-19 repo from https://github.com/CSSEGISandData/COVID-19.git
ln -s COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv confirmed

## Usage
Go to http://localhost:8080/index.html?XX,YY
where XX is the line number in 'confirmed' file for line on graph
and YY is the line number in the 'confirmed' file for the points

For example, http://localhost:8080/index.html/18,101 for Italy and NY state

