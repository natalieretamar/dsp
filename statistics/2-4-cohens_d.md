[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

This task required the use of Cohen's D to compute the effect size between 2 groups. I used two simple integer
lists to represent the two groups of data being compared. Numpy was imported in order to use its mean, and standard deviation methods.

The formula for [Cohen's D](http://trendingsideways.com/index.php/cohens-d-formula/) is easily explained at this website.

Code: 
```python
import numpy as np
#Two simple data list groups
g1 = np.array([2, 4, 7, 3, 7, 35, 8, 9],int)
g2 = np.array([7,13,5,1,26,4,],int)
#Difference of means
mean_diff = g1.mean()-g2.mean()
#Standard deviation squared
sd_g1= np.std(g1)**2
sd_g2= np.std(g2)**2

cohens_d = mean_diff/(np.sqrt(((sd_g1+sd_g2)/2)))
print cohens_d 
```
