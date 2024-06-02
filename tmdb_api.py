import requests

url = "https://api.themoviedb.org/3/tv/66875/season/2/episode/1?language=ja-JP"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNTk0NTA2YWEyZjBkYmNjM2U4MTgzYjY3MzJiYTU1OCIsInN1YiI6IjY0MWIyYTY3ZDc1YmQ2MDBmNjljNWVlOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.iv9c3_dRSYVrmaQVDWieAzszCTeukyHZQP2nC3MhyAM"
}

response = requests.get(url, headers=headers)

print(response.text)