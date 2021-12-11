# Variables can either be defined and directly used...
SOME_VAR="Hello World!"
echo $SOME_VAR
# or provided during script invocation like in this task. You
# can use the REPO_URL variable that points to a repository.

# Add your terminal commands here. Make sure to first run them
# locally on your machine to have more detailed error output.
git clone $REPO_URL repo
cd repo
printf "ccc" > c.txt
git add c.txt
git commit -m "Add new file c.txt with some content"
git push
