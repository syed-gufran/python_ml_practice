import streamlit as st
import pickle

model = pickle.load(open('/Users/syedgufrahussain/ds and ai/AQI_project/aqi_model.sav', 'rb'))

def AQI_bucket(AQI):
    if AQI >=13.0	and AQI<=50.0:
        return("AIR Quality is GOOD")
    elif AQI>=50.1	and AQI<=100.0:
        return("AIR Quality is Satisfactory")
    elif AQI>=100.1	and AQI<=200.0:
        return("AIR Quality is Moderate")
    elif AQI>=200.1	and AQI<=300.0:
        return("AIR Quality is Poor")
    elif AQI>=300.1	and AQI<=400.0:
        return("AIR Quality is Poor")
    else:
        return("AIR Quality is Severe")


def prediction(input_data):
    input_data =[input_data]
    prediction = model.predict(input_data)
    return AQI_bucket(prediction[0])

def main():
    st.title("Air Quality Index (AQI) Prediction")
    
    st.write("Enter the following parameters to predict the AQI:")
    #PM2.5	PM10	NO	NO2	NOx	NH3	CO	SO2	O3	Benzene	Toluene	Xylene
    pm25 = st.number_input("PM2.5 (ug/m3)", value=35.0)
    pm10 = st.number_input("PM10 (ug/m3)", value=50.0)
    no = st.number_input("NO (ug/m3)", value=5.0)
    no2 = st.number_input("NO2 (ug/m3)", value=20.0)
    nox = st.number_input("NOx (ug/m3)", value=30.0)
    so2 = st.number_input("SO2 (ug/m3)", value=10.0)
    nh3 = st.number_input("NH3 (ug/m3)", value=5.0)
    co = st.number_input("CO (mg/m3)", value=1.0)
    o3 = st.number_input("O3 (ug/m3)", value=25.0)
    benzene = st.number_input("Benzene (ug/m3)", value=1.0)
    toluene = st.number_input("Toluene (ug/m3)", value=1.0)
    xylene = st.number_input("Xylene (ug/m3)", value=1.0)
    if st.button("Predict AQI"):
        input_data = [pm25, pm10, no, no2, nox, nh3 , co, so2, o3, benzene, toluene, xylene]
        result = prediction(input_data)
        st.success(f"The predicted AQI is: {result}")

if __name__ == "__main__":
    main()