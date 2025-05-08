AI & ML Jobs Dashboard

An interactive data dashboard for exploring AI and Machine Learning job trends, built with Streamlit, Pandas, Plotly, and Scikit-learn. This project helps you analyze job titles, salaries, and required skills to gain insights into the AI and ML job market.


Features

Job Search: Search for specific job titles.

Location Filtering: Filter jobs by location.

Salary Analysis: Visualize average salaries by location.

Skills Clustering: Discover clusters of similar jobs based on required skills.

Interactive Word Clouds: Explore the most common skills in the industry.

Advanced Data Filtering: Refine your analysis with dynamic filters.


Project Structure

AI_&_ML_Jobs/
├── README.md
├── AI_ML_Jobs_Dashboard.py
├── final_job_list.csv (add this file to .gitignore if it's too large)
├── requirements.txt
└── .gitignore


Installation

Clone this repository:

git clone https://github.com/yourusername/AI_ML_Jobs.git

Navigate to the project directory:

cd AI_ML_Jobs

Install the required packages:

pip install -r requirements.txt

Run the dashboard:

streamlit run AI_ML_Jobs_Dashboard.py


Data Source

The project expects a final_job_list.csv file in the project root directory. Ensure this file is present before running the dashboard.

Future Improvements

Integrate with live job data APIs (e.g., LinkedIn, Glassdoor).

Add geographical heatmaps for better location analysis.

Implement natural language processing for skill extraction.


License

This project is licensed under the MIT License.

Feel free to contribute and make this project even better!