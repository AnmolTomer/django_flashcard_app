# Setting up version control

---

- Run the commands below if you are setting git for the first time on your machine. You need to run these once only.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@youraddress.com"
git config --global push.default matching
git config --global alias.co checkout
```

- After the above settings are done next steps are to initialize the git repo in a directory, and add files to staging area.

```bash
git init
git add --all or git add .
git commit -m "Message about changes done to project."
```

- For more on git commit check out this [link](https://git-scm.com/docs/git-commit)

- That's it for git. Everytime you have a stable app/website and you are about to do something major to your codebase, like creating a feature, first commit it to git.

- Create a new branch using `git branch new_feature_branch_name` , switch to that branch using `git checkout new_feature_branch_name`

- Finish implementing your changes on the feature branch. Once you are done, add, commit and push to a new branch on source repo using `git push origin new_feature_branch_name`

- Go to GitHub/GitLab/BitBucker or whatever site you are using, see the new PR from feature branch to master and check the diff, using CI define some tests if you want and merge if it's good.

---

## Connecting local git with your GitHub account

- Go to /c/Users/<username> with git bash type in the following `mkdir .ssh`

- Creates a new hidden folder called ssh for security purposes.

- cd to .ssh >> Type in `ssh-keygen.exe` to Generate ssh key. >> Enter passphrase if you want. Just hit enter twice if you don't want to enter the password, it will be blank in that case.

- If you see .ssh folder now you might notice `id_rsa` and `id_rsa.pub` files.

- `cat id_rsa.pub` will output a string copy this string and go to GitHub >> Settings >> SSH and GPG keys >> New SSH Key and Enter title and string you copied in key area, enter password to confirm that it is actually the owner who is entering the key.

- Create a new repo GitHub will show a similar command to push an existing repo from command line which will be something like this:

```bash
git remote add origin git@github.com:AnmolTomer/django_flashcard_app.git
git push -u origin master
```
