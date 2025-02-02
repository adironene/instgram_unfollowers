# instgram_unfollowers

Howdy. I'm tired of friends that get their information leaked by using 3rd party unfollower tracker so I wrote a script to do so.

## Instruction for tech people
1. download instagram data:
   1. profile > settings and activity > accounts center > information and permissions > download information
   2. select profile > some of your information > select followers and following > set date to all time
2. wait until the data is ready (it will be in the same place as above)
3. download that data and transfer it to a computer
4. run the script in the same directory as the unzipped parent folder of instagram download
5. you can modify the code to print the stuff in the other htmls files too

## Instruction for tech noobs
1. download instagram data:
   1. profile > settings and activity > accounts center > information and permissions > download information
   2. select profile > some of your information > select followers and following > set date to all time
2. wait until the data is ready (it will be in the same place as above)
3. download that data and transfer it to a computer 
   1. if it's downloaded on your phone, then you can email it over or airdrop if apple device
4. unzip the data on your computer
5. locate your terminal on your computer
   1. if you're on a mac, click on command + space and type in "terminal" then hit enter
6. find the path of your unzipped data folder. if you airdropped or downloaded off email, it's probably in downloads
7. in your terminal, type "cd PATH TO YOUR FOLDER"
   1. if it's in downloads, then it will be "cd Downloads"
8. then type "cat > script.py"
   1. and it will go to a new line
   2. go to the script.py file and copy everything
   3. paste it in the terminal
   4. after it's pasted in the terminal, type control + c or control + d
   5. that will save the rile
9. then "cat script.py" again and make sure the script is saved correctly
10. download python (https://www.python.org/downloads/)
11. once python is downloaded, go back to your terminal
    1.  make sure it's in the folder directory by typing pwd
    2.  if you're not in downloads/data folder or whatever path you were in, repeat steps above to be in the right directory
12. then type in your terminal "python3 script.py" or "python script.py"
13. it should print out the people that don't follow you back
14. if you run into any bugs, you probably don't know how to make a PR, so just email me at adironene@gmail.com