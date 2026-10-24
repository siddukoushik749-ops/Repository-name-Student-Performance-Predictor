from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
print("====================================")
print(" Student Performance Predictor ")
print("====================================")

hours = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
marks = [30, 40, 50, 60, 70, 75, 80, 85, 90, 95]

model = LinearRegression()
model.fit(hours, marks)
predicted_marks = model.predict(hours)
plt.scatter(hours, marks, color='blue', label='Actual Data')
plt.plot(hours, predicted_marks, color='red', label='Regression Line')
plt.legend()
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Student Performance Data")
plt.show()
hours_input = float(input("Enter study hours: "))

prediction = model.predict([[hours_input]])

print("Predicted Marks:", round(prediction[0], 2))

if prediction[0] >= 85:
    print("Performance Level: Excellent")
elif prediction[0] >= 70:
    print("Performance Level: Good")
else:
    print("Performance Level: Needs Improvement")