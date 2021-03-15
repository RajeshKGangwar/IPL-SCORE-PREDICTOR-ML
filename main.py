# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'ipl-Score-prediction.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
    print("i am inside index")


@app.route('/predict', methods=['POST'])
def predict():
    temp_array = []

    if request.method == 'POST':
        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

        print("after batting")
        print(temp_array)

        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

        print("after bowling")
        print(temp_array)

        Stadium = request.form['match-Venue']
        Venue_list = ['Barabati Stadium', 'Brabourne Stadium', 'Buffalo Park',
                      'De Beers Diamond Oval', 'Dr DY Patil Sports Academy',
                      'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
                      'Dubai International Cricket Stadium', 'Eden Gardens',
                      'Feroz Shah Kotla',
                      'Himachal Pradesh Cricket Association Stadium',
                      'Holkar Cricket Stadium',
                      'JSCA International Stadium Complex', 'Kingsmead',
                      'M Chinnaswamy Stadium', 'MA Chidambaram Stadium, Chepauk',
                      'Maharashtra Cricket Association Stadium',
                      'New Wanderers Stadium', 'Newlands',
                      'OUTsurance Oval',
                      'Punjab Cricket Association IS Bindra Stadium, Mohali',
                      'Punjab Cricket Association Stadium, Mohali',
                      'Rajiv Gandhi International Stadium, Uppal',
                      'Sardar Patel Stadium, Motera', 'Sawai Mansingh Stadium',
                      'Shaheed Veer Narayan Singh International Stadium',
                      'Sharjah Cricket Stadium', 'Sheikh Zayed Stadium',
                      "St George's Park", 'Subrata Roy Sahara Stadium',
                      'SuperSport Park', 'Wankhede Stadium']

        print("after stadium")

        print(Venue_list)

        index_no = Venue_list.index(Stadium)
        dummy = [0] * 31
        dummy[index_no] = 1

        print(dummy)



    overs = float(request.form['overs'])
    runs = int(request.form['runs'])
    wickets = int(request.form['wickets'])
    runs_in_prev_5 = int(request.form['runs_in_prev_5'])
    wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])

    temp_array = temp_array + dummy + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]

    data = np.array([temp_array])
    my_prediction = int(regressor.predict(data)[0])

    return render_template('result.html', minimum_runs=my_prediction - 10, maximum_runs=my_prediction + 5)

#port = 5000
if __name__ == '__main__':
    #hostname = "0.0.0.0"
    app.run(debug=True)