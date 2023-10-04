A repo for using in the project in quantum mechanics FMFF15
# working with git #
Allways start with a 
```
git status
```
if your working tree is fine, no files modified, do a 

```
git pull
```

then work away, when you feel finished for the day write 
```
git add -A
git commit -m "_ something to describe what you've done_"
git push
```
##  Start up # #

To run, open a terminal and go into a directory(cd home/_dir/) where you want to have the project.

In the terminal, write 
```
git clone _whatever_it_says_on_github 
``` 

You should also make sure you have python installed by runnin 
```
 python --version 
```

then run 
```
pip install numpy 
```

and you should be good to go! 


# Creating subplots
#fig, (axs1, axs2, axs3, axs4, axs5, axs6) = plt.subplots(6, 1, figsize = (8, 7))

# Plotting of the first subplot
# axs1.plot(Time, psiN[:, 0],Time, psiN[:, 1], 'r', label = 'Site 1')
# axs1.set_xlabel('Time')
# axs1.set_ylabel('|psi|² \n Site 1')     #Är detta nödvändigt?
# axs1.legend()

# # Plotting of the second subplot
# axs2.plot(Time, psiN[:, 1], 'b', label = 'Site 2')
# axs2.set_xlabel('Time')
# axs2.set_ylabel('|psi|²')
# axs2.legend()

# # Plotting of the second subplot
# axs3.plot(Time, psiN[:, 2], 'g', label = 'Site 3')
# axs3.set_xlabel('Time')
# axs3.set_ylabel('|psi|²')
# axs3.legend()

# # Plotting of the second subplot
# axs4.plot(Time, psiN[:, 3], 'r', label = 'Site 4')
# axs4.set_xlabel('Time')
# axs4.set_ylabel('|psi|²')
# axs4.legend()

# # Plotting of the second subplot
# axs5.plot(Time, psiN[:, 4], 'b', label = 'Site 5')
# axs5.set_xlabel('Time')
# axs5.set_ylabel('|psi|²')
# axs5.legend()

# Plotting of the second subplot
# axs6.plot(Time, psiN[:, 5], 'g', label = 'Site 6')
# axs6.set_xlabel('Time')
# axs6.set_ylabel('|psi|²')
# axs6.legend()

# for adjusting the space between subplots
# plt.tight_layout()
