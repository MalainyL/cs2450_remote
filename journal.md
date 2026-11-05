
8/26/26 Subject: Python 
    I've been having a hard time transitioning back to using python rather than c++. I had to look up the import keyword as I kept thinking that it was include. So heres a quick cheat sheet for me with python.

from x import y

def main():
    #no semicolons to end lines, and a pound sign for comments
    #also no need for curly braces and indentation matters
    x = 5   #no need to define types, although I can force a type
    print(f"The f formats so I can use values in code {x}")
    userIn = input("This is something I want to take from the user.")
    camelCase = 'is more used in python, also you can use " or \' for strings'
    #use def to define functions
    if this is not that:
        doThis()
        #dont use operators, use words, and rather than &&
        

    Also slightly related, I'm glad I've already taken care of keys, but it is a fairly straight-forward process in my opinion, just generate keys with ssh-keygen in the .ssh folder, than give github your PUB key info, not private. 
    Anyways, good first entry ig.
    Also, figure out the best way to format md files, this did not translate well.

9/4/26 Subject: Teamwork
    I hate when there isn't open communication in teams. I think our team has a few very strong willed people, (myself included in that), and some people that have strong opinions but aren't as willing to speak up, especially since there are some strong personalities. I think it doesn't help that some of us know each other, and some of us are new to the group.
    I don't think this will be a huge deal, but I think idea storming higlighted some team dynamics that could be a little rough :((. Hopefully by next week we will have thought about our ideas a bit more and we'll be able to come to an agreement with everyones opinion, and not just the opinion of whoever can talk the loudest. 
    Anyways. I keep forgetting the difference between import and include. C++ and Python consistently are messing with me. But I'll figure it out. I always do. Anyways. Until next time. 


9/9/26 Subject: Teamwork again
    I feel like I need to take charge of this and I really don't want to. Everyone is just waiting for someone else to say something and not contributing to the overall discussion. 
TBF we are all college students with a lot happening and we probably aren't super used to working in teams like this, but I feel like only a few of us are doing anything. I don't want to have to facilitate every conversation, and I know this would be far easier if I just did everything myself, but that isn't conductive to the environment and learning that I am supposed to be experiencing with this class. 
But I digress. The requirements need some tuning, we need to be more specific, but I don't want to try to discuss this over text and I have tests to study for. 
Regardless, I know we need to start working together more, maybe I'll start asking what specific people think to try to get some more invovlement out of every group member. I like being the scribe because I can make sure that things get done on my time, but maybe I should trust the members of my team a bit more. Anyways. Until next time. 


9/15/26 Subject: Git
    I wasn't aware that you need to make branches remote and on github, so that is interesting to me. To make a branch on your local computer, you use the command:  git checkout -b <branchName>
To make a branch on the github server, use: git push --set-upstream origin <branchName>
We also learned how to merge branches and make/approve pull requests. We need to delete the local branch on the local machine after
merging in git hub. Use: git branch -d <branchName> to delete on the local machine. also git checkout changes what branch you are currently in. 


9/22/26 Subject: Presenting
    I haven't ever really considered color use in a presentation before, but I guess it makes sence that it makes people feel certain things subconsciously. We've started on our presentation, and I think that our teamwork is going better now, like we've broken the seal and its easier to work with people you know a little better. 
Anyways, three main things to keep in mind when working on a presentation are: design principles, audience, and message. What we want to convey, the audience that we are conveying it to, and the way we want to convey it. I don't think thats too much to keep in mind, although I have written down the very basics, and thats what is important. 
Keep color in mind, as well as typeface, size, and other special things, like boldness and italics. 
Can use pictures to convey things as well, in fact, you should use pictures to convey things. A picture is easier than words for a lot of things, but it can also help propel your message. 

9/28 Subject: Project
    We need to meet as a group and go over our requirements again, as I think that a few of the things that are in the requirements and in the user stories are no longer accurate after we went over what we want in the slides. This is okay, and I know that things change and we've gone over our requirements more, but I also want to rebase now that we've discovered more about what we want to do. 
This class is more focused on the idea of development and working as a team then syntax, and I think that will be more useful in the long run, but I also need to go back and practice some syntax. As a quick reminder, its import in python and include in c++, c++ has semicolons and needs type definition while python does not. Yeah, short entry I guess. 


9/30 Subject: Presentations
    I think that we could've coordinated better for our presentation, but I think that we did fine. We talked after we presented and I think that we're all on the same page now, but we were slightly off when we presented. I also want to start coordinating a meeting between all of us but I know that Chris is busy with his capstone and Syd lives in hurricane so having a scrum once a week seems unlikely, unless I can convince everyone to start doing zoom together, which seems like an impossible task. 
But I digress, we all are on the same page and I am excited to start development next week. I need to continue working on cpp outside of class because I want to get better at it and I'm not going to learn it in any of the classes that I am taking or that I am planning on taking. 
I have mixed feelings about using excessive AI in this class, I think that it makes the class easier time wise and it makes it much faster, but I prefer to know everything that's going on, I guess thats the control freak in me. 
I don't think I'm using this journal correctly. I'm going to adjust the way that I use it to be more like a way to document what I'm doing rather than commenting on team dynamics. Anyways. Until next time. 

10/1 Subject: Scrum
    We talked about project management today, focusing on scrumming and being the scrum master. This is basically just a fancy term to meet up and discuss what has been done and what needs to be done. 

We will change scrum masters once a week, and whoever is the scrum master will send Professor Compas an email on the friday of this week telling him how many things have been completed, how many things are in progess, and how many things there are to still do. We will also give him a small update on what we've been doing and how things are going. 

10/8 Subject: AI
    We can use AI to enhance our workflows but we need to control how we use it rather than relying on AI to make all of the decisions. We still own the flow and what happens but the AI can do a lot of the steps. Its like we are the part of the person who makes good requirements and can communicate it, and the AI is the smart person that can implement it. 
AI can do whatever you tell it to but you need to give it good requirements. Supply a goal, supply a set of features that you want to be implemented. Give the AI the why, what, and the how.
Treat it like another team member, don't make it do all the work but you can delegate this.  

We used AI to fix the bug where a user can make a blank username and/or password. I used the copilot AI built into github since I am using vim and I don't think it's very helpful to install an AI tool into vim. I looked at what it returned to me and iterated a few times to fix some issues. Then I pushed everything that was changed to the github and called it a day after testing it extensively. It also won't allow spaces. 


10/13 Subject: Risk
    Companies risk a substansial amount when they develop software, things change quickly in this world and evrything to develop is a big risk. 
Requirements and talented developer. Good processes help us design things quickly and well. In this course we are learning to work together in a team and how to work through the software development process. Things go from us to git and back, then to the deployment pipeline, ending with the production environment. Then we can still have more progress. 
Continous integration is when we integrate over and over quickly into the source tree. Don't have floating tasks and branches. We need to keep things into smaller chunks so that things are being granular. Automated tests are also useful to speed up the process. Get rid out of as many bugs as possible while it's still in your testing environment. Solve the problem, send to the source, test quickly. Fail fast. 

Subject: Pair Programming
    This is when you work together as a team. Two people using the same computer to create code. There's a driver and a navigator, where one person works the computer and the other guides the process and notices issues with the work. There needs to be constant communication. Driver focuses on details and navigator things about the larger picture. Switch roles often. 
Sometimes it might be seen as not as productive for a company.

10/27 Subject: Software Quality
    We need to look at the user experience and see what they want from the application or experience. It also includes user security, updates. 
Qualities of Good Software:
    Correctness - Does it do what I want it to do?
    Reliability - Can the user use it like they need to when they need to? Does it do what you expect?
    Usability - Can the intended audience actually use it? It is easy enought or too hard?
    Performance - Is it fast enough?
    Maintainability - Can we change it later, did we make it modular enought and flexible enough to make further integration easier?
    Security - Is the user / user-data protected?

We need to implement quality, think thoughtfully about the design choices that we make, create simple architecture, have a good foundation (requirements), and following good coding principles. We should plan to fail clearly and early. 
Keep it simple stupid, fall clearly and early, structure matters, single purpose, easy to test.  
Don't hide errors, provide useful information to the user, try to avoid nested if statements, avoid poor logic in loops, short and simple functions, clear inputs and outputs, and good function parameters. 

11/5 Subject: Refactoring

I missed the lecture on this, as I was quite sick and couldn't come to class. I read through the assignment and worked on it, and I think that there is a lot to be said about learning someone else's code and making it better.
If you're refactoring your own code then it's easy to know what you are talking about, but sometimes it isn't so clear to others. 
I have realized how important properly documenting your code is, and I want to strive to make my code easier to understand by implementing with the best practices. 

I should really start working more on this project, it has kind of been on my backburner. 
