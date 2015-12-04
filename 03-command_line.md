# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > Ten new commands that are new to me and very useul are:
pushd: pushes current directory into a list for later, allowing you to view another directory
popd: takes you back to the last directory you were viewing before you pushd
cp -r: copies a directory and its files
less: shows contents of file in an editor
more: shows contents of file in terminal output
cat >: overwrites a file
cat>>: appends a file
mdfind: find command that uses spotlight search database
grep: find string in a file
apropos: display list of topics in manual

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls: Displays a list of files in a directory.
ls-a: Displays a list with hidden files.
ls-l: Displays a list in a long format with columns for file permissions, owners, group, size, modifications and name.
ls-lh: Displays file size in human readable format (M, K, G)



---


---

What does `xargs` do? Give an example of how to use it.

xargs is used to remove or do some operation on a list of files that were produced by find, ls, grep, etc. commands. 
It executes a command by passing a constructed argument list(s) which are usually long lists of filenames passed to xargs via a pipe. 

example: find all files in finance folder and pass it to grep and search for expenses:
find ./finance -print | xargs grep "expenses" 
---

