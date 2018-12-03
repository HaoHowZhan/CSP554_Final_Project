CREATE external TABLE cjp.all_crimes(
id string,
casenumber string,
caldate string,
block string,
iucr string,
primarytype string,
description string,
locationdescription string,
arrest boolean,
domestic boolean,
beat string,
district string,
ward string,
communityarea string,
fbicode string,
xcoordinate string,
ycoordinate string,
year string,
updatedon string,
latitude decimal(10,0),
longitude decimal(10,0),
location string
)
row format delimited fields terminated by ','
stored as textfile
location '/user/maria_dev/data/crimes';