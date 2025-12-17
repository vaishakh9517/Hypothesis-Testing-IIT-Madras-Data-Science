# --- Importing necessary Libraries ---

import pandas as pd
import scipy.stats


# --- Importing and reading raw files ---

cars_data = pd.read_csv("D:/Git/Hypothesis-Testing-IIT-Madras-Data-Science/Data/Raw/cars_sampled.csv")
cars = cars_data.copy() 

print(cars.info())

cars = cars[(cars.yearOfRegistration <= 2018)           # working range of data
            & (cars.yearOfRegistration >= 1950)
            & (cars.price >= 100)
            & (cars.price <= 150000)
            & (cars.powerPS >= 10)
            & (cars.powerPS <= 500)]

print(cars.info())


# --- ONE SAMPLE TEST FOR MEAN ---

print("ONE SAMPLE TEST FOR MEAN")
print("3 years back the average price of a car was $6000. has it changed now?")

# h0 : u = $6000
# h1 : u != $6000
# sample stats : x
# sample std dev : s
# t-value = ? 
# critical values = ?
# computed uncertainity, p = ?
# decision on h0 = ?

sample_size = 1000
sample1 = cars.sample(sample_size, random_state= 0)

pos_mean = 6000     # postulated mean = 6000 (h0)
print("\nMean of the sample : ", sample1['price'].mean())

from scipy.stats import ttest_1samp

statistic, pvalue = ttest_1samp(sample1["price"], pos_mean)
print(f"The t-value is {statistic} and p-value is {pvalue}")


# --- Calculating Critical Values using Degress of Freedom ---

n = len(cars['price'])
df = n - 1
print("\nThe Degrees of Freedom of the Price Column is ", df)

alpha = 0.05

from scipy.stats import t       # package for t-distribution

cv = t.ppf([alpha/2, 1 - alpha/2], df)
print("The Critical Values are : ", cv)

print(f"""\nSince t-value {statistic} lies in BETWEEN the Critical Values {cv},
      and p-value, {pvalue} is greater than alpha {alpha}, the decision on ho is : Do NOT reject h0,
      conclude that the mean has NOT changed over the past 3 years, hence u= $6000.""")



# --- ONE SAMPLE TEST FOR PROPORTION ---

print("\n\n\nONE SAMPLE TEST FOR PROPORTION")
print("3 years back, the percentage of used car with automatic transmission was 23%. Has it changed now?")

# h0 : pi = 0.23
# h1 : pi != 0.23
# sample stats = p-hat
# z value = ?
# critical values = ?
# p = ?
# decision on h0 = ?

alpha = 0.05
p0 = 0.23

from statsmodels.stats.proportion import proportions_ztest     # importing packge for 1 sample z-test
count = sample1['gearbox'].value_counts().iloc[1]
nobs = len(sample1['gearbox'])
print("\nThe Proportion of Automatic Transmission gearbox : \n", count/nobs)

statistic_oneprop, pvalue_oneprop = proportions_ztest(count = count, nobs = nobs,
                                                      value = p0, alternative = 'two-sided',
                                                       prop_var= False )
print(f"\nThe z-value is {statistic_oneprop} and p-value is {pvalue_oneprop}")

from scipy.stats import norm        # importing normal distribution
cv_norm = norm.ppf([alpha/2, 1-alpha/2])
print("\nThe Critical Values are  : ", cv_norm)

print(f"""\nSince z-value {statistic_oneprop} lies in BETWEEN the Critical Values {cv_norm},
      and p-value, {pvalue_oneprop} is greater than alpha {alpha}, the decision on ho is : Do NOT reject h0,
      conclude that the proportion has NOT changed over the past 3 years, hence pi = 0.23 (23%).""")




# --- TWO SAMPLE TEST FOR MEANS ---

print("\n\n\nTWO SAMPLE TEST FOR MEAN")
print("""\nTo check if the mean price of cars that have run 30,000 - 60,000 kms are equal to 
      the price of cars that have run 70,000 - 90,000 kms.""")

# h0 : u1 = u2
# h1 : u1 != u2
# sample stats : x
# test stats : depends whether the 2 groups have equal variance or not
# critical value = ?
# p = ?
# decision on h0 = ?

alpha = 0.05

# --- Checking Variance ---

km_70k_90k = cars[(cars.kilometer <= 90000)
                  & (cars.kilometer >= 70000)]
km_30k_60k = cars[(cars.kilometer <= 60000)
                  & (cars.kilometer >= 30000)]

sample_70k_90k = km_70k_90k.sample(500, random_state = 0)       # 500 samples from each set
sample_30k_60k = km_30k_60k.sample(500, random_state = 0)

print("\nThe Variance of 70k-90k set : ", sample_70k_90k.price.var())
print("The Variance of 30k-60k set : ", sample_30k_60k.price.var())
print("Both have UNEQUAL variances.")

print("\nThe sample mean of 70k-90k set : ", sample_70k_90k.price.mean())
print("The sample mean of 30k-60k set : ", sample_30k_60k.price.mean())

print("\nSince both have UNEQUAL variance, we will first calculate F-Statistic")
print("""\nWe will check test statistics (F-Statistics), critical vaules and p for F-distribution,
        and check for the hypthoses : ho :  s = s, or h1 = s != s""")

from scipy.stats import f       # import f statistic package

F = sample_70k_90k.price.var()/sample_30k_60k.price.var()
print("\nThe ratio of both the variances is : ", F)

# --- Calculating Degrees of Freedom ---

df2 = len(sample_70k_90k) - 1
df1 = len(sample_30k_60k) - 1

p_value_F = scipy.stats.f.cdf(F, df1, df2)
print("The p-value for the F-statistic is : ", p_value_F)

cv_F = f.ppf([alpha/2, 1 - alpha/2], df1, df2)
print("\nThe Critical Values for the F-statistic are : \n ", cv_F )

print(f"""\nSince the F-statistic {F} does NOT lie in the critical values {cv_F}
      and the p-value {p_value_F} is less than alpha {alpha}, we REJECT ho. Hence s != s""")


# --- Welch t-test for unequal variances ---

from scipy.stats import ttest_ind

statistic_2mean, pvalues_2mean = ttest_ind(sample_30k_60k.price, sample_70k_90k.price, equal_var= False)
print("\nThe t-statistics and p-value are : ", statistic_2mean, pvalues_2mean)

# --- Calculating Critical values through Degrees of Freedom ---

N1 = len(sample_30k_60k)
N2 = len(sample_70k_90k)
s12 = sample_30k_60k.price.var()
s22 = sample_70k_90k.price.var()

df = (((s12/N1) + (s22/N2))**2) / (((s12/N1)**2/(N1-1)) +(((s22/N2)**2)/(N2-1)))

print("\nDegrees of Freedom : ", df)

cv_t = t.ppf([alpha/2, 1 - alpha/2], df)
print("\nThe Critical Values are : ", cv_t)

print(f"""\nThe t-statistics {statistic_2mean} does NOT lie between the critical values
       {cv_t} and p-value {pvalues_2mean} is less than alpha, we REJECT ho. Hence
       we conclude u1 != u2 i.e., mean price of cars from the sets are different.""")



# --- TWO SAMPLE TEST FOR PROPORTION --- 

print("\n\n\nTWO SAMPLE TEST FOR PROPORTIN")
print("""Are the proportion of petrol cars in 2 differentent time periods 2009-2013 and
        2014-2018 different?""")

# h0 : pi1 = pi2
# h1 : pi1 != pi2
# sample stats = p-hat
# z-value = ?
# critical values = ?
# p = ?

alpha = 0.05

year_14_18 = cars[(cars.yearOfRegistration <= 2018)             # subsetting
                  & (cars.yearOfRegistration >= 2014)]
year_09_13 = cars[(cars.yearOfRegistration <= 2013)
                  & (cars.yearOfRegistration >= 2009)]

sample_14_18 = year_14_18.sample(1000, random_state = 0)        # sampling
sample_09_13 = year_09_13.sample(1000, random_state = 0)

count = [(sample_14_18['fuelType'] == 'petrol').sum(), (sample_09_13['fuelType'] == 'petrol').sum()]
nobs = [len(sample_14_18), len(sample_09_13)]
print("\nProportion on petrol cars in 2014-18 set : ", count[0]/nobs[0])
print("Proportion on petrol cars in 2009-13 set : ", count[1]/nobs[1])

statistic_2prop, pvalue_2prop = proportions_ztest(count = count, nobs = nobs,
                                                  value = 0, alternative = 'two-sided',
                                                  prop_var = False)

print("\nThe z-value and p-value are : ", statistic_2prop, pvalue_2prop)

cv_2prop = norm.ppf([alpha/2, 1 - alpha/2])
print("\nThe Critical Values are : ", cv_2prop)

print(f"""\nSince the z-value {statistic_2prop} LIES between the critical values
       {cv_2prop} and p-value {pvalue_2prop} is GREATER than alpha, we do NOT reject ho.
       Hence we conclude pi1 = pi2, i.e., the proportions of cars in the two given time
       periods are same.""")
