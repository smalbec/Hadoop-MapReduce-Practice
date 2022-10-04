hadoop makes you install the libraries the only one you need is 

$ sudo pip install feedparser==5.2.1

Instructions to deploy:

1. Start Hadoop by running:

start-hadoop.sh

3. Make a new directory on hdfs for the input files:
hdfs dfs -mkdir input

4. Copy the local directory APIcalls/ to the hdfs directory :
hdfs dfs -copyFromLocal $HOME/APIcalls input/APIcalls

5. Make sure you copied them to the right place:
hdfs dfs -ls input/APIcalls

6. Create two files - mapper.py and reducer.py and copy in the source code provided, make sure that they are located in $HOME/hadoop

7. Now run the MapReduce job by executing this command

hadoop jar $HOME/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.4.jar \
-file $HOME/mapper.py -mapper $HOME/mapper.py \
-file $HOME/reducer.py -reducer $HOME/reducer.py \
-input input/APIcalls/* -output output/authorcount

Note: make sure you specify new output file for every job or delete the old one.

8. You can now view the results by running:
hdfs dfs -cat output/authorcount/*

Or if you need the results locally, copy from hdfs then cat:
hdfs dfs -copyToLocal output/ $HOME/output

9. Make sure you always stop the HDFS file system before you leave. You can save the
current exploration.
stop-hadoop.sh

Note: There is a bug that makes solitary authors get printed twice, this only happens when the code is used through hadoop not locally. After many hours of trying to fix and no help online I’ve had to leave it there. Others online have had the same problem but without any solution 
https://stackoverflow.com/questions/19011036/hadoop-output-file-has-double-output
