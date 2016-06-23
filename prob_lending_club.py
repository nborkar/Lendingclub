import scipy.stats as stats
loansData.boxplot(column='Amount.Requested')

plt.show()

loansData.hist(column='Amount.Requested')
plt.show()



plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()