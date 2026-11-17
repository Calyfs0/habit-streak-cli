17/11/2026.
Did?
I wrote the first version of habit tracker where I asked user's habit first, then number of days he has been doing this habit. I keep on asking different habits unless user types Q or q. I also added validations for empty string checks, wrong input type such that negative number for days. I also said weeks if days exceeded 7 days.
Broke?
five crashed as ValueError if I try to convert days_done to int.
Empty strings and upper case Q were added as habits.
<=0 rejected 0 days.
I think I need to work on edge cases, plan each step thoroughly. I shouldn't rush in writing code either on paper or machine.
Learned?
I learned that we don't have to use continue in except block. input() returns a string always. TypeError vs ValueError. "" is a falsy not false, and "xyz" is a truthy not True. continue skips to the next iteration, break exits the loop. 