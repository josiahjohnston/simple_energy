This git repository stores a brief introduction to Pyomo. This assumes you are
familar with git, a python programming environment, and have installed pyomo
and glpk on your machine. I should write instructions for that in a INSTALL
file, but that can wait for another day.

Assuming you have a python programming
environment set up, you can test your installation by executing simple_energy.py.
This should write the text file results.yml into your working directory. If 
that doesn't work, you'll have to troubleshoot & fix your installation before
you can get your hands dirty with experiments.

Learning Pyomo:
* You can start by skimming through simple_energy.py to see what you are in for.
* If you are an experienced programmer and energy modeller, this file as-is
  should get you started.
* If you want a better walk-through, open the git repo and go back to the
  earliest commit. This model starts from a single-variable optimization
  problem and gradually introduces pyomo and python concepts, in steps 
  recorded via git commits. Read through all of this.
* If you want to get to the next level, I recommend practicing writing.

Write your own version of this in a new file. Follow the pattern shown in this
git history:
* Start from something dead simple and test that it works.
* Commit that working copy to your local copy of the git repo.
* Move on in small increments, checking that it still works after every edit.
* You can reuse the equations, but don't copy and paste or just retype
  everything verbatim.
* If you are like most people, these tests will often fail .. from typos,
  having different expectactions of program/library behaviors, subtle
  mistakes with python syntax, etc. The process of debugging those errors
  is a huge part of this lesson. If you don't rewrite the model yourself,
  you'll miss out on that process of exploration and discovery. On the flip
  side, the model is simple enough that rewriting it won't take too long.
* Saving working versions and testing at each edit is important to minimize
  debugging frustrations and maximizing productivity. ..If you know an error is
  the result of a few lines of edits, it's way easier to track down and figure
  out.
