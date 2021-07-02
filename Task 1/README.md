# Task 1

It seems a simple and straight-forward task. 

* Part 1

As the clue suggested, we have to look for branches, so I found 3 branches: "master", "develop", and "some". 
Firsty, I checked the "master" branch but found that all updates were made 12 months ago.
"Develop" was the branch the clue was placed, so I checked branch "some", and found the folder containing "something.md"

It had the part-1 of the flag: the type of hash used by git as default. I googled for it and easily found it - **SHA-1**

* Part 2

The 2nd clue was regarding the commits in github. So, I saw the commit history of "some" branch in github and saw 3 recent commits.
I checked the commit named "coommit".

It gave the part-2 of the flag: the default branch name used by Github - **main**

* Part 3

The 3rd clue suggested to look at the forks. I googled this and found the option under insights. The only interesting fork I could see is by ssl-team-aas. 
I found the "folder" there which contains the part-3 of the flag - the mechanism to automate tasks on github.

As the clue had already mentioned about Github Action, I started exploring it more. I got to know that how they work, its components like workflows, jobs, events, and so on.
As the task asked about the mechanism to automate tasks, I feel it should refer to **Workflows**.


**The Final Flag:**
1) SHA-1
2) main
3) Workflows

