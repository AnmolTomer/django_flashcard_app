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
