import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from django.shortcuts import render
from django.http import HttpResponse
from . models import Bookmain





def create_similarity():
    data = pd.read_csv('main_data.csv')
    data = data.drop_duplicates(['userID', 'bookTitle'])
    data_pivot = data.pivot(index='bookTitle', columns='userID', values='bookRating').fillna(0)
    data_matrix = csr_matrix(data_pivot.values)
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
    model_knn.fit(data_matrix)
    return data_pivot, data, model_knn


data_pivot, data, model_knn = create_similarity()


def rcmd(user_input_title):
    try:
        book_index = data_pivot.index.get_loc(user_input_title)
    except KeyError:
        return f"The book '{user_input_title}' is not in the dataset."

    distances, indices = model_knn.kneighbors(data_pivot.iloc[book_index, :].values.reshape(1, -1), n_neighbors=6)
    recommendations = [data_pivot.index[index] for index in indices.flatten() if index != book_index]

    if not recommendations:
        return "No recommendations found."
    else:
        return recommendations 






def home(request):
    return render(request, 'index.html')

def recommend(request):
    if request.method == 'POST':
        book_title = request.POST.get('movie')
        recommendations = rcmd(book_title)
        if isinstance(recommendations, str):
            return HttpResponse(recommendations)
        else:
            books = Bookmain.objects.filter(bookTitle__in=recommendations)
            return render(request, 'recommend.html', {'books': books}) 


