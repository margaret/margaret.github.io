title: Things I learned this week - July 6th 2015
date: 2015-07-08 23:54
tags: python decorators; in-browser markdown editor; job hunting and self esteem; color displays; subreddit simulator; goddammit berkeley

##Things I Learned This Week: July 6th 2015

I've been meaning to get a blog started for years, but didn't know what to write about. In the spirit of breadth vs. depth,  I'm going to just dump some interesting things I learned about each week, a la the weekly links on [slatestarcodex](http://slatestarcodex.com/). I think I'll probably update each post throughout the week, since I suspect if I wait til the end of the week to write things up, I'll never actually write anything up. 

Should I have just incorporated an preexisting blogging platform into my site? Probably. But where's the fun in that? I don't really know much web dev so I'm going to take this opportunity to reinvent a few wheels. 

####Python Decorators
Ever seen Python functions immediately preceded by a little @thing ? Those are decorators. I was aware of them the semester I started learning Python, and I shamefully admit to blindly using frameworks that included them since then, but I realized that I didn’t *really* know what they did, so I decided to suck it up and Google it. 

[Simeon Franklin’s article](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/) gives a really nice functional explanation (that includes going over the concept of namespaces and closures) that’s worth a read. The main idea is that decorators allow you to modify existing functions. One way you could do this is:

1. Write function `foo`.
2. Realize it’d be really handy to be able to have foo, but with functionality X.
3. Write a `wrapper` function that takes in a function returns that same function, but with functionality X.
4. Reassign `foo = wrapper(foo)`

Decorators are syntactic sugar for step 4. Say you realize that it’d be great to add functionality X to arbitrary functions. Instead of manually feeding wrapper functions and reassigning them, you can simply define the wrapper function and then add `@wrapper` above any function you’d like to have its functionality. You can also do this where wrapper is a class (implement the things you want it to do in `self.__call__`) instead of a function. Learn more and see some examples on Bruce Ekel's [write-up on decorators](http://www.artima.com/weblogs/viewpost.jsp?thread=240808).

Namespaces, closures, arguments, and parameters are important concepts for understanding decorators because otherwise it gets confusing how the original functions could possibly have access to information that you might think should only exist in the local scope of the wrapper function, but the article I linked to does a good job explaining those, so I’ll leave it to them. 

####In-browser markdown editor
Found [this editor](https://stackedit.io/editor) when I looked for markdown editors that would also do the whole dual-mode editor and WYSIWYG thing. The UI reminds me of [ShareLatex](http://sharelatex.com/) (which is awesome, and if you ever need to type things up in LaTeX you should definitely check it out). I like it so far. It comes with integration with all the big cloud document services and lots of import/export options. It doesn't seem to support multiple people editing in-app at once, and I think it would be more helpful to have a more comprehensive toolbar instead of providing an example document that showcases all the possible markdown options, but overall nothing much to gripe about.

####Job hunting and self-esteem
I graduated at the end of May but I'm still looking for a job. I could do a whole post about why this is the case, but that's for another time. I noticed that it's not terribly hard for me to get interviews - I've been applying to on average about five places a week since I moved back home, and I usually get about a phone screen a week. But those rarely go anywhere, and I suspect that my low self-esteem is showing and I'm talking myself into a hole. Some soft skills I'm going to consciously work on when talking to people:

- Not ending otherwise perfectly good sentences with ". . . .and ...yeah....."
- Not rambling.
- Not using "just" as a qualifier. I didn't "just extend an unofficial API" for a thing, I "extended an unofficial API for a thing." 

####Color Displays
Why do the colors get all weird when you change the vertical angle that you view your monitor from?

[The answer](http://blogs.plos.org/mitsciwrite/2013/05/02/your-computer-screen-from-an-angle/), courtesy of MITsciwrite. 
To be honest, I wasn't able to completely grok why this happens, but from what I can tell it involves something like: Your computer screen displays colors is by controlling how much red, green, or blue light is exposed from each subpixel. This is done with a mechanism sort of like window blinds that can change angles, which will increase or decrease the amount of light that gets through. This all assumes that you are viewing your screen from the front. 

There was also an interesting explanation of gamma correction (our eyes detect brightness logarithmically, so why bother storing minute changes in brightness?), but I couldn't quite connect this with the information on angle viewing.  

Related: A "[gamut](https://en.wikipedia.org/wiki/Gamut)" is either the full color spectrum, or the subset covered by a colorspace or a physical method of representing color. 

I think in an alternate universe where I entered college as a Cognitive Science major, I would have ended up studying something in this field. Heck, for a minute I actually contemplated shelling out for this textbook, but I think I'll just settle for googling everything in the table of contents. :( I wish I hadn't sold my textbook from the class I took on perception.

####Subreddit Simulator
If you've been on reddit for a certain amount of time, you'll probably wonder if anyone would even notice if people just started submitting posts generated by Markov Chains because it seems like the same sort of crap just comes up over and over. Enter [/r/subredditsimulator](http://reddit.com/r/subredditsimulator).

####Goddammit Berkeley
This hilarious [tumblr blog](http://goddammitberkeley.tumblr.com/) showcases the most Berkeley parts of Berkeley. Sometimes all the hippie granola stuff gets annoying (and I say this as a liberal who follows a ~70% vegetarian diet), and I'm not a fan of playing "Human or Animal (poop)?" and "Skunk or Weed?" multiple times a day, but man, I love that city. Can't wait to move back. 

<sub>Written with [StackEdit](https://stackedit.io/).</sub>