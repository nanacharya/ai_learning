import matplotlib.pyplot as plt

x=[2,4,5,9,16]
y = [3, 6, 2, 25, 4]
# plt.plot(x,y)
# plt.show()

#Line plot
# x= [1,2,3,4,5]
# y=[10,20,30,40,50]
# plt.plot([x,y], label = 'Line_plot')

#
#
# plt.plot([1,2,3,4],[20, 30, 40, 50] , label = 'Line_plot')
# plt.title('Line plot Learning')
# plt.xlabel('Money')
# plt.ylabel('Time')
# plt.legend()
# plt.show()


#Bar chart
# categoreis =["A","B","C","D","E","F","G","H"]
# values =[10, 5, 20, 10, 5, 30, 10, 5]
# plt.bar(categoreis,values,width=0.8, color='blue')
# plt.title("Bar Chart")
# plt.show()

#Histogram

# data= [1,2,2,4,5,6,4,4,9,1,1,1,4,0]
# plt.hist(data,bins=5, color='blue', edgecolor='black')
# plt.title("Histogram of data")
# plt.show()
#


# Scatter Plot
x=[2,4,5,9,16]
y=[3, 6, 2, 25, 4]
plt.scatter(x, y, color='red')
plt.title("scatter plot")
plt.show()
