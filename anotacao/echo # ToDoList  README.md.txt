echo "# ToDoList" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Hoaska/ToDoList.git
git push -u origin main

PS C:\Users\ead\Aperfeiçoamento em Python> git confi --global --list

limpara as credenciais 
PS C:\Users\ead\Aperfeiçoamento em Python> git config --global --unset user.name
PS C:\Users\ead\Aperfeiçoamento em Python> git config --global --unset user.email

PS C:\Users\ead\Aperfeiçoamento em Python> git config --global --list   

coloca sua credenciasi
PS C:\Users\ead\Aperfeiçoamento em Python> git config --global user.name "ale09carvalho"
PS C:\Users\ead\Aperfeiçoamento em Python> git config --global user.email "ale09.carvalho@gmail.com"

PS C:\Users\ead\Aperfeiçoamento em Python> git config --global --list
user.name=ale09carvalho
user.email=ale09.carvalho@gmail.com

On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   conf_git/terminal no vs c.txt
        modified:   lista02/main.py
        modified:   lista03/main.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        atividadeLista01/maiin.py

no changes added to commit (use "git add" and/or "git commit -a")
==================================================================

O comando git add adiciona uma alteração no diretório de trabalho à área de staging

S C:\Users\ead\Aperfeiçoamento em Python> git add .
PS C:\Users\ead\Aperfeiçoamento em Python> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   atividadeLista01/maiin.py
        modified:   conf_git/terminal no vs c.txt
        modified:   lista02/main.py
        modified:   lista03/main.py

=======================================
já estão na stage para commitar 
PS C:\Users\ead\Aperfeiçoamento em Python> git commit -m "Segundo commit"  
agora criar a brench
git branch -M main

 git push 










xgh