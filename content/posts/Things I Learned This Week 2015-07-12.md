title: Things I learned this week - July 12th 2015
date: 2015-08-03 18:45
tags: Gorskii Colorization; Terrible Decisions; Job Hunting; Fossil Fuels and Post-apocalyptic Rebuilding; NoSQL vs SQL; It's gone meta!

##Things I Learned This Week: July 12th 2015

To the surprise of absolutely no one, I managed to miss about three weeks of posts. Maybe I should actually just do a link dump instead of trying to summarize things. Anyway, here are some links from July. 

####Gorskii Colorization 
[Sergey Prokudin-Gorskii](https://en.wikipedia.org/wiki/Sergey_Prokudin-Gorsky#Photography_technique) was an early 20th-century photographer, whose claim to fame was basically doing color photography *before there was even a way to produce color photos*. Getting color information only via black and white photography involves taking the same photo three times, once with a red, green, or blue filter in order to capture each of the color channels. These were recombined by projecting them through colored filters, but now it seems to be a standard intro homework for computer vision courses to reproduce the color images by aligning the plates and applying appropriate corrective filters. 

<img width="100%" alt="three channels" src="https://inst.eecs.berkeley.edu/~cs194-26/fa14/hw/proj1/proj1_files/image001.jpg" />

####Terrible Decisions
Sometimes you want an answer on a scale of 1 to 5, sometimes on a scale of 1 to 10. Sometimes, you want to know "on a scale of 1 to Kodak not getting into digital photography, how bad of an idea is this?" Some answers I got were:

["WindowsME"](https://en.wikipedia.org/wiki/Windows_ME#Reception)

["Atari Jaguar"](https://en.wikipedia.org/wiki/Atari_Jaguar)

The thing in question was not done. 

####Fossil Fuels and Post-apocalyptic Rebuilding
[Alex](http://alexmennen.com/) shared an interesting [article](aeon.co/magazine/technology/could-we-reboot-civilisation-without-fossil-fuels/) that explores the idea that we would not be able to have another industrial revolution after an apocalypse, since we've used up all the easy-to-access fossil fuels. The bottleneck could actually be not having enough power to get smelting temperatures high enough to work with metals. 

####NoSQL vs SQL
Just one of those things that I never explicitly studied. I know some SQL from [SQLzoo](http://sqlzoo.net/), but I'm not sure why exactly one would choose NoSQL over SQL or vice versa. Main points from [MongoDB](https://www.mongodb.com/nosql-explained) and this really interesting [interview](https://medium.com/s-c-a-l-e/amplab-s-co-creator-on-where-big-data-is-headed-and-why-spark-is-so-big-f0c0da2f7c0f) with Professor Michael Franklin of AMPLab about the historical perspective on NoSQL. 

Non-relational databases allow the insertion of data without a predefined schema. This is particularly useful in an environment where you're constantly taking in new streams of data and the ability to be flexible is more useful than having perfectly optimized queries every time. Support for auto-sharding is also helpful with horizontal scaling.

Different types of non-relational databases include:

- **Document databases**: docs contain key-value pairs, key-array pairs, or even nested documents.
- **Graph stores**: what it says on the can. Storing information as a graph data structure.
- **Key-Value stores**: The simplest kind. Some of these (like Redis) have support for typing.
- **Wide-column Stores**: (e.g. HBase and Cassandra) store data by column, and are optimized for querying large datasets. 

####It's gone meta!
My new all-time favorite Reddit [post](https://www.reddit.com/r/totallynotrobots/comments/3cmva7/i_have_discovered_a_subreddit_that_is_composed_of/). In which /r/totallynotrobots discovers /r/subredditsimulator. 

<small>Written with [StackEdit](https://stackedit.io/).</small>