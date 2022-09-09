import os
from turtle import update
from git import Repo
from git import Git
import git

username = "Abhay-Jyot7" #Your github username here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
password = "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" #Your github password here (Use auth token for password )
number = int()
commit_message = ""


def commit_files(url , number , commit_message):
    repo_dir =  (r'C:\Users\abc\Desktop\newtest111') #Folder that is to be pushed to github
    file_name = os.path.join(repo_dir, 'work' ) #File/Folder inside the folder that is to be pushed to github i.e. in our case repo_dir


    if number == 0: #Case 1: If a new file is to be pushed to github (I.e. if the file is not present in the repo OR no .git folder )
        repo = Repo.init(repo_dir, env={"GIT_SSH_COMMAND": 'ssh -i ~/.ssh/id_rsa'}) #We need to add the ssh key and specify the path of the ssh key.
        repo.git.add(all=True) #Add the file to the repo
        repo.index.commit(commit_message) #Put a commit message
        repo.create_remote("origin", url=url)
        repo.remotes.origin.push(refspec='HEAD:refs/heads/main', force=True)
        #repo.git.push("origin" ,"main" ,force=True)      


    elif number == 1:#Case 3: If the file is already present in github and we want to update it in the main branch
        repo = Repo(repo_dir)
        repo.git.add([file_name])
        repo.index.commit(commit_message)
        repo.remotes.origin.push(refspec='HEAD:refs/heads/main', force=True)


    return     

def pull_files(url, number):
    repo_dir =  (r'C:\Users\abc\Desktop\newtest111') #Folder that is to be pulled from github
    file_name = os.path.join(repo_dir ,'work') #File/Folder inside the folder that is to be pulled from github i.e. in our case repo_dir
    #repo = Repo(repo_dir)
    repo = Repo.init(repo_dir , env={"GIT_SSH_COMMAND": 'ssh -i ~/.ssh/id_rsa'})
    repo.create_remote("origin", url=url)
    if number == 0:
        repo.git.pull(url) #Pulling from master branch
    elif number == 1:
        repo.git.pull(url, "master")
    elif number == 2:
        repo.git.pull(url, "qa")



    return


if __name__ == '__main__': 
    
    #commit_files(f"https://{username}:{password}@github.com/Abhay-Jyot7/munim1.git", number= 0, commit_message = "Message Check")#Use the url of the repository created in github   
    #commit_files(f"https://{username}:{password}@github.com/Abhay-Jyot7/munim2.git", number= 0, commit_message = "Message Check")#Use the url of the repository created in github     
    #commit_files(f"https://{username}:{password}@github.com/Abhay-Jyot7/munim3.git", number= 0, commit_message = "Message Check")#Use the url of the repository created in github     
    pull_files(f"https://{username}:{password}@github.com/Abhay-Jyot7/munim2.git", number= 0)

