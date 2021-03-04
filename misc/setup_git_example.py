# setup repo
# go to AWS code commit
# https://us-west-1.console.aws.amazon.com/codesuite/codecommit/repositories?region=us-west-1
# name it and add files

# git --version
# install git via web link
# cd to folder
# git init
# git status # see all untracked files
# # create .gitignore file --Python version

# add any other files from git status that we want to ignore.
# git add --all # add all files
# git commit -m "message" # added new function that handles this

# git push origin master
##create readme file,
# pip freeze > requirements.txt file
##echo "test1" >> README.md
##git add README.md
##git commit -m "first commit"
##
##git remote add origin https://github.com/parndtls1-test/Test1.git
##git push -u origin master # enter username and password to github #parndtls1biz@gmail.com password

# git log # review changes
##git checkout <commit hash>
##git checkout -b <new branch name>
##
##git diff <commit hash> <filename>
##git reset <commit hash> <filename> # revert file to that commit
##
### merge your change
##git checkout <my branch>
##git rebase master
##git checkout master
##git merge <my branch>