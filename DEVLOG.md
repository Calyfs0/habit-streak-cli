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


2026-11-19: Session 1 (Habit Streak v1): 1 star. Hand-traced 7 inputs; traced q -> int() ValueError -> inner loop. Wrote first spec; fixed 3 contradictions, added tests for 0, 2.5, Q, quit with 0. Learned int(2.5)=2 but int("2.5") raises ValueError.
Broke: spec contradictions (">7" vs test 7, wrong tomorrow math, plural in output); error message lied ("positive" rejects 2.5, excludes 0) -> decided: "a whole number, 0 or more".
Next: type fixes 1-3 from the spec (narrow try to line 16, one print, plurals) + new error message, run every spec test (0, 1, 7, 14, 15, 2.5, Q, quit with 0), then start Session 2 (lists, dicts -> v3).