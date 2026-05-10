from flask import Flask,render_template,request
#creates web application , opens html page , gets data enter by user in forms
import pandas as pd  
import pickle  #used to load saved ml files

app=Flask(__name__)

df=pd.read_csv("Hyd_cleaned.csv") 

#loading model and encoder
model=pickle.load(open("model.pkl","rb"))
le=pickle.load(open("encoder.pkl","rb"))

# ============ HOME ===============
#create route for home page
@app.route("/")
def home():
    return render_template("index.html")

# ======================================================================
# area page
@app.route("/area")
def area():
    return render_template("area.html")

# price page
@app.route("/price")
def price():
    return render_template("price.html")

# ========================================================================


# ========== AREA ==============

@app.route("/predict_area",methods=["POST"])    #This route accepts form data using POST method.
def predict_area():
    location=request.form["location"].lower()   #gets loc from user 
    bhk=int(request.form["bhk"])

    for i in le.classes_:                 #Loop through all area names inside encoder.
        if location in i.lower():         #Checks whether user input matches any area.  kph -- kphb
            i_encoded=le.transform([i])[0]  #converts area names into numbers
            input_data=pd.DataFrame({
                "Bhk":[bhk],
                "Location":[i_encoded]
            })

            prediction=model.predict(input_data)
            result=f"{i}  [ Rent: {round(prediction[0])} ]"
            return render_template(
                "area.html",
                result=result
            )
    return render_template(
        "area.html",
        result="Area not found!"
    )

# ============ PRICE =========================

@app.route("/predict_price",methods=["POST"])
def predict_price():
    amount=int(request.form["amount"])   #Gets amount entered by user.
    Areas=[]

    for j in range(len(df)):     #Loops through every row in dataframe.
        price=df.iloc[j]["Price"]
        if abs(price - amount) <= 2000:  #Checks whether price is within ₹2000 range.
            location=df.iloc[j]["Location"]
            bhk=df.iloc[j]["Bhk"]
            Areas.append(   #Stores matching result.
                f"{location} --> {bhk} BHK --> Rent: {price}"

            )

    if not Areas:
        Areas.append("No matching areas found!")

    return render_template(
        "price.html",
        Areas=Areas
    )


if __name__=="__main__":
    app.run(debug=True)  #uto reload on changes