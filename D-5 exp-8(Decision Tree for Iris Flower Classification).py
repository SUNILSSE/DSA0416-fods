from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

new_flower = np.array([[5.1, 3.5, 1.4, 0.2]])

predicted_species = model.predict(new_flower)
print(f'Predicted Species: {iris.target_names[predicted_species][0]}')

tree_rules = export_text(model, feature_names=iris.feature_names)
print(tree_rules)
