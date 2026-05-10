import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score,mean_squared_error
import pickle


df = pd.read_csv("Hyd_cleaned.csv")

# Encode locality column
le=LabelEncoder()  #creating object
df["Location"] = le.fit_transform(df["Location"])


X = df[["Bhk", "Location"]]
y = df["Price"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)  #same split repeat avvadanki.
#  80% training   20% testing

model=LinearRegression().fit(X_train,y_train)
# y_pred=model.predict(X_test)
# r2=r2_score(y_test,y_pred)
# mse=mean_squared_error(y_test,y_pred)
# print("r2_score:",r2)
# print("mse:",mse)


# Save model
pickle.dump(model, open("model.pkl", "wb"))

# Save encoder
pickle.dump(le, open("encoder.pkl", "wb"))

print("Model Saved Successfully!")


# while True:

#     print("\n1. By Area")
#     print("2. By Price")
#     print("3. Exit")

#     choice = int(input("\nEnter Choice: "))

#     # =====================
#     # BY AREA
#     # =====================
#     if choice == 1:

#         location = input("Enter Area Name: ").lower()
#         bhk = int(input("Enter BHK: "))

#         found = False

#         for loc in le.classes_:

#             if location in loc.lower():

#                 loc_encoded = le.transform([loc])[0]

#                 prediction = model.predict([[bhk, loc_encoded]])

#                 print("\nLocation:", loc)
#                 print("Predicted Rent:", round(prediction[0]))

#                 found = True
#                 break

#         if not found:
#             print("Area not found!")

#     # =====================
#     # BY PRICE
#     # =====================
#     elif choice == 2:

#         amount = int(input("Enter Your Budget: "))
        

#         found = False

#         print("\nSuitable Areas:\n")

    
#         for i in range(len(df)):
#             price=df.iloc[i]["Price"]

#             if abs(price-amount)<=2000:
#                 location=le.inverse_transform([df.iloc[i]["Location"]])[0]
#                 bhk=df.iloc[i]["Bhk"]

#                 print(location, "->",bhk, "BHK -> Rent:",price)

#                 found=True

#         if not found:
#             print("No matching Areas found!")

#     # =====================
#     # EXIT
#     # =====================
#     elif choice == 3:
#         print("Thank You!")
#         break

#     else:
#         print("Invalid Choice!")